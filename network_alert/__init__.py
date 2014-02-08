from network_alert.scanner import Scanner
from network_alert.persistance import Persistance
from network_alert.mailer import Mailer
from network_alert.version import VERSION, VERSION_STRING

__all__ = [
    'Scanner', 'Persistance', 'Mailer', 'VERSION', 'VERSION_STRING'
]

#@TODO Load this configuration from an external file
KNOWN_MACHINES_FILE = '~/.nalert_known_machines'
INTERFACE = 'wlan0'
SMTP_SERVER = 'localhost'
ALERTING_USER = 'network-alert@michael.mccanns.org'
USERS_TO_ALERT = 'michael@mccanns.org'
