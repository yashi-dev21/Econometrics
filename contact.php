<?php
	$name = $_POST['name'];
	$email = $_POST['email'];
	$message = $_POST['message'];

	$to = 'yashikamule219@gmail.com';
	$subject = 'Contact Form Submission';

	$body = "From: $name\nEmail: $email\n\n$message";

	mail($to, $subject, $body);
?>