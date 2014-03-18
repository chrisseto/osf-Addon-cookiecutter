# -*- coding: utf-8 -*-
"""Routes for the {{cookiecutter.short_name}} addon.
"""

from framework.routing import Rule, json_renderer
from website.routes import OsfWebRenderer

from . import views


settings_routes = {
    'rules': [
        # Example:
        # Rule([
        #     '/project/<pid>/{{cookiecutter.short_name | lower }}',
        # ]),
        # 'get',
        # views.{{ cookiecutter.short_name | lower }}_get,
        # json_renderer
    ]
}
