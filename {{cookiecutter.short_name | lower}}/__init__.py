from . import model
from . import routes
from . import views

MODELS = [
    model.Addon{{cookiecutter.short_name | capitalize}}UserSettings,
    model.Addon{{ cookiecutter.short_name | capitalize }}NodeSettings,
]
USER_SETTINGS_MODEL = model.Addon{{ cookiecutter.short_name | capitalize }}UserSettings
NODE_SETTINGS_MODEL = model.Addon{{ cookiecutter.short_name | capitalize }}NodeSettings

ROUTES = [routes.settings_routes]

SHORT_NAME = '{{cookiecutter.short_name | lower}}'
FULL_NAME = '{{cookiecutter.full_name}}'

OWNERS = ['node']  # can include any of ['user', 'node']

ADDED_TO = {
    'user': False,
    'node': False,
}

VIEWS = []  # page, widget
CONFIGS = ['node']  # any of ['user', 'node']

CATEGORIES = [{{cookiecutter.categories}}]

INCLUDE_JS = {
    'page': [],
    'files': []
}

INCLUDE_CSS = {
    'page': [],
    'files': []
}

HAS_HGRID_FILES = True  # set to True for storage addons that display in HGrid
#GET_HGRID_DATA = views.hgrid.{{cookiecutter.short_name}}_hgrid_data
MAX_FILE_SIZE = 10  # MB
