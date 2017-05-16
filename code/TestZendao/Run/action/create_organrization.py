#coding:utf-8
'''
    function: create organization 
    Autor: tsx
    date: 2015-11-14
    
'''
import time


lst = [u"测试", u"开发", u"产品"]


def create_org(drive):
    length = len(lst)
    
    drive.find_element_by_xpath(".//*[@id='menucompany']").click()
    drive.find_element_by_xpath(".//*[@id='submenudept']").click()  
    
    #列表单元格赋值
    for i in range(length):
        Te = drive.find_element_by_xpath(".//*[@id='depts[]']")
        Te.send_keys(lst[i])
        Te.submit()
        time.sleep(1)
        
    
    





    
    
    