import commands
import smtplib
import time
import syslog

def get_network_interfaces():
     network_info = commands.getoutput("/sbin/ifconfig")
     return network_info

def send_mail(subject,content):
     try:
          #configuring smtp
          smtp_user_name = "abc@live.com"
          smtp_password = "password"
          smtp_server = "smtp-mail.outlook.com"
          smtp_port = 587
          server = smtplib.SMTP(smtp_server,smtp_port)
          server.ehlo()
          server.starttls()
          server.login(smtp_user_name, smtp_password)
          
          #lets send the mail
          mail_from = "abc@live.com"
          mail_to = "cde@gmail.com"
          subject = subject
          headers = 'To:' + mail_to + '\n' + 'From: ' + mail_from + '\n' + 'Subject:'+ subject +'\n'
          msg = content
          mail_content = headers + msg
          server.sendmail(mail_from, mail_to, mail_content)
          server.close()
          message = "RPi IP mail sent"
          syslog.syslog(syslog.LOG_INFO, message)
     except Exception, e:
          print "Could not send raspberry PI ip, " + str(e)
          syslog.syslog(syslog.LOG_ERR, str(e))

     
def email_my_network_info(datetime):
     net_info = get_network_interfaces()
     subject = "RPi started@"+datetime
     send_mail(subject,net_info)

email_my_network_info(time.strftime("%c"))

