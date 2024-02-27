#! python3
# a program to download all xkcd comics
import time
import requests
import bs4
import os
import threading

# load xkcd home page
xkcd_home_page = 'https://xkcd.com/'
headers = headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:80.0) Gecko/20100101 Firefox/80.0"
}
#create a folder to save downloaded files to
os.makedirs('xkcd', exist_ok=True)

def downloader(start_comic, end_comic):
    for url_number in range(start_comic, end_comic):
        # download the page
        print(f'Downloading the page {xkcd_home_page + str(url_number)}')
        request_object = requests.get(f'{xkcd_home_page + str(url_number)}', headers)
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

start_time = time.time()
# Create and start the Thread objects (2897 total)
download_threads = list() # a list of all thread objects
for i in range(0, 2900, 100): # loops 29 times, creates 29 threads
    start = i
    end = i + 99
    if start == 0:
        start = 1 #there is no comic 0, set start to 1 "https://xkcd.com/1/"

    download_thread = threading.Thread(target=downloader, args=(start, end))
    download_threads.append(download_thread)
    download_thread.start()

# Wait for all the threads to end
# use the .join method on the list of threads, if the thread is not finished
# it will force the main thread to wait until the sub thread finishes
for download_thread in download_threads:
    download_thread.join()

print('Done downloading')

end_time = time.time()
print(f'Multithreaded - done downloading the comics in {end_time - start_time} seconds')