#! python3
# a program to download all xkcd comics

import requests
import bs4
import os

# load xkcd home page
xkcd_home_page = 'https://xkcd.com/'
headers = headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
}

os.makedirs('xkcd', exist_ok=True)
def downloader(url):
    # load the page in to a request object
    request_object = requests.get(url, headers)
    try:
        request_object.raise_for_status()
    except Exception as err:
        print(f'Something went wrong with downloading: {err}')
        return
    # get the comic image url
    soup_object = bs4.BeautifulSoup(request_object.text, 'lxml')
    image_link = soup_object.select('#comic > img:nth-child(1)')
    if not image_link:
        print('Could not find comic image on current page')
    else:
        comic_url = 'https:' + image_link[0].get('src')
        # save image to the folder xkcd
        image_file = open(os.path.join('xkcd', os.path.basename(comic_url)), 'wb')
        image_request_object = requests.get(comic_url)
        print(f'Downloading image {comic_url}')
        for chunk in image_request_object.iter_content(100000):
            image_file.write(chunk)
        image_file.close()

    # get the previous buttons url
    previous_comic_link = soup_object.select('a[rel="prev"]')

    if previous_comic_link == []:
        print('No more comics left!')
        return
    else:
        previous_comic_url = 'https://xkcd.com' + previous_comic_link[0].get('href')
        # recursively call the function with previous url as parameter
        downloader(previous_comic_url)


downloader(xkcd_home_page)

