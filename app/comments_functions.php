<?php

function get_topics_from_url($url) {
	$topics = array();
	
	$tokens = preg_split("/\p{P}/", $url);

	foreach($tokens as $topic) {
		if (empty($topic)) { continue; } // skip empty

		$ignored = array("php", "html");
		if (in_array($topic, $ignored)) { continue; } // skip file ending

		$topics[] = $topic;
	}

	return $topics;
}

function get_comments_in_topics($topics, $db) {
	// $pdo = new PDO($db);
}