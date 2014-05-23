# -*- coding: utf-8 -*-
"""Routes for the {{cookiecutter.short_name}} addon.
"""

from framework.routing import Rule, json_renderer
from website.routes import OsfWebRenderer

from . import views

# Routes that use the web renderer
web_routes = {
    'rules': [

        ##### View file #####
    #     Rule(
    #         [
    #             '/project/<pid>/{{cookiecutter.short_name}}/files/<path:path>',
    #             '/project/<pid>/node/<nid>/{{cookiecutter.short_name}}/files/<path:path>',
    #         ],
    #         'get',
    #         views.crud.{{cookiecutter.short_name}}_view_file,
    #         OsfWebRenderer('../addons/{{cookiecutter.short_name}}/templates/{{cookiecutter.short_name}}_view_file.mako'),
    #     ),


    #     ##### Download file #####
    #     Rule(
    #         [
    #             '/project/<pid>/{{cookiecutter.short_name}}/files/<path:path>/download/',
    #             '/project/<pid>/node/<nid>/{{cookiecutter.short_name}}/files/<path:path>/download/',
    #         ],
    #         'get',
    #         views.crud.{{cookiecutter.short_name}}_download,
    #         notemplate,
    #     ),
    ],
}

# JSON endpoints
api_routes = {
    'rules': [

        ##### Node settings #####

        Rule(
            ['/project/<pid>/{{cookiecutter.short_name}}/config/',
            '/project/<pid>/node/<nid>/{{cookiecutter.short_name}}/config/'],
            'get',
            views.{{cookiecutter.short_name}}_config_get,
            json_renderer
        ),

        Rule(
            ['/project/<pid>/{{cookiecutter.short_name}}/config/',
            '/project/<pid>/node/<nid>/{{cookiecutter.short_name}}/config/'],
            'put',
            views.{{cookiecutter.short_name}}_config_put,
            json_renderer
        ),

        Rule(
            ['/project/<pid>/{{cookiecutter.short_name}}/config/',
            '/project/<pid>/node/<nid>/{{cookiecutter.short_name}}/config/'],
            'delete',
            views.{{cookiecutter.short_name}}_deauthorize,
            json_renderer
        ),

        Rule(
            ['/project/<pid>/{{cookiecutter.short_name}}/config/import-auth/',
            '/project/<pid>/node/<nid>/{{cookiecutter.short_name}}/config/import-auth/'],
            'put',
            views.{{cookiecutter.short_name}}_import_user_auth,
            json_renderer
        ),
    ],

    ## Your routes here

    'prefix': '/api/v1'
}
