from pyramid.view import view_config


@view_config(route_name='home', renderer='templates/home.pt')
def view_home(request):
    return {'project': 'paulla.ldapmanager'}

@view_config(route_name='add', renderer='templates/add.pt')
def view_add(request):
    return {'project': 'paulla.ldapmanager'}
