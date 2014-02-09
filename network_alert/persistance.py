class Persistance(object):
    DELIMITER = '\t'

    def __init__(self, file):
        self.file = file

    def save(self, device):
        if device not in self.all():
            with open(self.file, 'a+') as f:
                line = self.DELIMITER.join(
                    [device['mac'], device['ip'], device['name']]
                )
                f.write(line + '\n')

    def all_macs(self):
        return [d['mac'] for d in self.all()]


    def all(self):
        with open(self.file, 'a+') as f:
            parse = lambda line: dict(
                zip(['mac', 'ip', 'name'], line.split(self.DELIMITER))
            )

            devices = [parse(d) for d in f.read().strip().split('\n')]

        # ensure no empty entries
        devices = [d for d in devices if len(d['mac']) > 0]
        return devices

    def clear(self):
        open(self.file, 'w').close()
