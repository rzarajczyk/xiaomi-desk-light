from apscheduler.schedulers.blocking import BlockingScheduler
from homie_helpers import MqttSettings

from XiaomiDeskLight import XiaomiDeskLight
from bootstrap.bootstrap import start_service

config, logger, timezone = start_service()

scheduler = BlockingScheduler(timezone=timezone)

device = XiaomiDeskLight(config=config['xiaomi-desk-light'], mqtt_settings=MqttSettings.from_dict(config['mqtt']))

scheduler.add_job(device.refresh, 'interval', seconds=config['fetch-interval-seconds'])

scheduler.start()
