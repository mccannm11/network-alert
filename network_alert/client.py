class Client(object):
    def __init__(self, scanner, mailer, persistance):
        self.scanner = scanner.scan()
        self.mailer = mailer
        self.persistance = persistance

    # lists unknown devices on the network
    def unknown(self):
        return [m for m in self.all() if m['mac'] not in self.known()]

    # lists known devices on the network
    def known(self):
        return self.persistance.all()

    ## returns an array of all devices currently connected
    def all(self):
        return self.scanner.devices

    # scans the network for all devices and adds them
    # the the list of known devices
    def learn(self):
        for m in self.scanner.devices:
            self.persistance.save(m['mac'])

    # sends an email to users if an unknown device is found on the network, also adds devices as known
    def alert(self):
        self.mailer.send_warning_message(self.scanner.devices)
        self.learn()
