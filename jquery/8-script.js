$(function() {
	$.get('https://swapi-api.alx-tools.com/api/films/?format=json', function(data, textStatus) {
		if (textStatus === 'success') {
				for (let movie of data.results) {
					$('<li></li>').text(movie.title).appendTo('UL#list_movies')
				}
			}
		})
});
