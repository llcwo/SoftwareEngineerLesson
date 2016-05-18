from sqlalchemy import *
from migrate import *


from migrate.changeset import schema
pre_meta = MetaData()
post_meta = MetaData()
buyer = Table('buyer', post_meta,
    Column('buyerID', String(length=20), primary_key=True, nullable=False),
    Column('buyerPhoto', String(length=100)),
    Column('buyerName', String(length=50)),
    Column('buyerCount', String(length=20)),
)


def upgrade(migrate_engine):
    # Upgrade operations go here. Don't create your own engine; bind
    # migrate_engine to your metadata
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['buyer'].columns['buyerPhoto'].create()


def downgrade(migrate_engine):
    # Operations to reverse the above upgrade go here.
    pre_meta.bind = migrate_engine
    post_meta.bind = migrate_engine
    post_meta.tables['buyer'].columns['buyerPhoto'].drop()
