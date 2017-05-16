#coding:utf-8
import locator
import time

def create_an_project(browser, p_n=None, p_c =None, d_st = None ,d_end=None, awd=0 ,t_n = None, Pro_type='sprint', p_des = None, 
                      access='access_default'):
    try:
        element = browser.find_element_by_xpath(locator.locate['new_project'])
    except Exception, e:
        print e
        browser.find_element_by_xpath(".//*[@id='menuproject']").click()
        time.sleep(1)
        element = browser.find_element_by_xpath(".//*[@id='submenucreate']")
        
    time.sleep(1)
    element.click()
    b1 = browser.find_element_by_xpath(locator.locate['pro_name'])
    time.sleep(2)
    b1.send_keys(p_n )
    browser.find_element_by_xpath(locator.locate['pro_code']).send_keys(p_c)
    
    #日历控件
    d_s = browser.find_element_by_xpath(locator.locate['date_start'])
    d_s.clear()
    d_s.send_keys(d_st)
    d_s.click()
    d_e = browser.find_element_by_xpath(locator.locate["date_end"])
    d_e.clear()
    d_e.send_keys(d_end)
    d_e.click()
    
    browser.find_element_by_xpath(locator.locate['AWD']).send_keys(awd)
    time.sleep(1)
    browser.find_element_by_xpath(locator.locate['team_name']).send_keys(t_n)
    
    #下拉列表菜单
    p_t = browser.find_element_by_xpath(locator.locate["pro_type"])
    p_t.find_element_by_xpath(locator.locate[Pro_type]).click()
    time.sleep(1)
    
    #文本描述
    browser.find_element_by_xpath(locator.locate['pro_des']).send_keys(p_des)
    
    #访问模式选择，checkbutton
    p_a = browser.find_element_by_xpath(locator.locate[access])
    p_a.click()
    time.sleep(1)
    
    #保存，创建成功
    browser.find_element_by_xpath(locator.locate['save']).click()


