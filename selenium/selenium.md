# 一、什么是selenium
selenium 是一套完整的web应用程序测试系统，包含了测试的录制（selenium IDE）,编写及运行（Selenium Remote Control）和测试的并行处理（Selenium Grid）。Selenium的核心Selenium Core基于JsUnit，完全由JavaScript编写，因此可以用于任何支持JavaScript的浏览器上。

selenium可以模拟真实浏览器，自动化测试工具，支持多种浏览器，爬虫中主要用来解决JavaScript渲染问题。
# 二、selenium基本使用
爬虫主要用的是selenium的Webdriver，可以查看Webdriver支持哪些浏览器
![exsample icon](https://github.com/joyce0101/Python_web_spider/blob/master/pics/webdriver.png)
![exsample icon](https://github.com/joyce0101/Python_web_spider/blob/master/pics/webdriver_help.png)
上图显示基本上支持所有的浏览器   
**这里要说一下比较重要的PhantomJS,PhantomJS是一个而基于WebKit的服务端JavaScript API,支持Web而不需要浏览器支持，其快速、原生支持各种Web标准：Dom处理，CSS选择器，JSON等等。PhantomJS可以用用于页面自动化、网络监测、网页截屏，以及无界面测试**
## 访问页面

	def get_url():  
    	browser = webdriver.Chrome()  
    	browser.get("http://baidu.com")  
    	print(browser.page_source)  
    	browser.close()  

   
运行上述代码后，脚本自动代开chrome浏览器，打开百度后，关闭浏览器,并打印页面信息   
*注意：运行时可能会抛出没有Chromedriver的异常，此时只要brew install chromedriver 即可* 
## 查找元素
### 单个元素查找
	def find_element():
    	browser = webdriver.Chrome()
    	browser.get("http://www.taobao.com")
    	mes = browser.find_element_by_id("q")
    	print(mes)
    	browser.close()
这里列举一下常用的查找元素方法：   

find_element_by_name   
find_element_by_id   
find_element_by_xpath   
find_element_by_link_text   
find_element_by_partial_link_text   
find_element_by_tag_name   
find_element_by_class_name   
find_element_by_css_selector   
### 多个元素查找
其实多个元素和单个元素没什么区别，举个例子：find_elements,单个元素是find_element,其他使用上没什么区别，通过其中的一个例子演示: 

    def find_mul():
    	browser = webdriver.Chrome()
    	browser.get("http://www.taobao.com")
    	list = browser.find_elements_by_css_selector('.service-bd li')
    	print(list)
    	browser.close()
这样就获得一个列表。结果如下：  
![查找多个元素](https://github.com/joyce0101/Python_web_spider/blob/master/pics/find_mul.png)
### 元素交互操作
代码见element_interaction()函数
    browser = webdriver.Chrome()
    browser.get("http://www.taobao.com")
    input_str = browser.find_element_by_id('q')
    input_str.send_keys("ipad")
    time.sleep(1)
    input_str.clear()
    input_str.send_keys("MacBook pro")
    button = browser.find_element_by_class_name("btn-search")
    button.click()
    time.sleep(10)
运行结果可以看出会打开Chrome浏览器，打开淘宝，输入pro后，删除，输入macbook pro，然后点击搜索
Selenium所有的api文档：http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains
### 交互动作
代码见action_chains(）
    browser = webdriver.Chrome()

    url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    source = browser.find_element_by_css_selector('#draggable')
    target = browser.find_element_by_css_selector('#droppable')
    actions = ActionChains(browser)
    actions.drag_and_drop(source）
    actions.perform()
更多操作参考：http://selenium-python.readthedocs.io/api.html#module-selenium.webdriver.common.action_chains

	

