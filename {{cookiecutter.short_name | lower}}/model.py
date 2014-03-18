# -*- coding: utf-8 -*-
"""Persistence layer for the {{ cookiecutter.short_name }} addon.
"""

from website.addons.base import AddonUserSettingsBase, AddonNodeSettingsBase


class Addon{{ cookiecutter.short_name | capitalize }}UserSettings(AddonUserSettingsBase):
    pass
    # TODO


class Addon{{ cookiecutter.short_name | capitalize }}NodeSettings(AddonNodeSettingsBase):
    pass
    # TODO


