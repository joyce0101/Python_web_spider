from selenium import webdriver
import time
from selenium.webdriver import ActionChains


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


def element_interaction():
    browser = webdriver.Chrome()
    browser.get("http://www.taobao.com")
    input_str = browser.find_element_by_id('q')
    input_str.send_keys("ipad")
    time.sleep(1)
    input_str.clear()
    input_str.send_keys("MakBook pro")
    button = browser.find_element_by_class_name("btn-search")
    button.click()
    time.sleep(10)


def action_chains():
    browser = webdriver.Chrome()

    url = "http://www.runoob.com/try/try.php?filename=jqueryui-api-droppable"
    browser.get(url)
    browser.switch_to.frame('iframeResult')
    source = browser.find_element_by_css_selector('#draggable')
    target = browser.find_element_by_css_selector('#droppable')
    actions = ActionChains(browser)
    actions.drag_and_drop(source, target)
    actions.perform()


if __name__ == '__main__':
    action_chains()

