from selenium import webdriver


def get_url():
    browser = webdriver.Chrome()
    browser.get("http://baidu.com")
    print(browser.page_source)
    browser.close()


if __name__ == '__main__':
    get_url()
