#!/usr/bin/env python3
"""Test for utilities.py.
"""


@app.before_request
def before_request() -> None:
    """Performs some routines before each request's resolution.
    """
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Retrieves the locale for a web page."""
    try:
        queries = request.args.to_dict()
        locale = queries.get('locale')
        if locale and locale in app.config["LANGUAGES"]:
            return locale
    except Exception as e:
        app.logger.error(f"Error processing request query parameters: {e}")

    # Resort to default behavior if locale not provided or invalid
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route('/')
def get_indexi() -> str:
    """ Prints a Message when / is called """
    g.locale = str(get_locale())
    return render_template('5-index.html')


if __name__ == "__main__":
    """ Main Function """
                                                                                                                               38,1          96%
