#coding:utf-8

import requests
from bs4 import BeautifulSoup as BS


class MetroSP():

    def __init__(self):
        self.url_metro = 'http://www.metro.sp.gov.br/' +\
            'Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx'

    def _get_response_and_content(self):
        response = requests.get(self.url_metro)
        content = response.content
        status_code = response.status_code
        return status_code, content

    def _clean_string(self, value):
        new_value = value.replace('\n', '').replace('\r', '')
        return ' '.join(new_value.split())

    def _set_item_on_dict(self, spans, info):
        if len(spans) != 2:
            raise 'Something went wrong. Check data structure.'
        if spans[1].find('a'):
            spans1 = self._clean_string(spans[1].a.string).encode('utf-8')
        else:
            spans1 = self._clean_string(spans[1].string).encode('utf-8')

        info[spans[0].string] = spans1
        return info

    def _get_info_from_items(self, items):
        info = {}
        for item in items:
            spans = item.find_all('span')
            self._set_item_on_dict(spans, info)
        return info

    def get_metro_status(self):
        status_code, content = self._get_response_and_content()
        if status_code != 200:
            raise 'status: {}. Aborting...'.format(status_code)
        html = BS(content, "html.parser")
        items = html.find_all('li')
        info = self._get_info_from_items(items)
        return info
