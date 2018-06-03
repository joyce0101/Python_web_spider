import urllib.parse
import urllib.request
import urllib.error
import socket
from urllib import request
import http.cookiejar
"""
urllib 是python的内置HTTP请求库
包括以下模块
1.urllib.request 请求模块
2.urllib.error 异常模块
3.urllib.parse url解析模块
4.urllib.robotparser robots.txt解析模块
"""
"""
一.urllib.request 模块
urlopen：
关于urllib.request.urlopen参数的介绍
urllib.request.urlopen(url, data=None, [timeout, ]*, cafile=None, capath=None, cadefault=False, context=None)
该函数一般常用三个参数，urllib.request.urlopen(url,data,timeout):
url为请求的网址；data为请求的参数；timeout设置超时时间，防止程序一直等待。
"""
# 示例如下


def request_test():
    payload = bytes(urllib.parse.urlencode({'world': 'hello'}), encoding='utf8')  # urlencode()将json解析成url参数'world=hello'
    print(payload)
    response1 = urllib.request.urlopen('http://httpbin.org/post', data=payload)
    print(response1.read())
    response1 = urllib.request.urlopen('http://httpbin.org/get', timeout=1)
    print(response1.read())


"""
设置请求时间为1的时候不会报错，但是设置为0.1的时候会抛出异常，这时需要对异常进行抓取
"""


def timeout_test():
    try:
        response2 = urllib.request.urlopen('http://httpbin.org/get', timeout=0.1)
    except urllib.error.URLError as e:
        if isinstance(e.reason, socket.timeout):
            print("TIME OUT")


"""
response是请求的响应，response.read()读取响应体的内容
1.可以通过type(response) 获取响应类型
2.response.getheaders() 获取响应头，为列表形式，包含所有头部信息，如下
[('Connection', 'close'), ('Server', 'gunicorn/19.8.1'), ('Date', 'Thu, 31 May 2018 12:51:41 GMT'),('Content-Type', 'application/json'), 
('Content-Length', '183'),('Access-Control-Allow-Origin', '*'), ('Access-Control-Allow-Credentials', 'true'), ('Via', '1.1 vegur')]
可以通过response.getheaders('Server'),获取指定头部信息
"""
"""
设置指定头部信息，很多网站为了防止爬虫，需要携带一些头部信息，常见的有 user-agent参数（用户代理，包括浏览器类型版本，操作系统等信息）
如下为一个列子：
"""


def header_test():
    apiurl = 'http://httpbin.org/post'
    dicts = {
        'name': 'Germey'
    }
    payload = bytes(parse.urlencode(dicts), encoding='utf8')
    req = request.Request(url=apiurl, data=payload, method='POST')
    req.add_header('User-Agent', 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)')
    response1 = request.urlopen(req)
    print(response1.read().decode('utf-8'))


"""
高级用法，各种handler
1.代理，ProxyHandler
通过rulllib.request.ProxyHandler()可以设置代理,网站它会检测某一段时间某个IP 的访问次数，如果访问次数过多，它会禁止你的访问,所以这个时候需要通过设置代理来爬取数据
"""

def proxy_test():
    proxy_handler = urllib.request.ProxyHandler(
        {
            'http': 'http://127.0.0.1:9743',
            'https': 'https://127.0.0.1:9743'
        }
    )
    opener = urllib.request.build_opener(proxy_handler)
    response = opener.open('http://httpbin.org/get')
    print(response.read())


"""
2.cookie,HTTPCookiProcessor
cookie中保存中我们常见的登录信息，有时候爬取网站需要携带cookie信息访问,这里用到了http.cookijar，用于获取cookie以及存储cookie
"""


def cookie_test():
    cookie = http.cookiejar.CookieJar()
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    for item in cookie:
        print(item.name + "=" + item.value)


"""
同时cookie可以写入到文件中保存
"""
# http.cookiejar.MozillaCookieJar()方式


def cookie_save1():
    filename = "cookie.txt"
    cookie = http.cookiejar.MozillaCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)

# http.cookiejar.LWPCookieJar()方式


def cookie_save2():
    filename = 'cookie.txt'
    cookie = http.cookiejar.LWPCookieJar(filename)
    handler = urllib.request.HTTPCookieProcessor(cookie)
    opener = urllib.request.build_opener(handler)
    response = opener.open('http://www.baidu.com')
    cookie.save(ignore_discard=True, ignore_expires=True)


"""
二、urllib.error异常处理模块
通常有两个异常错误：
URLError一个属性：reason，捕获异常的时候只能打印异常信息
HTTPError三个属性：code,reason,headers，即抓异常的时候可以获得code,reson，headers三个信息，例子如下
"""


def error_test():
    try:
        response = request.urlopen("http://pythonsite.com/1111.html")
    except error.HTTPError as e:
        print(e.reason)
        print(e.code)
        print(e.headers)
    except error.URLError as e:
        print(e.reason)

    else:
        print("reqeust successfully")


"""
三、urllib.parse url解析
1、urlparse() 函数可以将 URL 解析成 ParseResult 对象。
"""
result = urlparse("http://www.baidu.com/index.html;user?id=5#comment")
print(result)
"""结果为：ParseResult(scheme='http', netloc='www.baidu.com', path='/index.html', params='user', query='id=5', fragment='comment')
"""
"""
2.urlunpars()函数与1相反，为拼接
"""
data = ['http', 'www.baidu.com', 'index.html', 'user', 'a=123', 'commit']
print(urlunparse(data))
"""
3.urlencode()函数将字典（json）格式转换为url的参数
"""


def urlencode_test():
    params = {
        "name": "zhaofan",
        "age": 23,
    }
    base_url = "http://www.baidu.com?"

    url = base_url + urlencode(params)
    print(url)  # 结果：http://www.baidu.com?name=zhaofan&age=23

