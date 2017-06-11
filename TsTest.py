# encoding=utf8
import tushare as ts
from sqlalchemy import create_engine, String

#a = tushare.get_k_data("002743")
# df = ts.get_k_data(code='601199', start='2017-05-01', end='2017-05-05')
# print df.size
# print df.to_dict('index ')
# print df
#
# df = ts.get_stock_basics()
# df_dict = df.to_dict('index')
# print len(df_dict.keys())
# df_keys = df_dict.keys()
# rec1 = df_dict[df_keys[0]]
# print rec1.get("industry")

db_name = "stock_data"
engine = create_engine('mysql://root:cnp200@HW@127.0.0.1/?charset=utf8')
#engine.execute("CREATE DATABASE IF NOT EXISTS %s" % db_name)
engine.execute("USE %s" % db_name)
#engine.execute('SET NAMES utf8;')
#engine.execute('SET CHARACTER SET utf8;')
#engine.execute('SET character_set_connection=utf8;')
#df = ts.get_concept_classified()
#df = ts.get_k_data(code='601199', start='2017-05-01', end='2017-05-05')
#df = ts.get_stock_basics()
#df = df.set_index('code')
#df.to_sql('stock_crawl_list', engine, if_exists='append', index=True, index_label='code', dtype={"code": Integer})
#print df.dtypes
#print df.ftypes

#df1 = df[['name', 'industry', 'area']]
#df1.to_sql('stock_crawl_list', engine, if_exists='append', index=True, index_label='code', dtype={"code": String(6)})

# 获取K线
#df = ts.get_k_data('600000', ktype='5', start='2017-05-12', end='2017-05-12')
df = ts.get_tick_data('600000', date='2017-05-12')
print df


#print df
