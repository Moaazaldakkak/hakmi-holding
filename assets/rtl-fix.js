/**
 * RTL fixes for index-rtl.html
 * - Resets ElementsKit nav menu translateX offset
 * - Rebuilds testimonials carousel in LTR mode (tiny-slider breaks under dir=rtl)
 */
(function () {
	'use strict';

	function fixOverflow() {
		document.documentElement.style.overflowX = 'hidden';
		document.body.style.overflowX = 'hidden';
	}

	function fixNavMenu() {
		document.querySelectorAll('.elementskit-menu-container').forEach(function (el) {
			el.style.transform = 'none';
			el.style.position = 'relative';
			el.style.left = 'auto';
			el.style.right = 'auto';
			el.style.inset = 'auto';
		});
	}

	function watchNavMenu() {
		document.querySelectorAll('.elementskit-menu-container').forEach(function (el) {
			var observer = new MutationObserver(fixNavMenu);
			observer.observe(el, { attributes: true, attributeFilter: ['style'] });
		});
	}

	function patchTinySlider() {
		if (typeof window.tns !== 'function' || window.__rtlTnsPatched) {
			return;
		}

		var originalTns = window.tns;
		window.tns = function (options) {
			options = options || {};
			options.rtl = false;
			return originalTns(options);
		};
		window.__rtlTnsPatched = true;
	}

	function getUniqueTestimonialItems(track) {
		var seen = Object.create(null);
		var items = [];

		track.querySelectorAll('.testimonial-item').forEach(function (item) {
			var match = item.className.match(/elementor-repeater-item-[a-f0-9]+/);
			var key = match ? match[0] : item.outerHTML;

			if (!seen[key]) {
				seen[key] = true;
				items.push(item.outerHTML);
			}
		});

		return items;
	}

	function buildResponsiveConfig(settings) {
		var defaults = {
			0: { items: 1, gutter: 0 },
			768: { items: 2, gutter: 0 },
			1025: { items: 3, gutter: 10 }
		};
		var responsive = {};

		Object.keys(settings.responsive || {}).forEach(function (key) {
			var bp = settings.responsive[key];
			var breakpoint = bp.breakpoint;
			var fallback = defaults[breakpoint] || defaults[0];

			responsive[breakpoint] = {
				items: bp.items !== '' ? bp.items : fallback.items,
				gutter: bp.margin !== '' ? bp.margin : fallback.gutter
			};
		});

		return responsive;
	}

	function rebuildTestimonialsCarousel() {
		var wrapper = document.querySelector('.jkit-testimonials[data-id]');
		if (!wrapper || wrapper.dataset.rtlCarouselReady === '1') {
			return;
		}

		if (typeof window.tns !== 'function' || typeof jQuery === 'undefined') {
			return;
		}

		var list = wrapper.querySelector('.testimonials-list');
		var track = wrapper.querySelector('.testimonials-track');
		if (!list || !track) {
			return;
		}

		var items = getUniqueTestimonialItems(track);
		if (!items.length) {
			return;
		}

		var settings = jQuery(wrapper).data('settings');
		var dataId = wrapper.getAttribute('data-id');
		if (!settings || !dataId) {
			return;
		}

		var outer = wrapper.querySelector('.tns-outer');
		if (outer) {
			outer.remove();
		}

		list.innerHTML = '<div class="testimonials-track">' + items.join('') + '</div>';
		wrapper.style.direction = 'ltr';
		list.style.direction = 'ltr';

		var slider = window.tns({
			container: '.jkit-testimonials[data-id="' + dataId + '"] .testimonials-track',
			loop: true,
			mouseDrag: true,
			autoplay: settings.autoplay,
			autoplayTimeout: settings.autoplay_speed,
			autoplayHoverPause: settings.autoplay_hover_pause,
			navPosition: 'bottom',
			controlsPosition: settings.arrow_position,
			controlsText: [settings.navigation_left, settings.navigation_right],
			responsiveClass: true,
			responsive: buildResponsiveConfig(settings),
			rtl: false
		});

		jQuery(wrapper).find('button[data-action]').remove();

		if (settings.show_navigation) {
			jQuery(wrapper).find('.tns-controls').show();
		} else {
			jQuery(wrapper).find('.tns-controls').remove();
		}

		if (settings.show_dots) {
			jQuery(wrapper).find('.tns-nav').show();
		} else {
			jQuery(wrapper).find('.tns-nav').remove();
		}

		if (slider && typeof slider.goTo === 'function') {
			slider.goTo(0);
		}

		wrapper.dataset.rtlCarouselReady = '1';
		fixOverflow();
	}

	function fixTextAlignment() {
		var selectors = [
			'.elementor-heading-title',
			'.elementor-widget-text-editor',
			'.elementor-widget-text-editor p',
			'.elementor-icon-box-description',
			'.testimonial-box',
			'.comment-content',
			'.comment-content p',
			'.jkit-button',
			'.jkit-postblock-content'
		];

		selectors.forEach(function (selector) {
			document.querySelectorAll(selector).forEach(function (el) {
				if (getComputedStyle(el).textAlign === 'left') {
					el.style.textAlign = 'right';
					el.style.direction = 'ltr';
				}
			});
		});
	}

	function scheduleCarouselRebuild() {
		setTimeout(rebuildTestimonialsCarousel, 300);
		setTimeout(rebuildTestimonialsCarousel, 1200);
		setTimeout(function () {
			rebuildTestimonialsCarousel();
			fixTextAlignment();
		}, 2500);
	}

	function init() {
		fixOverflow();
		fixNavMenu();
		watchNavMenu();
		fixTextAlignment();
	}

	patchTinySlider();
	fixOverflow();

	if (document.readyState === 'loading') {
		document.addEventListener('DOMContentLoaded', init);
	} else {
		init();
	}

	window.addEventListener('load', function () {
		fixNavMenu();
		scheduleCarouselRebuild();
	});

	if (typeof jQuery !== 'undefined') {
		jQuery(window).on('elementor/frontend/init', scheduleCarouselRebuild);
	}
})();
