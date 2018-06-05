from bs4 import BeautifulSoup


"""
Beautiful Soup 4.4官方文档连接：http://beautifulsoup.readthedocs.io/zh_CN/latest/
Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库.
它能够通过你喜欢的转换器实现惯用的文档导航,查找,修改文档的方式.Beautiful Soup会帮你节省数小时甚至数天的工作时间.
"""


def test():
    """
    快速开始，一个简单的示例，使用Beautiful Soup 解析这段代码，能够得到一个BeaytifulSoup对象，按照lxml格式的结构输出。
    """
    html = '''
    <html><head><title>The Dormouse's story</title></head>
    <body>
    <p class="title"><b>The Dormouse's story</b></p>

    <p class="story">Once upon a time there were three little sisters; and their names were
    <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
    <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
    <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
    and they lived at the bottom of a well.</p>
    <p class="story">...</p>
    '''
    soup = BeautifulSoup(html, 'lxml')
    print(soup.prettify())
    print(soup.title)
    print(soup.title.name)
    print(soup.title.string)
    print(soup.title.parent.name)
    print(soup.p)
    print(soup.p["class"])
    print(soup.a)
    print(soup.find_all('a'))
    print(soup.find(id='link3'))
