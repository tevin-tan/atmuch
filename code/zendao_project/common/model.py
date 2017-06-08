# coding:utf-8

from selenium import webdriver
import os
import logging


def browser(arg=None):
    '''选择浏览器'''
    if arg == "ie":
        driver = webdriver.Firefox()
    elif arg == "chrome":
        driver = webdriver.Chrome()
    else:
        driver = webdriver.Firefox()

    return driver


def insert_img(driver, file_name):
    '''截图'''
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    # print("base_dir:" + base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir + '/log/'
    # print("base" + base)
    file_path = base + file_name
    # print(file_path)
    driver.get_screenshot_as_file(file_path)


def logger_init():
    '''定义logger级别'''
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
                        datefmt='%a, %d %b %Y %H:%M:%S',
                        # filename='myapp.log',
                        filemode='w')

    return logging


if __name__ == '__main__':
    dr = browser()
    dr.get("http://www.baidu.com")
    insert_img(dr, 'baidu.jpg')
    dr.quit()

    logger = logger_init()
    logger.debug('This is debug message')
    logger.info('This is info message')
    logger.warning('This is warning message')
