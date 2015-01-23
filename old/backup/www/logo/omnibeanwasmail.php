<?php
//http://www.omnibean.net16.net/omnibean/php/mailomnibeanwas.php
$rcv = $_GET['rcv']; // = 1
$name = $_GET['name']; // = 2
$nname = $_GET['nname']; // = 3

$To = $rcv;
$Subject = "OmniBean Get Website-Your Confirmation Email";
$Message = "I would like to get sponsor page (right)!". PHP_EOL 
           ." My name is: ".$name. PHP_EOL 
           ."My email is: ".$rcv. PHP_EOL 
           ."My nickname is: ".$nname;
$Headers = "From: omnibean@outlook.com \r\n" .
"Reply-To: omnibean@outlook.com \r\n" .
"Content-type: text/html; charset=UTF-8 \r\n";

//echo('Sent To:'.$rcv."\r\n");
//echo('Subject:'.$Subject."\r\n");
//echo('Message:'.$Message."\r\n");

//echo($rcv);
mail($To, $Subject, $Message, $Headers);
$To = 'omnibean@outlook.com';
mail($To, $Subject, $Message, $Headers);
//$message = "Confirmation Email was sent to: ".$rcv."\nRedirecting to OmniBean Home...";
//echo "<script type='text/javascript'>alert('$message');</script>";
header("Location: http://www.omnibean.weebly.com");


?>