#coding:utf-8
'''
    name: AddGroup.py
    Func: add group
    Autor: Tsx
    date: 2015-11-15
'''
import time


def add_group(Browser, group_name=None, group_des=None):
    Browser.find_element_by_xpath(".//*[@id='menucompany']").click()
    time.sleep(3)
    Browser.find_element_by_xpath(".//*[@id='submenuaddGroup']").click()
    time.sleep(1)
    Browser.find_element_by_xpath(".//*[@id='name']").send_keys(group_name)
    Browser.find_element_by_xpath(".//*[@id='desc']").send_keys(group_des)
    Browser.find_element_by_xpath(".//*[@id='submit']").click()
    