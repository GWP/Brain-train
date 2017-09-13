import os
basedir = os.path.abspath(os.path.dirname(__file__))

WTF_CSRF_ENABLED = True
SECRET_KEY = 'unguessable-key'
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://masterblaster:triumphtr4@whetstone-mysql.cd76mudin3zw.us-west-2.rds.amazonaws.com:3306/whetstonedb'

#if os.environ.get('DATABASE_URL') is None:
#    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
#else:
#    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']
#    SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://whetstone-mysql:triumphtr4@whetstone-mysql.cd76mudin3zw.us-west-2.rds.amazonaws.com:3306
    

