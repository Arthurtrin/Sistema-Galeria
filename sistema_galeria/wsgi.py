import os
import sys

# Caminho para a pasta do seu projeto
project_home = '/home/arthurtestesistemas/Sistema-Galeria'
if project_home not in sys.path:
    sys.path.append(project_home)

# Virtualenv (opcional, mas recomendado se estiver usando)
activate_this = '/home/arthurtestesistemas/.virtualenvs/venv/bin/activate_this.py'
with open(activate_this) as file_:
    exec(file_.read(), dict(__file__=activate_this))

# Define as configurações do Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'sistema_galeria.settings')

from django.core.wsgi import get_wsgi_application
application = get_wsgi_application()

