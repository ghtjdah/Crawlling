from bs4 import BeautifulSoup

html = """<td class="title black">
						<div class="tit3" id="t3" name="t3's name">
							<a href="/movie/bi/mi/basic.nhn?code=163533" title="안시성">안시성</a>
						</div>
					</td>"""


# 1. Tag 조회
def ex1():
    bs =BeautifulSoup(html,"html.parser")
    #print(bs,'\n')

    tag=bs.td
    print(tag,'\n')
    #print(tag.div)

    tag = bs.div
    print(tag,'\n')

    tag=bs.a
    print(tag,'\n')

    print('=======================================================')
    print(bs,'\n')
    print(bs.div,'\n')
    print(bs.div.a)


# 2. Atribute 값 조회
def ex2():
    bs = BeautifulSoup(html, "html.parser")

    tag = bs.td
    print(tag,'\n')
    print(tag['class'])
    print(tag.name,'\n')

    tag = bs.div
    print(tag['id'])
    print(tag.attrs)
    # print(tag['name'])
    # print(tag.name)


# 3. attr로 조회하기
def ex3():
    bs = BeautifulSoup(html, "html.parser")

    tags = bs.find('td',attrs={'class':'black'})
    print(tags,'\n')

    tags = bs.find(attrs={'title':'안시성'})
    print(tags,'\n')

    tags = bs.find('a')
    print(tags)



if (__name__ == '__main__'):
    #ex1()
    #ex2()
    ex3()