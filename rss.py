from cgi import print_form
import logging
import sys
import calendar
import xmltodict, json
import argparse
import xml.etree.ElementTree as ET
import requests

app_version = 1.1
#positional arg
parser = argparse.ArgumentParser(description='Your RSS Reader')
#optional args
parser.add_argument('URL', metavar='source', 
                     help='RSS URL')
parser.add_argument('--json', action='store_true', help="Print result as JSON in stdout")
parser.add_argument('--version', action='store_true', help="Print version info")
parser.add_argument('--verbose', action='store_true', help="Outputs verbose status messages")
parser.add_argument('--limit', type=int, required=False, help="Limit news topics if this parameter provided")

args = parser.parse_args()
#print version
if args.version:
    #print(sys.version)
    print(app_version)

url_test = requests.get(args.URL).text
# print(url_test)

tree = ET.fromstring(url_test)
# print(tree[0])

#print feed and limited titles
n=0
for x in tree[0]:
    if x.tag == 'title':
            print()
            print('Feed: ', x.text)
            print()
    if x.tag == 'item':
        if args.limit != None and args.limit > n:
            title = x.find('title')
            print('Title: ', title.text)
            date = x.find('pubDate')
            print('Date: ', date.text)
            link = x.find('link')
            print(link.text)
            print()
            n+=1
        elif args.limit == None:
            title = x.find('title')
            print('Title: ', title.text)
            date = x.find('pubDate')
            print('Date: ', date.text)
            link = x.find('link')
            print(link.text)
            print()





