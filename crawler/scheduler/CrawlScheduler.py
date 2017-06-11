import datetime


class CrawlScheduler(object):
    def __init__(self):
        self.task_queues = []

    def generate_crawl_task(self):
        pass

    def run_tasks(self):
        while True:
            now_time = datetime.time.now()

