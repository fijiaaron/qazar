<?php
	$url = $_SERVER['REQUEST_URI']
	$urlbase = "/";
	$suffix = ".html";

	$pagename = $_REQUEST
	$page = $urlbase . $pagename . $suffix;
?>

<h1> Display </h1>
<hr>

<?php include($page);