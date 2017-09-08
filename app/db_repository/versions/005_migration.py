from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
problem = Table('problem', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('question', String(length=140)),
    Column('answer', String(length=140)),
    Column('problem_type', String(length=64)),
    Column('timestamp', DateTime),
    Column('time_to_complete', String(length=120)),
    Column('user_id', Integer),
)

user = Table('user', post_meta,
    Column('id', Integer, primary_key=True, nullable=False),
    Column('date_created', DateTime),
    Column('date_modified', DateTime),
    Column('nickname', String(length=64)),
    Column('password', String(length=64)),
    Column('email', String(length=120)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['problem'].create()
    post_meta.tables['user'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['problem'].drop()
    post_meta.tables['user'].drop()
