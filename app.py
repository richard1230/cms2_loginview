from flask import Flask
from apps.cms import bp as cms_bp
from apps.front import bp as front_bp
from apps.common import bp as common_bp
import config
from exts import db



def create_app():
    app = Flask(__name__)
    app.register_blueprint(cms_bp)
    app.register_blueprint(front_bp)
    app.register_blueprint(common_bp)
    app.config.from_object(config)

    db.init_app(app)

    return app



#
# @app.route('/')
# def hello_world():
#     return 'Hello World!'


if __name__ == '__main__':
    app= create_app()
    app.run()


"""

mysql> create databases zlbbs charset utf8;
ERROR 1064 (42000): You have an error in your SQL syntax; check the manual that corresponds to your MySQL server version for the right syntax to use near 'databases zlbbs charset utf8' at line 1
mysql> create database zlbbs charset utf8;
Query OK, 1 row affected (0.00 sec)

mysql> show databases;
+-----------------------+
| Database              |
+-----------------------+
| information_schema    |
| alembic_demo          |
| flask_alembic_demo    |
| flask_migrate_demo    |
| flask_restful_demo    |
| flask_script_demo     |
| flask_sqlalchemy_demo |
| icbc_demo             |
| mysql                 |
| performance_schema    |
| sys                   |
| zlbbs                 |
+-----------------------+
12 rows in set (0.00 sec)

mysql> use zlbbs
Reading table information for completion of table and column names
You can turn off this feature to get a quicker startup with -A

Database changed
mysql> show tables;
+-----------------+
| Tables_in_zlbbs |
+-----------------+
| alembic_version |
| cms_user        |
+-----------------+
2 rows in set (0.00 sec)


"""