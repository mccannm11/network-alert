import ConfigParser
import os
import sys

#@todo: fix path 
ROOT_PATH = os.path.dirname(os.path.realpath(__file__)) + '/..'

def main():
    from client import Client
    from scanner import Scanner
    from mailer import Mailer
    from data import Data

    if len(sys.argv) is not 2:
        print_help()
        exit()

    config = ConfigParser.RawConfigParser()
    config.read(ROOT_PATH + '/config.cfg')

    KNOWN_MACHINES_FILE = ROOT_PATH + '/' + config.get('config', 'known_machines_file')
    INTERFACE = config.get('config', 'interface')
    SMTP_SERVER = config.get('config', 'smtp_server')
    ALERTING_USER = config.get('config', 'alerting_user')
    USERS_TO_ALERT = config.get('config', 'users_to_alert').split(',')

    mailer = Mailer(SMTP_SERVER, USERS_TO_ALERT, ALERTING_USER)
    persistance = Data(KNOWN_MACHINES_FILE)
    scanner = Scanner(INTERFACE)

    client = Client(scanner, mailer, persistance)


    command = sys.argv[1]

    s = '\t'
    if command == "unknown":
        print client.unknown()

    elif command == "known":
        print client.known()

    elif command == "learn":
        print client.learn()

    elif command == "alert":
        print client.alert()

    elif command == "all":
        print client.all()

    else:
        '\t Error:' + command + 'is not a supported command, see help'
        print_help()

def print_help():
    print """
    Usage:
        unknown: Lists all unknown machines on the network.
        known: Lists all known machines on the network.
        learn: Marks all machines on the network as known.
        alert: Sends and email to users, if unknown machines are found.
    """


if __name__ =="__main__":
    main()

