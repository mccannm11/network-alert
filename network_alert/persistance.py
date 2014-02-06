class Persistance(object):

    def __init__(self, filename):
        self.filename = filename

    def save(self, mac):
        if mac not in self.all():
            with open(self.filename, 'a+') as f:
                f.write(mac + '\n')

    def all(self):
        with open(self.filename, 'a+') as f:
            devices = f.read().strip().split('\n')

        # ensure no empty entries
        devices = [d for d in devices if len(d) > 0]
        return devices

    def clear(self):
        with open(self.filename, 'w') as f:
            pass