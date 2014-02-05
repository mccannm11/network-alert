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
        alert = ""
        for m in macs:
            alert = alert + "\n MAC: " + m['mac'] + " Name: " + m['name']\
            + " IP: "+ m['ip']
        return alert
