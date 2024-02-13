#! python3
# a program to check if all the links on a website are functional

import re
import bs4
import requests
import logging
import pprint
import sys
import time

logging.basicConfig(
    level=logging.DEBUG, format=" %(asctime)s -  %(levelname) s -  %(message)s"
)
logging.disable(logging.CRITICAL)

logging.debug("Start of program")

headers = headers = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64; rv:122.0) Gecko/20100101 Firefox/122.0"
}

starting_url = 'https://www.kliimaseade.ee'

url_regex = re.compile(r'(?<![@])(kliimaseade.ee).*')
url_regex_shortened = re.compile(f'^(?!.*\\b(?:.com|.ee|.eu|.org|mailto)\\b).*(?:(/.*/))')


def link_crawler(url):
    links_list = list()
    # tuples of parent/child url links
    links_list.append((url, url))
    external_links = list()
    visited_links = list()
    broken_links = list()

    while links_list:
        logging.debug(f'lenght of list is {len(links_list)}')
        for link in links_list:
            if link[1] in visited_links:
                #removing all references to already visited links in the main collection of links
                links_list = [value for value in links_list if value[1] != link[1]]
                logging.debug(f'already visited the link {link}, removing {link}')
                continue

            working_link = link[1]
            parent_link = link[0]
            links_list = [value for value in links_list if value[1] != link]
            visited_links.append(working_link)
            #logging.debug(f'visited links are {visited_links}')
            #request_object = requests.get(working_link, headers)
            # check if the download went OK
            try:
                request_object = requests.get(working_link, headers)
                request_object.raise_for_status()
            except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema) as schemaerr:
                print(f'Something went wrong with downloading: {schemaerr}')
                continue
            except requests.exceptions.HTTPError as err:
                print(f'Something went wrong with downloading: {err}')
                print(err.response.status_code)
                #print(err.response.text)
                print(parent_link, working_link)

                for i, x in enumerate(broken_links):
                    if working_link == x:
                        break
                else:
                    broken_links.append((parent_link, working_link))

            #create soup object and parse it with 'lxml'
            request_object.encoding = request_object.apparent_encoding
            soup_object = bs4.BeautifulSoup(request_object.content, 'lxml')

            all_href_links = soup_object.find_all("a", href=True)

            for i in all_href_links:
                new_link = i['href']
                if new_link in visited_links:
                    continue

                match_object = url_regex.search(new_link)
                match_object_shortened = url_regex_shortened.search(new_link)

                if match_object:
                    logging.debug(f'regex match found! {match_object.group(1)} {new_link}')
                    for i, x in enumerate(visited_links):
                        if new_link in x:
                            logging.debug(f'already have the link in visited_links {new_link}')
                            break
                    else:
                        logging.debug(f'found new link : {new_link}')
                        links_list.append((working_link, new_link))

                    for i, x in enumerate(links_list):
                        if new_link in x:
                            logging.debug(f'already have the link on links_list {new_link}')
                            break
                    else:
                        links_list.append((working_link, new_link))

                elif match_object_shortened:
                    elongated_url = starting_url + match_object_shortened.group()
                    #print(elongated_url)
                    #time.sleep(5)
                    for i, x in enumerate(visited_links):
                        if elongated_url in x:
                            logging.debug(f'already have the link in visited_links {new_link}')
                            break
                    else:
                        logging.debug(f'found new link : {new_link}')
                        links_list.append((working_link, elongated_url))

                    for i, x in enumerate(links_list):
                        if elongated_url in x:
                            logging.debug(f'already have the link on links_list {new_link}')
                            break
                    else:
                        links_list.append((working_link, elongated_url))

                elif match_object == None:
                    #logging.debug(f'found external link {new_link}')
                    for i, x in enumerate(external_links):
                        if new_link in x:
                            logging.debug(f'already seen this external link {new_link}')
                            break
                    else:
                        external_links.append((working_link, new_link))



    for link in external_links:
        # check if the link has already been listed in broken links:
        for i, x in enumerate(broken_links):
            if link[1] in x:
                logging.debug(f'{link[1]} already in broken_links!')
                break

         # check if the link has already been visited:
        for i, x in enumerate(visited_links):
            if link[1] in x:
                logging.debug(f'{link[1]} already in visited_links!')
                break
        else:
            continue

        try:
            request_object = requests.get(link[1], headers)
            request_object.raise_for_status()
        except (requests.exceptions.MissingSchema, requests.exceptions.InvalidSchema) as schemaerr:
            print(f'Something went wrong with downloading: {schemaerr}')
            """
            for i, x in enumerate(broken_links):
                if link[1] == x:
                    logging.debug(f'{link[1]} already in broken_links!')
                    break
            """
        except requests.exceptions.HTTPError as err:
            (f'Something went wrong with downloading: {err}')
            print(err.response.status_code)
            """
            for i, x in enumerate(broken_links):
                if link[1] == x:
                    logging.debug(f'{link[1]} already in broken_links!')
                    break
            else:
            """
            broken_links.append(link)
                #external_links = [value for value in external_links if value[1] != link[1]]

    #logging.debug('external links are:')
    #logging.debug(pprint.pprint(external_links))

    return broken_links






website_broken_links = link_crawler(starting_url)
pprint.pprint(website_broken_links)
