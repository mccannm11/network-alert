#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import sys
from ConfigParser import RawConfigParser
from network_alert import Scanner, Mailer, Persistance, KNOWN_MACHINES_FILE
from network_alert import INTERFACE, SMTP_SERVER, ALERTING_USER, USERS_TO_ALERT


class NetworkAlert(object):

    def __init__(self):
        self.scanner = Scanner(INTERFACE)
        self.mailer = Mailer(SMTP_SERVER, USERS_TO_ALERT, ALERTING_USER)
        self.persistance = Persistance(KNOWN_MACHINES_FILE)

    def run(self, args):
        if len(args) > 1:
            self.print_help()
            return
        else:
            self.scanner.scan()
            print getattr(self, args[0])()

    # lists unknown devices on the network
    def unknown(self):
        return [m for m in self.all() if m['mac'] not in self.known()]

    # lists known devices on the network
    def known(self):
        return self.persistance.all()

    # returns an array of all devices currently connected
    def all(self):
        return self.scanner.devices

    # scans the network for all devices and adds them
    # the the list of known devices
    def learn(self):
        for m in self.scanner.devices:
            self.persistance.save(m['mac'])

    # sends an email to users if an unknown device is found on the network,
    # also adds devices as known
    def alert(self):
        self.mailer.send_warning_message(self.scanner.devices)
        self.learn()

    def reset(self):
        self.persistance.clear()

    def print_help():
        print """
        Usage:
            unknown: Lists all unknown machines on the network.
            known: Lists all known machines on the network.
            learn: Marks all machines on the network as known.
            alert: Sends and email to users, if unknown machines are found.
        """


def main():
    NetworkAlert().run(sys.argv[1:])

if __name__ == '__main__':
    main()
