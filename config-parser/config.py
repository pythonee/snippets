import os
import ConfigParser

is_existed = os.path.exists('config.ini')


config = ConfigParser.RawConfigParser()
config.read('config.ini')

node_config = {}

for sec in config.sections():
    node_config[sec] = dict(config.items(sec))

print node_config
