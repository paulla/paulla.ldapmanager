import ldap
import os

from ConfigParser import SafeConfigParser

filename = "config.ini"

if not os.path.isfile(filename):
        raise Exception("%s is not a file" % filename)
config = SafeConfigParser()
config.read(filename)
config_dict = dict(config.items('ldap'))
#print config_dict('uri')



def connect():
    import ldap    
    l = ldap.initialize(config_dict('uri'))
        
    method = ldap.AUTH_SIMPLE
    l.bind(config_dict('rootdn'), config_dict('password'), config_dict('method'))
    return l



def find_entries(search_base, search_filter):
    l = connect()

    search_scope = ldap.SCOPE_SUBTREE

    try:
        return l.search_s(search_base, search_scope, search_filter)
    except ldap.LDAPError, e:
	    print e



# vim:set et sts=4 ts=4 tw=80:
