import os
MYSQL_HOST = os.getenv('MYSQL_HOST', 'mysql.flask-notes-app.svc.cluster.local')
MYSQL_USER = os.getenv('MYSQL_USER', 'flask_user')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', 'flask_password')
MYSQL_DB = os.getenv('MYSQL_DB',   'flask_notes')
MYSQL_CURSORCLASS = 'DictCursor'
