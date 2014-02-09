import smtplib


class Mailer(object):

    def __init__(self, server, recipients, sender):
        self.server = server
        self.recipients = recipients
        self.sender = sender

    def send_warning_message(self, devices):
        if len(devices) is 0:
            return False

        message = self.build_message(devices)
        smtp = smtplib.SMTP(self.server)

        smtp.sendmail(self.sender, self.recipients, message)
        smtp.quit()
        return True

    def build_message(self, devices):
        message = ["\n MAC: %s Name: %s IP: %s" %
                   (d['mac'], d['name'], d['ip']) for d in devices]
        return "".join(message)
