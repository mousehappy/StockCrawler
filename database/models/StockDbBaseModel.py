# -*- coding: UTF-8 -*-
# encoding: utf-8

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, BIGINT, Text, Date, DateTime, Float, DECIMAL
from sqlalchemy import PrimaryKeyConstraint

Base = declarative_base()


class CrawlManageSchedule(Base):
    __tablename__ = 'crawl_management'
    index = Column(Integer, primary_key=True, autoincrement=True)
    last_crawl_start_datetime = Column(DateTime)
    last_crawl_datetime = Column(DateTime)
    crawl_status = Column(String(10))

    def __repr__(self):
        return "CrawlManageSchedule, index: %s, last_crawl_data: %s, crawl_status： %s" % (
            self.index, self.last_crawl_datetime, self.crawl_status)


'''
code,代码
name,名称
industry,所属行业
area,地区
pe,市盈率
outstanding,流通股本(亿)
totals,总股本(亿)
totalAssets,总资产(万)
liquidAssets,流动资产
fixedAssets,固定资产
reserved,公积金
reservedPerShare,每股公积金
esp,每股收益
bvps,每股净资
pb,市净率
timeToMarket,上市日期
undp,未分利润
perundp, 每股未分配
rev,收入同比(%)
profit,利润同比(%)
gpr,毛利率(%)
npr,净利润率(%)
holders,股东人数
'''


class StockDataSchedule(Base):
    __tablename__ = 'stock_crawl_schedule'
    code = Column(String(6), primary_key=True, nullable=False)
    name = Column(String(8))
    industry = Column(Text)
    area = Column(Text)
    pe = Column(Float)
    outstanding = Column(Float)
    totals = Column(Float)
    totalAssets = Column(Float)
    liquidAssets = Column(Float)
    fixedAssets = Column(Float)
    reserved = Column(Float)
    reservedPerShare = Column(Float)
    esp = Column(Text)
    bvps = Column(Float)
    pb = Column(Float)
    timeToMarket = Column(Date)
    undp = Column(Float)
    perundp = Column(Float)
    rev = Column(Float)
    profit = Column(Float)
    gpr = Column(Float)
    npr = Column(Float)
    holders = Column(Integer)
    last_crawled_date = Column(Date, server_default='2017-01-01')
    crawler_pid = Column(Integer)
    crawl_start_time = Column(DateTime)
    last_analyzed_date = Column(Date, server_default='2017-01-01')
    analyze_pid = Column(Integer)
    analyze_start_time = Column(DateTime)


class StockConceptClassify(Base):
    __tablename__ = 'concept_classify'
    index = Column(Integer, primary_key=True, autoincrement=True)
    code = Column(String(6))
    name = Column(String(6))
    c_name = Column(String(10))

    def __repr__(self):
        return "code: %s, name: %s, concept: %s" % (self.code, self.name, self.c_name)

# class Stock15MinK(Base):
#    __tables = '15min_K_data'
