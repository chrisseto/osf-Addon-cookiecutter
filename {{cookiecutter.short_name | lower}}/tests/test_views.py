# -*- coding: utf-8 -*-
from webtest_plus import TestApp
from nose.tools import *  # PEP8 asserts

from tests.base import DbTestCase, URLLookup
from tests.factories import AuthUserFactory


from .utils import app, {{cookiecutter.short_name | capitalize }}AddonTestCase

lookup = URLLookup(app)

class Test{{cookiecutter.short_name | capitalize}}Views(DbTestCase):

    def setUp(self):
        self.app = TestApp(app)
        self.user = AuthUserFactory()

    def test_example(self):
        # an example test
        url = lookup('api', '{{cookiecutter.short_name}}_some_view')
        res = self.app.get(url, auth=self.user.auth)
        assert_equal(res.status_code, 200)


