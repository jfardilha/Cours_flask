import pytest

from app import create_app
from flask import template_rendered


@pytest.fixture
def user_name():
    return "adrien"


@pytest.fixture
def app():
    app = create_app()
    return app


@pytest.fixture
def captured_templates(app):
    recorded = []

    def record(sender, template, context, **extra):
        recorded.append((template, context))

    template_rendered.connect(record, app)
    try:
        yield recorded
    finally:
        template_rendered.disconnect(record, app)
