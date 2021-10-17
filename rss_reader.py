import argparse
import requests
from bs4 import BeautifulSoup
import logging
import json
import textwrap

parser = argparse.ArgumentParser()
parser.add_argument("source", nargs="?", help="RSS URL", default=None)
parser.add_argument("--version", help="Version info", action="store_true")
parser.add_argument("--json", help="Print result as JSON in stdout", action="store_true")
parser.add_argument("--verbose", help="Outputs verbose status messages", action="store_false")
parser.add_argument("--limit", help="Limit news topics if this parametr provided", default=None, type=int)
parser.add_argument("-a", "--action", help="Fetch your RSSfeed", default="parserss")
args = parser.parse_args()
logging.getLogger().disabled = args.verbose
logging.basicConfig(format='%(levelname)s - %(asctime)s : %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO)
logging.info(f"Arguments have been added: {args}")


def check_connection(func):

    def wrapper(source):
        try:
            response = requests.get(source)
            if response.status_code == 200:
                logging.info(f"Responce was succesfully recieved. Status code - {response.status_code}")
                func(response)
            else:
                logging.warning(f"Source is not responsible. Status code - {response.status_code}")
        except:
            return f"can't reach source"
            logging.warning("Failured to connect")
    return wrapper


@check_connection
def parserss(source):
    new_json = {}
    list_values = []
    soup = BeautifulSoup(source.content, "xml")
    channel = soup.find("channel")
    feed = channel.title.text
    items = soup.find_all("item")
    cntr_number_news = 0
    for item in items:
        if args.limit is None or cntr_number_news < args.limit:
            title = item.title.string
            link = item.link.text
            date = item.pubDate.text
            try:
                description = item.description.text
            except:
                description = title
                logging.info(f"Numbers of news: Description doesn't exist")
            cntr_number_news += 1
            if args.json is False:
                descr = "\n".join(textwrap.wrap(description, 100))
                print(f"Feed: {feed}\nTitle: {title}\nDate: {date}\nLink:"
                      f" {link}\nDescription:\n{descr}\n -----------------------------------"
                      f"---------------------------------------------------------------\n")
            else:
                item_dict = {}
                item_dict['title'] = title
                item_dict['link'] = link
                item_dict['date'] = date
                item_dict['description'] = description
                list_values.append(item_dict)

    if args.json is True:
        new_json["feed"] = feed
        new_json["items"] = list_values
        to_json = json.dumps(new_json, indent=2, ensure_ascii=False)
        print(to_json)

def show_version():

    print("Current parser's version 0.00001")


if args.version is True:
    show_version()
    logging.info('Info about version')

if args.source is not None:
    parserss(args.source)
    logging.info(f"Max numbers of news: {args.limit}")







