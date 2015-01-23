<html>
<head><link rel="stylesheet" href="../css/foundation.css" /></head>
<body>
<div class="row">
<h2>Enter Password:</h2><br>
<form ><!--action="functioncalling.php">-->
    <input type="password" name="txt" />
    <!--<input type="submit" name="insert" value="insert" onclick="insert()" />-->
    <input type="submit" name="select" value="Go" onclick="select()" />
</form>
<a href="led.php">Try the Online LED</a>
<a href="presentable/index.php">Presentable Edition</a>
</div>
<?php
$password = file_get_contents('password.pw');
$LOG = file_get_contents('logfile.pw');
$STATUS = file_get_contents('status.pw');

$pass = $_GET['txt'];
if ($pass == $password)
{
	echo "Correct Password.<br>";
	echo 'Starting log file writer...<br>';
	//exec('python /home/pi/securitysystem/test_logwriter.py');
	//	file_put_contents('trigger.pw','Triggered...');
	//sleep(2);	
        echo 'Status of Security System (Live):<br>'.$STATUS;
	//echo 'Log File: <br>'.$LOG;
	//echo '<script>setTimeout(function () {   window.location.href = "#";}, 2000); </script>';
	echo '<meta http-equiv="refresh" content="2" >';

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