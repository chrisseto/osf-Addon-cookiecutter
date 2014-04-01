# -*- coding: utf-8 -*-
from framework.auth import get_current_user
from website.project.decorators import (must_be_valid_project,
    must_have_addon, must_have_permission, must_not_be_registration
)


# TODO
@must_be_valid_project
@must_have_addon('{{cookiecutter.short_name}}', 'node')
def {{cookiecutter.short_name}}_config_get(node_addon, **kwargs):
    """API that returns the serialized node settings."""
    user = get_current_user()
    return {
        'result': 'TODO',
    }, http.OK

@must_have_permission('write')
@must_not_be_registration
@must_have_addon('{{cookiecutter.short_name}}', 'node')
def {{cookiecutter.short_name}}_config_put(node_addon, auth, **kwargs):
    """View for changing a node's linked {{cookiecutter.short_name}} folder."""
    folder = request.json.get('selected')
    path = folder['path']
    node_addon.set_folder(path, auth=auth)
    node_addon.save()
    return {
        'result': {
            'folder': {
                'name': 'Dropbox' + path,
                'path': path
            },
            'urls': serialize_urls(node_addon)
        },
        'message': 'Successfully updated settings.',
    }, http.OK


@must_have_permission('write')
@must_have_addon('{{cookiecutter.short_name}}', 'node')
def {{cookiecutter.short_name}}_deauthorize(auth, node_addon, **kwargs):
    node_addon.deauthorize(auth=auth)
    node_addon.save()
    return None


@must_have_permission('write')
@must_have_addon('{{cookiecutter.short_name}}', 'node')
def {{cookiecutter.short_name}}_import_user_auth(auth, node_addon, **kwargs):
    """Import {{cookiecutter.short_name}} credentials from the currently logged-in user to a node.
    """
    user = auth.user
    user_addon = user.get_addon('{{cookiecutter.short_name}}')
    if user_addon is None or node_addon is None:
        raise HTTPError(http.BAD_REQUEST)
    node_addon.set_user_auth(user_addon)
    node_addon.save()
    return {
        'result': serialize_settings(node_addon, user),
        'message': 'Successfully imported access token from profile.',
    }, http.OK
