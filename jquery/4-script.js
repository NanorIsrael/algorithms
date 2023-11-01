$(function() {
	$('#toggle_header').on('click', function() {
		const cls = $('header').attr('class')
		$('header').removeClass(cls);
		if (cls === 'red') {
			$('header').addClass('green');
		}
		if (cls === 'green') {
			$('header').addClass('red');
		}
	})
});
