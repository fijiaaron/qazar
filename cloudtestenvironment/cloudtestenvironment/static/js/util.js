String.prototype.contains = function(it) { return this.indexOf(it) != -1; };

function includeScript(script_src) {
	script_start_tag= '%3Cscript';
	script_end_tag = '%3E%3C/script%3E';
	script_local_jquery = script_start_tag + ' src="' + script_src + 'type="text/javascript"' + script_end_tag;

	document.write(unescape(script_local_jquery));
}