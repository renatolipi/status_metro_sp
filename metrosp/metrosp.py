#coding:utf-8

import sys
import httplib2
from bs4 import BeautifulSoup as BS

URL_METRO = 'http://www.metro.sp.gov.br/' +\
            'Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx'


class MetroSP():

    def __init__(self):
        self.url_metro = 'http://www.metro.sp.gov.br/' +\
                    'Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx'

    def get_response_and_content(self):
        h = httplib2.Http(".cache")
        headers = {'cache-control': 'max-age=%s' % (3600 * 24 * 365)}
        resp, content = h.request(self.url_metro, "GET", headers=headers)
        return resp, content

    def clean_string(self, value):
        new_value = value.replace('\n', '').replace('\r', '')
        return ' '.join(new_value.split())

    def set_item_on_dict(self, spans, info):
        if len(spans) != 2:
            raise 'Something went wrong. Check data structure.'
        if spans[1].find('a'):
            spans1 = self.clean_string(spans[1].a.string).encode('utf-8')
        else:
            spans1 = self.clean_string(spans[1].string).encode('utf-8')

        info[spans[0].string] = spans1
        return info

    def get_info_from_items(self, items):
        info = {}
        for item in items:
            spans = item.find_all('span')
            self.set_item_on_dict(spans, info)
        return info

    def get_metro_status(self):
        resp, content = self.get_response_and_content()
        if resp['status'] != '200':
            raise 'status: {}. Aborting...'.format(resp['status'])
        html = BS(content)
        items = html.find_all('li')
        info = self.get_info_from_items(items)
        return info
