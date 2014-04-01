# -*- coding: utf-8 -*-
from webtest_plus import TestApp

from tests.base import DbTestCase, URLLookup


from .utils import app, {{cookiecutter.short_name | capitalize }}AddonTestCase


class Test{{cookiecutter.short_name | capitalize}}Views(DbTestCase):

    def setUp(self):
        self.app = TestApp(app)
