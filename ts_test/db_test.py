from database.db_manage.DBManager import DBManager
from database.models.StockDbBaseModel import *

db_uri = 'mysql://root:cnp200@HW@127.0.0.1/?charset=utf8'
db_manager = DBManager(db_uri)

session = db_manager.get_session()
concept_classifies = session.query(StockConceptClassify).all()
for classify in concept_classifies:
    print classify