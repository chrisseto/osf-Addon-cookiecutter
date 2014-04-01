# -*- coding: utf-8 -*-
from website.addons.base.testing import AddonTestCase

from webtest_plus import TestApp

import website


app = website.app.init_app(
    routes=True, set_backends=False, settings_module='website.settings'
)

class {{cookiecutter.short_name | capitalize }}AddonTestCase(AddonTestCase):

    ADDON_SHORT_NAME = {{cookiecutter.short_name}}

    def create_app(self):
        return TestApp(app)

    def set_user_settings(self, settings):
        # Any user settings model setup here
        # ...

    def set_node_settings(self, settings):
        # Any node settings model setup here
        # ...
