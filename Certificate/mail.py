from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from PIL import Image, ImageDraw, ImageFont
import pandas as pd
import os
import smtplib

df = pd.read_csv('list2.csv')
font = ImageFont.truetype('arial.ttf', 60)


smtp_server = 'smtp.gmail.com'  
smtp_port = 587
smtp_username = 'abc624951@gmail.com'
app_password = 'mnkempprfflswedi'

for index, j in df.iterrows():
    img = Image.open('certificatetemplate.png')
    draw = ImageDraw.Draw(img)
    draw.text(xy=(890,700), text='{}'.format(j['Name']), fill=(0, 0, 0), font=font)
    
    
    certificate_filename = 'generatedcertificates/{}.png'.format(j['Name'])
    img.save(certificate_filename)
    img.close()

    msg = MIMEMultipart()
    msg['From'] = smtp_username
    msg['To'] = j['Email']  
    msg['Subject'] = 'Certificate'
    
    body = "Dear {},\n\nPlease find attached your certificate.\n\nBest regards,\nTeam SARK".format(j['Name'])
    msg.attach(MIMEText(body, 'plain'))
    
    img_data = open(certificate_filename, 'rb').read()
    image = MIMEImage(img_data, name=os.path.basename(certificate_filename))
    msg.attach(image)
    
    try:  
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, app_password)
        server.sendmail(smtp_username, j['Email'], msg.as_string())
        print("Email sent to:", j['Email'])
    except Exception as e:
        print("Error sending email to", j['Email'], ":", str(e))
    finally:
        server.quit()
