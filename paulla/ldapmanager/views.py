from pyramid.view import view_config
import utils

@view_config(route_name='home', renderer='templates/home.pt')
def view_home(request):
    result = utils.find_entries("ou=users,","(uid=*)")   
    return {'project': 'paulla.ldapmanager' , 'users' : result }

@view_config(route_name='add', renderer='templates/add.pt')
def view_add(request):
    return {'project': 'paulla.ldapmanager'}
    

# vim:set et sts=4 ts=4 tw=80:
