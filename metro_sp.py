#coding:utf-8

import re
import httplib2


URL_METRO = 'http://www.metro.sp.gov.br/Sistemas/direto-do-metro-via4/diretodoMetroHome.aspx'
RE_INFO_METRO = re.compile(r'\{*\"id\".*?\}', re.DOTALL)

def find_metro():
    h = httplib2.Http(".cache")
    headers = {'cache-control':'max-age=%s' %(3600*24*365)}
    resp, content = h.request(URL_METRO, "GET", headers=headers)
    all_metro_status = RE_INFO_METRO.findall(content)
      
    print all_metro_status

    print resp['status']
    return all_metro_status


if __name__ == '__main__':
    find_metro()
