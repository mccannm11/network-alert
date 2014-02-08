import smtplib


class Mailer(object):

    def __init__(self, server, recipients, sender):
        self.server = server
        self.recipients = recipients
        self.sender = sender

    def send_warning_message(self, macs):
        if len(macs) is 0:
            return False

        message = self.build_message(macs)
        smtp = smtplib.SMTP(self.server)

        smtp.sendmail(self.sender, self.recipients, message)
        smtp.quit()
        return True

    def build_message(self, macs):
        message = ["\n MAC: %s Name: %s IP: %s" %
                   (m['mac'], m['name'], m['ip']) for m in macs]
        return "".join(message)
