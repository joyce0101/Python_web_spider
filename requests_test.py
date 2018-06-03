import requests
import urllib3
"""
Requests是用python语言基于urllib编写的，采用的是Apache2 Licensed开源协议的HTTP库
requests库比urllib库好用很多，建议爬虫相关和http协议相关使用requests库
"""
"""
requests有各种请求方式，大致如下：

requests.get("http://httpbin.org/get")
requests.post("http://httpbin.org/post")
requests.put("http://httpbin.org/put")
requests.delete("http://httpbin.org/delete")
requests.head("http://httpbin.org/get")#获取头部信息
requests.options("http://httpbin.org/get")#查看支持的方法
"""
# 1.GET请求
"""
get请求，允许直接将参数附在url的后面，"http://httpbin.org/get?name=zhaofan&age=23"
或者使用params参数
"""


def get_test():
    data = {
        "name": "nihao",
        "age": 18
    }
    response = requests.get("http://httpbin.org/get", params=data)
    print(response.url)
    print(response.text)
    print(response.json())#解析json


"""
添加headers，当你访问知乎时，需要头部信息，在chrome浏览器中输入chrome://version就可以看到用户代理（通常包含浏览器版本，操作系统版本等信息）
"""


def get_zhihu():
    headers = {

        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_4) AppleWebKit/537.36 (KHTML, like Gecko) "
                      "Chrome/58.0.3029.110 Safari/537.36"
    }
    response = requests.get("https://www.zhihu.com", headers=headers)
    print(response.text)
# 2.post请求


"""
post请求，参数不能附在url后面，要使用data参数，其余如headers和get请求一样
"""


def post_test():
    data = {
        "hello": "world",
        "age": 18
    }
    response = requests.post("http://httpbin.org/post", data=data)
    print(response.text)
# 高级用法
# 获取cookie，通常用于回话维持


def get_cookies():
    response = requests.get("http://www.baidu.com")
    print(response.cookies)
    for key, value in response.cookies.items():
        print(key + "=" + value)
    # cookies的一个作用就是模拟登录，会话维持
    s = requests.Session()
    s.get("http://httpbin.org/cookies/set/number/123456")
    response1 = s.get("http://httpbin.org/cookies")
    print(response1.text)
# 证书验证，现在很多网站是https访问，此时涉及证书问题,为了避免这种情况的发生可以通过verify=False


def zhengshu():
    urllib3.disable_warnings()  # 忽略一个warning
    response = requests.get("https://www.12306.cn", verify=False)
    print(response.status_code)
# 代理设置


def set_proxies():
    proxies = {
        "http": "socks5://127.0.0.1:9999"
    }
    response = requests.get("https://www.baidu.com", proxies=proxies)
    print(response.text)


"""
如果需要设置账户名和密码
proxies = {
"http":"http://user:password@127.0.0.1:9999"
}
"""
# 异常处理，http://www.python-requests.org/en/master/api/#exceptions 在该网站中，学会查看文档是十分重要滴
if __name__ =='__main__':
    set_proxies()