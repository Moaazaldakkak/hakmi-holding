<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $name = htmlspecialchars(trim($_POST['name']));
    $email = htmlspecialchars(trim($_POST['email']));
    
    if (empty($name) || empty($email)) {
        http_response_code(400);
        echo "Name and email are required.";
        exit;
    }
    
    if (!filter_var($email, FILTER_VALIDATE_EMAIL)) {
        http_response_code(400);
        echo "Invalid email format.";
        exit;
    }
    
    $to = "moaazaldakak1997@gmail.com";
    $subject = "New Notification Request from Hakmi Holding";
    $message = "Name: $name\nEmail: $email";
    $headers = "From: $email\r\nReply-To: $email\r\nContent-Type: text/plain; charset=UTF-8\r\n";
    
    if (mail($to, $subject, $message, $headers)) {
        http_response_code(200);
        echo "success";
    } else {
        http_response_code(500);
        echo "Failed to send email. Please try again later.";
    }
} else {
    http_response_code(405);
    echo "Method not allowed.";
}
?>