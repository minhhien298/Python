import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

fromaddr = "hienlhm@saomaisoft.com"
toaddr = "minhhien90@gmail.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "TIÊU ĐỀ CỦA MAIL (SUBJECT)"
body = "NỘI DUNG MAIL"
try:
    msg.attach(MIMEText(body, 'plain'))
    filename = './input/melbourne-housing-snapshot/melb_data.csv'
    attachment = open(filename, "rb")
    part = MIMEBase('application', 'octet-stream')
    part.set_payload((attachment).read())
    encoders.encode_base64(part)
    part.add_header('Content-Disposition', "attachment; filename= %s" % filename)
    msg.attach(part)
    server = smtplib.SMTP('smtp.dreamhost.com', 587)
    server.starttls()
    server.login(fromaddr, "epN*TCwd")
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)
    server.quit()
except Exception as e:
 print(str(e))
