import datetime

from crawler.scheduler.DailyInitialCrawl import DailyInitialCrawl

# dailyCrawl =DailyInitialCrawl()
# print dailyCrawl.need_crawl()

now_time = datetime.datetime.now()

START_CRAWL_TIME = datetime.time(hour=20)

print START_CRAWL_TIME
print now_time
print now_time.time()