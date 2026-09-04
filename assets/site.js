(() => {
	const header = document.querySelector(".site-header");
	if (!header) return;

	const toggle = header.querySelector(".nav-toggle");
	const nav = header.querySelector(".site-nav");
	const subItems = header.querySelectorAll(".nav-item--has-sub");

	if (toggle && nav) {
		toggle.addEventListener("click", () => {
			const open = nav.classList.toggle("is-open");
			toggle.setAttribute("aria-expanded", open ? "true" : "false");
			if (!open) {
				subItems.forEach((item) => item.classList.remove("is-open"));
			}
		});
	}

	subItems.forEach((item) => {
		const button = item.querySelector(":scope > button");
		if (!button) return;

		button.addEventListener("click", (event) => {
			if (window.matchMedia("(max-width: 980px)").matches) {
				event.preventDefault();
				item.classList.toggle("is-open");
			}
		});
	});

	document.addEventListener("click", (event) => {
		if (!header.contains(event.target)) {
			nav?.classList.remove("is-open");
			toggle?.setAttribute("aria-expanded", "false");
			subItems.forEach((item) => item.classList.remove("is-open"));
		}
	});
})();
