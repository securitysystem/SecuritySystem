<html>
<h1>Security System - Control Panel</h1>
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
}?>