from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database.models.StockDbBaseModel import *

db_name = 'stock_data'
db_uri = 'mysql://root:cnp200@HW@127.0.0.1/?charset=utf8'
db_username = None
db_password = None


class DBManager(object):
    DB_engine = None
    DB_session = None

    @classmethod
    def init_db(cls):
        if not cls.DB_engine:
            cls.DB_engine = create_engine(db_uri)
            cls.DB_engine.execute("USE %s" % db_name)
            Base.metadata.create_all(cls.DB_engine)
            cls.DB_session = sessionmaker(bind=cls.DB_engine)

    @classmethod
    def get_session(cls):
        if not cls.DB_engine:
            cls.init_db()
        return cls.DB_session()
