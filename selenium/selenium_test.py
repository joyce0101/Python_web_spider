from selenium import webdriver


def get_url():
    browser = webdriver.Chrome()
    browser.get("http://baidu.com")
    print(browser.page_source)
    browser.close()


def find_element():
    browser = webdriver.Chrome()
    browser.get("http://www.taobao.com")
    mes = browser.find_element_by_id("q")
    print(mes)
    browser.close()


def find_mul():
    browser = webdriver.Chrome()
    browser.get("http://www.taobao.com")
    list = browser.find_elements_by_css_selector('.service-bd li')
    for ele in list:
        print(ele)
    browser.close()


if __name__ == '__main__':
    find_mul()
