from instapy_cli import client
import requests
import os
from PIL import Image
import subprocess

def Reformat_Image(ImageFilePath):
    image = Image.open(ImageFilePath, 'r')
    image_size = image.size
    width = image_size[0]
    height = image_size[1]

    if(width != height):
        bigside = width if width > height else height

        background = Image.new('RGBA', (bigside, bigside), (255, 255, 255, 255))
        offset = (int(round(((bigside - width) / 2), 0)), int(round(((bigside - height) / 2),0)))

        background.paste(image, offset)
        background.save('out.png')

account = open('Account.txt','r')
username = account.readline().rstrip()
password = account.readline().rstrip()
account.close()
file = open('./img_urls.txt','r')
urls = file.readlines()
urls = [i[:-1] for i in urls]
urls = [i.split('^^') for i in urls]
file.close()

cli = client(username,password)

for i in urls:
    r = requests.get(i[0])
    f = open("image",'wb')
    f.write(r.content)
    viewer = subprocess.Popen(['eog','image'])
    print("URL - " + i[2])
    c = input("upload?[y/n]")
    if c=='n':
        viewer.terminate()
        viewer.kill()
        os.remove('image')
        f.close()
        continue
    Reformat_Image('image')
    cli.upload('out.png',"Post mirrored from Reddit\nCREDITS: "+i[1]+".\n.\n.\n.\n.\n.\n#memes #dankmemes #reddit #sadmemes #spicymemes #humor #funny #pewdiepie #fortnite #dailymemes #thanosmemes #minecraft #memereview #lwiay #pewnews #pewpew #memestgram #memedaily #memesfunny #epicmemes #normiememes #spicymeme #stolenmemes #dankmemesdaily #mememachine")
    viewer.terminate()
    viewer.kill()
    os.remove('image')
    os.remove('out.png')
    f.close()

os.remove('post_urls.txt')
os.remove('img_urls.txt')
