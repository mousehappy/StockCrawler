import tushare as ts
from test_common import engine
from sqlalchemy import String, Date
import pandas as pd

def test_get_k_data():
    df = ts.get_k_data("000001", start='2017-06-11')
    df1 = df[['code', 'date', 'open', 'close']]
    print df
    return df
    #df.set_index(['code', 'date'], inplace=True)
    #df.to_sql("day_k_data", engine, if_exists='append', index=True,
    #          dtype={"code": String(6), "date": Date})
    #print df1

def test_get_h_data():
    df = ts.get_h_data("600926", start='2017-05-20', end='2017-05-30')
    print df

def test_get_hist_data():
    df = ts.get_hist_data("600926", start='2017-05-10', end='2017-05-30')
    df.reset_index(inplace=True)
    df['code'] = pd.Series("600926", index=df.index)
    #df.set_index(['code', 'date'], inplace=True)
    df.to_sql("day_hist_data", engine, if_exists='append', index=False, dtype={"code": String(6), "date": Date})
    print df

def test_get_today_all():
    df = ts.get_today_all()
    print df

def test_get_today_ticks():
    df = ts.get_today_ticks('601333')
    print df

def test_get_tick_data():
    df = ts.get_tick_data('600533', date='2017-05-25')
    print df[df.volume > 400]
    print df[df.volume > 400].head(10)

def test_get_sina_dd():
    df = ts.get_sina_dd('600533', date='2017-05-25')
    print df.head(10)

def test_profit_data():
    df = ts.profit_data(year=2016, top=100)
    print df

def test_forecast_data():
    df = ts.forecast_data(2017,1)
    print df

df = test_get_k_data()
print df.shape[0]