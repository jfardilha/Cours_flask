from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap

def create_app():
    app = Flask(__name__)
    Bootstrap(app)

    @app.route('/')
    def index():
        user_agent = request.headers.get('User-Agent')
        return f"<p> Your browser is {user_agent}</p>\n<h1>ECM Bonjour</h1>"

    @app.route('/user/<name>')
    def user(name):
        return render_template('user.html', name=name)

    @app.route('/professor')
    def my_api_route():
        return {
            "name": "Adrien",
            "birthday": "02 January",
            "age": 85,
            "sex": None,
            "friends": ["Amadou", "Mariam"]
        }

    return app


