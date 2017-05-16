#coding:utf-8
'''
    name: CreateProduct.py
    function: create an product
    Autor: tan
    date: 2014-11-16
'''
import time

def create_product(Browser):
    
    time.sleep(3)
    #Product
    Browser.find_element_by_xpath(".//*[@id='menuproduct']").click()
    time.sleep(1)
    #Product name
    Browser.find_element_by_xpath(".//*[@id='name']").send_keys("ZoneDirector")
    #product code
    Browser.find_element_by_xpath(".//*[@id='code']").send_keys("odc-001")
    #product owner
    Browser.find_element_by_xpath(".//*[@id='PO_chosen']/a").click()
    #select owner 
    Browser.find_element_by_xpath(".//*[@id='PO_chosen']/div/ul/li[2]").click()
    time.sleep(1)
    #Test owner
    Browser.find_element_by_xpath(".//*[@id='QD_chosen']/a").click()
    #select test owner
    Browser.find_element_by_xpath(".//*[@id='QD_chosen']/div/ul/li[4]").click()
    #public owner
    Browser.find_element_by_xpath(".//*[@id='RD_chosen']/a").click()
    #select public owner
    Browser.find_element_by_xpath(".//*[@id='RD_chosen']/div/ul/li[3]").click()
    #product discription
    Browser.find_element_by_xpath("html").send_keys("congratulations")
    #check access control
    Browser.find_element_by_xpath(".//*[@id='aclprivate']").click()
    #save
    Browser.find_element_by_xpath(".//*[@id='submit']").click()
    
    
    
    
    
    
    
    