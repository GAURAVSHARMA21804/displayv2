from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

#Initializing database
db = SQLAlchemy()

migrate = Migrate()