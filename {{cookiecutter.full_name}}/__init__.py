from . import model
from . import routes
from . import views

MODELS = [model.Addon{{cookiecutter.short_name}}NodeSettings]  # model.Addon{{cookiecutter.short_name}}UserSettings
#USER_SETTINGS_MODEL = model.AddonS3UserSettings
NODE_SETTINGS_MODEL = model.AddonS3NodeSettings

ROUTES = [routes.settings_routes]

SHORT_NAME = '{{cookiecutter.short_name}}'
FULL_NAME = '{{cookiecutter.full_name}}'

OWNERS = ['node']  # user

ADDED_TO = {
    'user': False,
    'node': False,
}

VIEWS = []  # page, widget
CONFIGS = ['node']  # User

CATEGORIES = ['{{cookiecutter.categories}}']

INCLUDE_JS = {
    'widget': [],
    'page': [],
    'files': []
}

INCLUDE_CSS = {
    'widget': [],
    'page': [],
}

HAS_HGRID_FILES = False
#GET_HGRID_DATA = views.hgrid.{{cookiecutter.short_name}}_hgrid_data
MAX_FILE_SIZE = 10  # MB
