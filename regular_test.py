import re


"""
\w      匹配字母数字及下划线 （*）
\W      匹配f非字母数字下划线 （*）
\s      匹配任意空白字符，等价于[\t\n\r\f] （*）
\S      匹配任意非空字符
\d      匹配任意数字 （*）
\D      匹配任意非数字
\A      匹配字符串开始
\Z      匹配字符串结束，如果存在换行，只匹配换行前的结束字符串
\z      匹配字符串结束
\G      匹配最后匹配完成的位置
\n      匹配一个换行符
\t      匹配一个制表符
^       匹配字符串的开头 （*）
$       匹配字符串的末尾 （*）
.       匹配任意字符，除了换行符，re.DOTALL标记被指定时，则可以匹配包括换行符的任意字符
[....]  用来表示一组字符，单独列出：[amk]匹配a,m或k
[^...]  不在[]中的字符：[^abc]匹配除了a,b,c之外的字符 
*       匹配0个或多个的表达式
+       匹配1个或者多个的表达式
?       匹配0个或1个由前面的正则表达式定义的片段，非贪婪方式 （*）
{n}     精确匹配n前面的表示
{m,m}   匹配n到m次由前面的正则表达式定义片段，贪婪模式
a|b     匹配a或者b
()      匹配括号内的表达式，也表示一个组
进阶：
要做更精确地匹配，可以用[]表示范围，比如：

[0-9a-zA-Z\_]可以匹配一个数字、字母或者下划线；

[0-9a-zA-Z\_]+可以匹配至少由一个数字、字母或者下划线组成的字符串，比如'a100'，'0_Z'，'Py3000'等等；

[a-zA-Z\_][0-9a-zA-Z\_]*可以匹配由字母或下划线开头，后接任意个由一个数字、字母或者下划线组成的字符串，也就是Python合法的变量；

[a-zA-Z\_][0-9a-zA-Z\_]{0, 19}更精确地限制了变量的长度是1-20个字符（前面1个字符+后面最多19个字符）
"""


# re模块 match返回一个match对象
def match_test():
    m = re.match(r'^(\d{3})-(\d{3,8})$', '010-12345')  # r前缀避免转义，^以3个数字开头
    print(m.group(0))  # 输出为010-12345
    print(m.group(1))  # 输出为010
    # 匹配时间
    t = '19:05:30'
    m1=re.match(r'^(0[0-9]|1[0-9]|2[0-3]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9]):(0[0-9]|1[0-9]|2[0-9]|3[0-9]|4[0-9]|5[0-9]|[0-9])$',t)
    print(m1.groups())  # 输出为('19','05','30')


"""
贪婪匹配：
正则匹配默认是贪婪匹配，也就是匹配尽可能多的字符，举例如下
"""


def tanlan_test():
    m = re.match(r'^(\d+)(0*)$', '102300')
    print(m.groups())  # 结果为('102300', ''),由于\d+采用贪婪匹配，直接把后面的0全部匹配了，结果0*只能匹配空字符串了
    m1 = re.match(r'^(\d+?)(0*)$', '102300').groups()  # 加一个？，可以采用非贪婪匹配
    print(m1.groups())  # 结果为('1023', '00')


"""
正则表达式博大精深，后面用到什么需要继续学习，共勉
"""
if __name__ == '__main__':
    match_test()

