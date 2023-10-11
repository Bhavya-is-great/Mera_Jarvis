import requests
from time import sleep
import os

# prompttoimg = input("Enter the prompt to generate image:")


def textimage(prompttoimg):
    r = requests.post('https://clipdrop-api.co/text-to-image/v1',
  files = {
      'prompt': (None, prompttoimg, '4k resolution/plain')
  },
  headers = { 'x-api-key': "Clipdrop_Api"}
)
    if (r.ok):
      # r.content contains the bytes of the returned image
    #   print(r.content)
        filename = "C:\\Users\\bhavy\\OneDrive\\Desktop\\project 2.o\\Generated images\\" + prompttoimg + ".jpg"
        with open(filename,'wb') as f:
           f.write(r.content)

        sleep(2)

        os.startfile(filename)

        return True

    else:
      r.raise_for_status()

# texttoimage()