import os
from flask_migrate import Migrate, MigrateCommand
from flask_sqlalchemy import SQLAlchemy
from flask import Flask, request, render_template
from flask_bootstrap import Bootstrap


from flask_marshmallow import Marshmallow
from flask_smorest import Api, Blueprint, abort




basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
ma = Marshmallow()


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
    def profesor_api_route():
        return {
            "name": "Adrien",
            "birthday": "02 January",
            "age": 85,
            "sex": None,
            "friends": ["Amadou", "Mariam"]
        }

    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///{os.path.join(basedir, 'data.sqlite')}"
    app.config['SQLALCHEMY_COMMIT_ON_TEARDOWN'] = True

    db.init_app(app)
    ma.init_app(app)

    from tasks.models import Task

    migrate = Migrate(app, db)

    # @app.route('/todoz')
    # def my_api_route():
    #     tasks = Task.query.all()
    #     return {"results": [{field: getattr(task, field) for field in Task.__table__.columns.keys()}for task in tasks]}

    @app.route('/todoz')
    def my_api_route():
        from tasks.serializers import TaskSchema
        tasks = Task.query.all()
        return {"results": TaskSchema(many=True).dump(tasks)}

    return app


