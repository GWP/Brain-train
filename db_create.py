#!virtual/bin/python3.6

from migrate.versioning import api
#from config import SQLALCHEMY_DATABASE_URI
#from config import SQLALCHEMY_MIGRATE_REPO
from app import db
import os.path

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://masterblaster:triumphtr4@whetstone-mysql.cd76mudin3zw.us-west-2.rds.amazonaws.com:3306/whetstonedb'
#SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
db.create_all()

#if not os.path.exists(SQLALCHEMY_MIGRATE_REPO):
#    api.create(SQLALCHEMY_MIGRATE_REPO, 'database repository')
#    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO)
#else:
#    api.version_control(SQLALCHEMY_DATABASE_URI, SQLALCHEMY_MIGRATE_REPO, api.version(SQLALCHEMY_MIGRATE_REPO))
