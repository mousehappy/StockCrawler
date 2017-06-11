import datetime
import tushare as ts

from common.constants import *
from database.db_manage.DBManager import DBManager, CrawlManageSchedule

START_CRAWL_TIME = datetime.time(hour=20)


class DailyInitialCrawl(DBManager):
    def need_crawl(self):
        session = DailyInitialCrawl.get_session()
        # now time is early than START_CRAWL_TIME, do not start crawl
        now_time = datetime.datetime.now()
        if now_time.time() < START_CRAWL_TIME:
            return False
        # Read last_crawl_time from DB, and judge if need to start crawl
        lastRec = session.query(CrawlManageSchedule).one_or_none()
        new_daily_crawl = False
        if lastRec:
            last_crawl_datetime = lastRec.last_crawl_datetime
            if not last_crawl_datetime:
                new_daily_crawl = True
            elif last_crawl_datetime.date() < now_time.date():
                new_daily_crawl = True
            elif last_crawl_datetime.date() == now_time.date() and last_crawl_datetime.time() < START_CRAWL_TIME:
                new_daily_crawl = True
        else:
            new_daily_crawl = True
            lastRec = CrawlManageSchedule()
            lastRec.index = 1
            session.add(lastRec)
        if not new_daily_crawl:
            return new_daily_crawl
        today_date = now_time.date().isoformat()
        is_trade_day = self.test_trade_day(today_date)
        # Update last_crawl record
        if not is_trade_day:
            lastRec.last_crawl_start_datetime = now_time
            lastRec.last_crawl_datetime = now_time
            lastRec.crawl_status = CRAWL_STATUS_SUCCESS
        else:
            lastRec.last_crawl_start_datetime = now_time
            lastRec.crawl_status = CRAWL_STATUS_CRAWLING
        session.commit()
        return is_trade_day

    @staticmethod
    def test_trade_day(today_date):
        # Crawl today's SSE (Shanghai Stock Exchange) Composite Index;
        df = ts.get_k_data("000001", start=today_date)
        row_count = df.shape[0]
        return True if row_count == 1 else False


