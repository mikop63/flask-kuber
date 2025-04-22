import os

MYSQL_HOST = os.environ.get('MYSQL_HOST', 'localhost')
MYSQL_USER = os.environ.get('MYSQL_USER', 'flask_user')
MYSQL_PASSWORD = os.environ.get('MYSQL_PASSWORD', 'flask_password')
MYSQL_DB = os.environ.get('MYSQL_DB', 'flask_notes')
MYSQL_CURSORCLASS = 'DictCursor'
