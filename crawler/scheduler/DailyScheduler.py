from database.db_manage.DBManager import DBManager


class DailyScheduler(DBManager):
    pm_crawl_hour = (18, 24)
    am_crawl_hour = (0, 8)

    def read_conf(self):
        pass