<?php
// the message
$msg = "Security Breach";

// use wordwrap() if lines are longer than 70 characters
$msg = wordwrap($msg,70);

// send email
mail("talur.nihal@outlook.com","Security Breach",$msg);
?> 