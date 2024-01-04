$(function() {
	$.get('https://hellosalut.stefanbohacek.dev/?lang=fr', function(data, textStatus) {
		if (textStatus === 'success') {
				$('DIV#hello').text(data.hello)
			}
		})
});
