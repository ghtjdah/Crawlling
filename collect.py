from itertools import count

from bs4 import BeautifulSoup

from collection.crawler import crawling
import pandas as pd

RESULT_DIRECTORY = '__result__'


def crawling_pelicana():

    result = []

    # 시작과 끝이 있으면 range, 없으면 count
    for page in count(start=1):
        html = crawling('http://pelicana.co.kr/store/stroe_search.html?page={}&branch_name=&gu=&si='.format(page))
        bs = BeautifulSoup(html,'html.parser')
        tag_table = bs.find('table',attrs={'class':'table mt20'})
        tag_tbody = tag_table.find('tbody')
        tags_tr = tag_tbody.findAll('tr')

        # 마지막 페이지 검출
        if (len(tags_tr)==0):
            break
        for tag_tr in tags_tr:
            strings = list(tag_tr.strings)
            name = strings[1]
            address = strings[3]
            result.append((name,address))
            #print("{} : {}".format(name, address))

    # Store
    table = pd.DataFrame(result, columns=['name','address'])
    table.to_csv('{0}/pelicana_table.csv'.format(RESULT_DIRECTORY),encoding='utf-8',mode='w',index=True)
    print(table)

def crawling_nene():

    result = []

    # 시작과 끝이 있으면 range, 없으면 count
    for page in count(start=1):
        html = crawling('https://nenechicken.com/17_new/sub_shop01.asp?page={}&ex_select=1&ex_select2=&IndexSword=&GUBUN=A'.format(page))
        bs = BeautifulSoup(html, 'html.parser')
        tags_div = bs.findAll('div',attrs={'class':'shopInfo'})

        for tag_div in tags_div:
            shopname = tag_div.find('div',attrs={'class':'shopName'}).text
            shopaddress = tag_div.find('div',attrs={'class':'shopAdd'}).text
            result.append((shopname,shopaddress))

        if(len(tags_div)<24):
            break

    # Store
    table = pd.DataFrame(result, columns=['name', 'address'])
    table.to_csv('{0}/nene_table.csv'.format(RESULT_DIRECTORY), encoding='utf-8', mode='w', index=True)
    print(table)



def crawling_kyochon():

    result = []

    # 시작과 끝이 있으면 range, 없으면 count
    for page in count(start=1):
        html = crawling('http://www.kyochon.com/shop/domestic.asp?sido1=18&sido2=1&txtsearch='.format(page))
        bs = BeautifulSoup(html, 'html.parser')
        print(bs)

    # Store
    # table = pd.DataFrame(result, columns=['name', 'address'])
    # table.to_csv('{0}/kyochon_table.csv'.format(RESULT_DIRECTORY), encoding='utf-8', mode='w', index=True)
    # print(table)



if (__name__ == '__main__'):
    # 페리카나
    #crawling_pelicana()

    # 네네
    #crawling_nene()

    # 교촌
    crawling_kyochon()