<html>
<head>
<title>Online LED</title>
<link rel="stylesheet" href="../css/foundation.css" />
</head>

<body>
<div class="row">
Turn the LED <form method="post"><input type="submit" name="action" value="on" label="Turn on the LED"/><br></form>
</div>
</body>
</html>
<?php
//ini_set('display_errors',1);
//ini_set('display_startup_errors',1);
//error_reporting(-1);
echo 'Online LED<br>';
$action = $_POST['action'];

if ($action == 'on'){
//echo 'PHP- LED turned On. [Blink 5 sec]';
file_put_contents('led.pw','on');
exec('sudo python ledon.py');
}
else if ($action == 'off'){
//echo 'PHP LED Off.';
exec('sudo python ledon.py');
}
else
{
echo 'Invalid Command';
}
?>