import smtplib


smtpObj = smtplib.SMTP('SMTP.office365.com', 587)
smtpObj.ehlo()
smtpObj.starttls()

smtpObj.login('salimmouloueletude@outlook.fr', 'Smoul25082015')
 
str_send_mail="""Subject: testin'...\n
izanus"""
#... This is a test '''
self.smtpObj.sendmail("salimmouloueletude@outlook.fr","salim.moulouel@gmail.com",str_send_mail) 
smtpObj.quit()

                


