import pandas as pd
from PIL import Image,ImageDraw,ImageFont
df = pd.read_csv('list2.csv')
font=ImageFont.truetype('arial.ttf',70)
for index,j in df.iterrows():
    img=Image.open('certificatetemplate.png',)
    draw=ImageDraw.Draw(img)
    draw.text(xy=(890,700),text='{}'.format(j['Name']),fill=(0,0,0),font=font)
    img.save('generatedcertificates/{}.png'.format(j['Name']))
    img.close()