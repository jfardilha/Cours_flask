from flask import Flask, request, render_template

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        user_agent = request.headers.get('User-Agent')
        return f"<p> Your browser is {user_agent}</p>\n<h1>ECM Bonjour</h1>"

    @app.route('/user/<name>')
    def user(name):
        return render_template('user.html', name=name)

    return app


