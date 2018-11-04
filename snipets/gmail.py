import smtplib
s=smtplib.SMTP('smtp.gmail.com',587)
send='chiragreddy272@gmail.com'
smtp.ehlo()
smtp.starttls()
s.login(send,"chirag1235711")
message =("""hey anish
this is a test email for my project.......:)""")
s.sendmail(send,"anishr890@gmail.com",message)
s.quit()
