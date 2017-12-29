import ConfigParser

config = ConfigParser.RawConfigParser()
config_file = "crawl_config.cfg"


def refresh_config():
    config.read(config_file)