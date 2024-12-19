# coding:utf-8

from bs4 import BeautifulSoup as BS
import requests


class MetroSP():

    def __init__(self):
        self.url_metro = "https://www.metro.sp.gov.br/direto-do-metro"

    def _get_response_and_content(self):
        response = requests.get(self.url_metro)
        content = response.content
        status_code = response.status_code
        return status_code, content

    def _set_item_on_dict(self, divs, info):
        linha_numero = None
        linha_nome = ""
        linha_status = ""
        for div in divs:
            if 'linha-numero' == div.get('class', []):
                linha_numero = int(div.text)
            if 'linha-nome' == div.get('class', []):
                linha_nome = div.text
            if 'linha-situacao' == div.get('class', []):
                linha_status = div.text

        info[linha_numero] = {linha_nome: linha_status}
        return info

    def _get_info_from_items(self, items):
        info = {}
        for item in items:
            divs = item.find_all('div')
            self._set_item_on_dict(divs, info)
        return info

    def get_metro_status(self):
        status_code, content = self._get_response_and_content()
        if status_code != 200:
            raise 'status: {}. Aborting...'.format(status_code)
        html = BS(content, "html.parser")
        items = html.find_all('li')
        info = self._get_info_from_items(items)
        return info

    def print_metro_status(self):
        metro_status = self.get_metro_status()
        for line, status in metro_status.items():
            print(line, status)
