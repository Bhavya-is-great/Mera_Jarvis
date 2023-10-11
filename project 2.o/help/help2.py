import requests
from bs4 import BeautifulSoup
import os

def download_images_by_xpath(url, xpath_expression, save_path='C:\\Users\\bhavy\\OneDrive\\Desktop'):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, 'html.parser')
  images = soup.find_all(xpath=xpath_expression)

  for image in images:
    src = image['src']
    filename = src.split('/')[-1]

    # Create the directory if it doesn't exist
    os.makedirs(save_path, exist_ok=True)

    # Download the image
    response = requests.get(src)
    with open(os.path.join(save_path, filename), 'wb') as f:
      f.write(response.content)


if __name__ == '__main__':
  url = 'https://www.google.com/images/'
  xpath_expression = '//img[@class="rg_ic rg_i"]'
  save_path = 'C:\\Users\\bhavy\\OneDrive\\Desktop'
  download_images_by_xpath(url, xpath_expression, save_path)
