#coding:utf-8

import sys
import httplib2
from bs4 import BeautifulSoup as BS

URL_METRO = 'http://www.metro.sp.gov.br/' +\
            'Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx'


def get_response_and_content():
    h = httplib2.Http(".cache")
    headers = {'cache-control': 'max-age=%s' % (3600 * 24 * 365)}
    resp, content = h.request(URL_METRO, "GET", headers=headers)
    return resp, content


def clean_string(value):
    new_value = value.replace('\n', '').replace('\r', '')
    return ' '.join(new_value.split())


def set_item_on_dict(spans, info):
    if len(spans) != 2:
        print 'Something went wrong. Check data structure.'
        sys.exit()
    if spans[1].find('a'):
        spans1 = clean_string(spans[1].a.string).encode('utf-8')
    else:
        spans1 = clean_string(spans[1].string).encode('utf-8')

    info[spans[0].string] = spans1
    return info


def get_info_from_items(items):
    info = {}
    for item in items:
        spans = item.find_all('span')
        set_item_on_dict(spans, info)
    return info


def get_metro_status():
    resp, content = get_response_and_content()
    if resp['status'] != '200':
        print 'status: {}. Aborting...'.format(resp['status'])
        sys.exit()
    html = BS(content)
    items = html.find_all('li')
    info = get_info_from_items(items)
    return info


if __name__ == '__main__':
    metro_status = get_metro_status()
    print '\n\n metro_status = {} \n\n'.format(metro_status)
