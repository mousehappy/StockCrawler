from sqlalchemy import create_engine, String

db_name = "stock_data"
engine = create_engine('mysql://root:cnp200@HW@127.0.0.1/?charset=utf8')
#engine.execute("CREATE DATABASE IF NOT EXISTS %s" % db_name)
engine.execute("USE %s" % db_name)