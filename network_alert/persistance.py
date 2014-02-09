import os


class Persistance(object):
    DELIMITER = '\t'

    def __init__(self, filename):
        self.filename = os.path.expanduser('~/' + filename)

    def save(self, device):
        if device not in self.all():
            with open(self.filename, 'a+') as f:
                line = self.DELIMITER.join(
                    [device['mac'], device['ip'], device['name']]
                )
                f.write(line + '\n')

    def all(self):
        with open(self.filename, 'a+') as f:
            devices = [d.split('\t')[0] for d in f.read().strip().split('\n')]

        # ensure no empty entries
        devices = [d for d in devices if len(d) > 0]
        return devices

    def clear(self):
        open(self.filename, 'w').close()
