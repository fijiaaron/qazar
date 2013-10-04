<?php
	$url = $_SERVER['REQUEST_URI'];
	$urlbase = "/";
	$suffix = ".html";

	$pagename = "landing";
	$page = $urlbase . $pagename . $suffix;
?>

<h1> Display </h1>
<hr>
<?= $url ?>
<?php include($page); ?>