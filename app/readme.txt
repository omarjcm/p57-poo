Creación de un ambiente para la generación de la aplicación:


virtualenv --python=python3 venv
source venv/bin/activate

Me dirijo al directorio donde se encuentra la aplicación principal.



Para install la aplicación como tal:
pip install --editable .

Luego utilizar las respectivas líneas de comando.
which upsv
upsv --help
upsv clientes --help

tree -I '__pycache__|*.egg-info|venv'



