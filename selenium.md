#一、什么是selenium
selenium 是一套完整的web应用程序测试系统，包含了测试的录制（selenium IDE）,编写及运行（Selenium Remote Control）和测试的并行处理（Selenium Grid）。Selenium的核心Selenium Core基于JsUnit，完全由JavaScript编写，因此可以用于任何支持JavaScript的浏览器上。

selenium可以模拟真实浏览器，自动化测试工具，支持多种浏览器，爬虫中主要用来解决JavaScript渲染问题。
#二、selenium基本使用
爬虫主要用的是selenium的Webdriver，可以查看Webdriver支持哪些浏览器
![exsample icon](https://github.com/joyce0101/Python_web_spider/blob/master/pics/webdriver.png)
![exsample icon](https://github.com/joyce0101/Python_web_spider/blob/master/pics/webdriver_help.png)
上图显示基本上支持所有的浏览器
*这里要说一下比较重要的PhantomJS,PhantomJS是一个而基于WebKit的服务端JavaScript API,支持Web而不需要浏览器支持，其快速、原生支持各种Web标准：Dom处理，CSS选择器，JSON等等。PhantomJS可以用用于页面自动化、网络监测、网页截屏，以及无界面测试*
