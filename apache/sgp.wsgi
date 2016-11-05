import sys
import site

# Add the site-packages of the chosen virtualenv to work with
site.addsitedir('/home/inventsis/apps_wsgi/vinvent/lib/python2.7/site-packages')

# Activate the virtual env
activate_env=os.path.expanduser("/home/inventsis/apps_wsgi/vinvent/bin/activate_this.py")
execfile(activate_env, dict(__file__=activate_env))

# Calculates the path based on location of WSGI script.
apache_configuration = os.path.realpath(os.path.dirname(__file__))

project = os.path.join(apache_configuration, 'vinvent/sgp')

sys.path.append(apache_configuration)
sys.path.append(project)
sys.path.append("/home/inventsis/apps_wsgi/vinvent/lib/python2.7/")
os.environ['DJANGO_SETTINGS_MODULE'] = 'sgp.settings'
from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()
