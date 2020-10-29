import sys
from smtplib import SMTP
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def getNormalMessageBody(message):
    Full_Message = ""
    Full_Message = Full_Message + """\nMessage - \n""" + message
    # print(Full_Message)
    return Full_Message
# Send Email Function
def sendEmail(recipientEmail, Subject,message):
    #####################################
    username = 'arkapriya@geekypi.net'
    password = 'Arkapriya@geekypi'
    SMTPServer = 'mail.geekypi.net:26'
    fromaddr = 'arkapriya@geekypi.net'
    s = SMTP(SMTPServer)
    s.login(username, password)
    ###################################

    if (recipientEmail.strip() == ''   or Subject.strip() == '' or message.strip() == ''):
        Return_Message = 'Plese provide all the required parameters in the below exected format' + """
        sendEmail(recipientEmail,Subject,message]"""

    else:
        try:
            toaddr = recipientEmail.strip()
            msgRoot = MIMEMultipart('related')
            msgRoot['Subject'] = Subject
            msgRoot['From'] = fromaddr
            msgRoot['To'] = toaddr
            msgRoot.preamble = 'This is a multi-part message in MIME format.'
            msg = MIMEMultipart('alternative')
            msgRoot.attach(msg)

            alternativeplaindata = MIMEText(
                    getNormalMessageBody(message), 'plain')
            msg.attach(alternativeplaindata)

            # Sending email
            s.sendmail(fromaddr, toaddr.split(','), msgRoot.as_string())
            s.quit()
            Return_Message = 'Successfully sent email to recipient email address'

        except Exception as e:
            print(e)
            Return_Message = 'Some error occered duting sending the email. Check if attachment path is given correctly and recipient list is comma (,) separated'

    return Return_Message


if __name__ == '__main__':

    if len(sys.argv) != 4:
        Return_Message = 'Plese provide all the required parameters in the below exected format' + """
        sendEmail(recipientEmail,Subject,message]"""
        print(Return_Message)
    else:
        Return = sendEmail(recipientEmail=sys.argv[1], Subject=sys.argv[2], message=sys.argv[3])
        print(Return)