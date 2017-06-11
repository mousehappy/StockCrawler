import tushare as ts
from sqlalchemy import create_engine, String

db_name = "stock_data"
engine = create_engine('mysql://root:cnp200@HW@127.0.0.1/?charset=utf8')
engine.execute("USE %s" % db_name)


def test_get_industry_classified():
    df = ts.get_industry_classified()
    df.to_sql("industry_classify", engine, if_exists='replace', index=False, dtype={"code": String(6)})


def test_get_concept_classified():
    df = ts.get_concept_classified()
    df.to_sql("concept_classify", engine, if_exists='replace', index=False, dtype={"code": String(6)})


def test_get_stock_basics():
    df = ts.get_stock_basics()
    #df.set_index(['code'], inplace=True)
    #row = df.at(2633)
    #a = df[2632:2633]['esp']
    #print a.get_vaule
    df.to_sql("stock_crawl_schedule", engine, if_exists='append', index=True, dtype={"code": String(6)})

test_get_stock_basics()