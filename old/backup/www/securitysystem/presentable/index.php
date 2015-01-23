<!doctype html>
<html class="no-js" lang="en">
  <head>
	
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Security System - Presentation</title>
    <link rel="stylesheet" href="css/foundation.css" />
    <script src="js/vendor/modernizr.js"></script>
  </head>
  <body> 
<a href="#" class="button" data-reveal-id="indevModal">Log In</a> <br>
<div id="indevModal" class="reveal-modal" data-reveal>
  <h2>Enter Password:</h2><br>
<form ><!--action="functioncalling.php">-->
    <input type="password" name="txt" />
    <!--<input type="submit" name="insert" value="insert" onclick="insert()" />-->
    <input type="submit" name="select" value="Go" onclick="select()" />
</form>
  <a class="close-reveal-modal">&#215;</a>
</div>	
      
    <script src="js/vendor/jquery.js"></script>
    <script src="js/foundation.min.js"></script>
    <script>
      $(document).foundation();
	//$(document).ready(function(){$('#indevModal').foundation('reveal', 'open')});
    </script>
  </body>
</html>
<?php
$password = file_get_contents('password.pw');
$LOG = file_get_contents('logfile.pw');
$pass = $_GET['txt'];
if ($pass == $password)
{
	echo "Correct Password.<br>";
	echo 'Starting log file writer...<br>';
	//exec('python /home/pi/securitysystem/test_logwriter.py');
	//	file_put_contents('trigger.pw','Triggered...');
	sleep(2);	
	echo 'Log File: <br>'.$LOG;


}
if ($pass != $password)
{
   echo 'Incorrect Password.';
}
//select()
//function select(){
//   echo "The select function is called.";
//}
//function insert(){
//   echo "The insert function is called.";
//}
?>