import bs4
from bs4 import BeautifulSoup
import re


"""
Beautiful Soup 4.4官方文档连接：http://beautifulsoup.readthedocs.io/zh_CN/latest/
Beautiful Soup 是一个可以从HTML或XML文件中提取数据的Python库.
它能够通过你喜欢的转换器实现惯用的文档导航,查找,修改文档的方式.Beautiful Soup会帮你节省数小时甚至数天的工作时间.
推荐使用lxml解析器，它速度更快，功能更加强大，其他解析器查看官方文档。
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
    print(soup.prettify())  # prettify()函数格式化输出，经常用到，需要记好
    print(soup.title)
    print(soup.title.name)
    print(soup.title.string)
    print(soup.title.parent.name)
    print(soup.p)
    print(soup.p["class"])
    print(soup.a)
    print(soup.find_all('a'))
    print(soup.find(id='link3'))


"""
Beautiful Soup将复杂HTML文档转换成一个复杂的树形结构，每个节点都是一个python对象，所有对象可以归纳为四种：
1、Tag 2、NavigableString 3、Beautiful Soup 4、Comment
下面的代码进行举例。
"""


def soup_test():
    html = '''
        <html><head><title>The Dormouse's story</title></head>
        <body>
        <p class="title" name="dromouse"><b>The Dormouse's story</b></p>
        <p class="story">Once upon a time there were three little sisters; and their names were
        <a href="http://example.com/elsie" class="sister" id="link1">!--Elsie--</a>,
        <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
        <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
        and they lived at the bottom of a well.</p>
        <p class="story">...</p>
        '''
    soup = BeautifulSoup(html, 'lxml')
    # 1、tag对象的使用，即HTML文档中的标签
    print(soup.title)  # <title>The Dormouse's story</title>
    print(soup.head)  # <head><title>The Dormouse's story</title></head>
    print(soup.a)  # <a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>，需要注意它查找第一个符合要求的标签
    print(type(soup.title))  # 验证对象的类型， <class 'bs4.element.Tag'>
    # 对于tag，他有两个重要的属性，name和attrs
    print(soup.name)  # [document]
    print(soup.head.name)  # head ,输出标签本身的名字
    print(soup.p.attrs)  # {'class': ['title'], 'name': 'dromouse'}，将p标签的属性打印出来，典型的字典类型，可以获取键值。
    print(soup.p["class"])  # title 获取字典的某个属性
    # 2、NavigableString 已经得到标签的内容，获取标签中的文字用.string解决
    print(soup.p.string)  # The Dormouse's story
    # 3、Beautiful Soup 文档的全部内容
    # 4、Comment 是一个特殊类型的NavigableString类型，其输出的内容仍然不包括注释符号，如果不好好处理，对文本会造成麻烦。
    print(soup.a)  # <a class="sister" href="http://example.com/elsie" id="link1"><!-- Elsie --></a>
    print(soup.a.string)  # Elsie
    print(type(soup.a.string))  # <class 'bs4.element.Comment'>
    # a标签中的内容其实是注释，但我们用.string输出时，已经把注释符号去掉了，因此在使用前最好判断是不是Comment类型
    if type(soup.a.string) == bs4.element.Comment:
        print(soup.a.string)  # 判断之后进行相应的操作


def trave_test():
    """
    遍历文档树
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
    # 1、直接子节点：.contents 和 .children属性
    print(soup.head.contents)  # tag的.content属性可以将tag的子节点以列表的形式输出，[<title>The Dormouse's story</title>]
    print(soup.head.contents[0])  # 可以用列表索引来获取它的某一个元素
    print(soup.head.children)  # <list_iterator object at 0x000002C89BCA1CF8>,我们可以发现他是一个list生成器对象
    # 可以通过遍历获得里面的内容
    for child in soup.body.children:
        print(child)
    # 2、所有子孙节点：.descendants属性
    for child in soup.descendants:
        print(child)  # 打印出了所有的节点
    # 3、多个内容: .string和.stripped_strings属性
    for string in soup.strings:
        print(repr(string))  # 获取里面的内容
    for string in soup.stripped_strings:
        print(repr(string))  # 输出的字符串中可能包含很多空格或空行，使用stripped_strings可以除多余空白内容
    # 4、父节点和全部父节点
    p = soup.p
    print(p.parent.name)  # body
    # 全部父节点
    content = soup.head.title.string
    for parent in content.parents:
        print(parent.name)
    # 5、兄弟节点
    print(soup.a.next_siblings)  # 获取后面的兄弟节点
    print(soup.a.previous_siblings)  #获取前面的兄弟节点
    print(soup.a.next_sibling)  # 获取下一个兄弟标签
    print(soup.a.previous_sinbling)  # 获取上一个兄弟标签
    # 6、前后节点
    print(soup.head.next_element)  # <title>The Dormouse's story</title>
    # 通过.next_elements和.previous_elements的迭代器就可以向前或向后访问文档的解析内容
    for element in soup.head.next_elements:
        print(repr(element))


def has_class_no_id(tag):
    return tag.has_attr('class') and not tag.has_attr('id')


def serach_test():
    """
    搜索文档树
    以find_all( name , attrs , recursive , text , **kwargs )为例
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
    # 1、name参数，可以传递字符串、正则表达式、列表、True
    soup = BeautifulSoup(html, 'lxml')
    """
    print(soup.find_all("b"))  # 传递字符串参数，查找文档中所有<b>标签,[<b>The Dormouse's story</b>]
    for tag in soup.find_all(re.compile("^b")):
        print(tag.name)  # 传递以b开头的正则表达式，结果为body b
    print(soup.find_all(["a", "b"]))  # 传入列表参数，soup将与列表中任意匹配的元素返回，下面找出文档中所有<a>和<b>标签
    for tag in soup.find_all(True):
        print(tag.name)  # True匹配任何值，查找所有tag，但是不会返回字符串节点
    # 同时可以传递方法，如果这个方法返回True表示当前元素匹配，并且被找到，如果不是则返回False
    print(soup.find_all(has_class_no_id))  # has_class_no_id在上面定义，这个方法将返回所有<p>标签
    # 2、keyword参数，不知道标签，而是知道标签中指定的属性。
    print(soup.find_all(id='link2'))
    # [<a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>],soup会搜索tag的每一个id属性
    soup.find_all(href=re.compile("elsie"),id='link1')  # 可以同时过滤tag的多个属性，
    """
    # 用class过滤时，class是python的关键字，这时，加个下划线就可以了
    print(soup.find_all("a", class_="sister"))
    # 有些tag属性在搜素时不能使用，比如HTML5中的"data-*"属性
    data_soup = BeautifulSoup('<div data-foo="value">foo!</div>')
    # print(data_soup.find_all(data-foo="value")) 错误写法
    print(data_soup.find_all(attrs={"data-foo":"value"}))  # 通过 find_all() 方法的 attrs 参数定义一个字典参数来搜索包含特殊属性的tag
    # 3、text参数可以搜素文档中的字符串内容，与name参数的可选值一样，可以传递字符串、列表、正则表达式等等
    print(soup.find_all(text="Elsie"))
    # 4、limit参数，限制返回结果的数量
    print(soup.find_all("a", limit=2))
    # 5、recursive参数，当设置recursive=False时，返回tag的的直接子节点
    test_html = """
    <html>
 <head>
  <title>
   The Dormouse's story
  </title>
 </head>
    """
    test_soup = BeautifulSoup(test_html, 'lxml')
    print(test_soup.html.find_all("title",recursive=False))  # 结果为[]空，因为html的直接子节点为head


"""
其他一些类似的用法：
find_parents()返回所有祖先节点，find_parent()返回直接父节点。
find_next_siblings()返回后面所有兄弟节点，find_next_sibling()返回后面第一个兄弟节点。
find_previous_siblings()返回前面所有兄弟节点，find_previous_sibling()返回前面第一个兄弟节点。
find_all_next()返回节点后所有符合条件的节点, find_next()返回第一个符合条件的节点
find_all_previous()返回节点后所有符合条件的节点, find_previous()返回第一个符合条件的节点
"""


def css_test():
    """
    CSS选择器，写CSS时，标签名不加任何修饰，类名前加.，id名前加#，可以采用类似的方法筛选元素，用到的方法是soup.select()返回list
    """
    html = '''
    <div class="panel">
        <div class="panel-heading">
            <h4>Hello</h4>
        </div>
        <div class="panel-body">
            <ul class="list" id="list-1">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
                <li class="element">Jay</li>
            </ul>
            <ul class="list-small" id="list-2">
                <li class="element">Foo</li>
                <li class="element">Bar</li>
            </ul>
        </div>
    </div>
    '''
    soup = BeautifulSoup(html, 'lxml')
    print(soup.select('div'))  # 通过标签名来查找
    print(soup.select('.panel'))  # 通过类名来查找
    print(soup.select('#list1'))  # 通过id来查找
    print(soup.select('ul #list-2'))  # 组合查找，如查找ul标签中，id等于list-2的内容，两者通过空格隔开
    # 属性查找，属性需要用中括号括起来，注意属性和标签属于同一节点，所以中间不能加空格，否则会无法匹配到。
    print(soup.select('li[class="element"]'))
    # 以上select方法返回的结果都是列表形式，可以遍历列表输出
    for li in soup.select('li'):
        print(li.get_text())  # get_text()函数获取内容，Foo Bar Jay
        print(li['class'])  # 获取属性,element


if __name__ == '__main__':
    css_test()
