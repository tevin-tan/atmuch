#coding:utf-8
import time



data = {'tanxiaoming': u'谭小明',
        'lidasi': u'李大四',
        'wangdawu': u'王大五',
                
        }

email = {'tanxiaoming': 'xiaoming@163.com',
         'lidasi': 'lisi@163.com',
         'wangdawu': 'wangwu@163.com',        
         }

def add_user(Browser):
    
    length = len(data)
    
    Browser.find_element_by_xpath(".//*[@id='menucompany']").click()
    time.sleep(3)
    
    for element in range(length):  
        Browser.find_element_by_xpath(".//*[@id='submenuaddUser']").click()
        time.sleep(3)
        
        #select "测试"
        dept = Browser.find_element_by_xpath(".//*[@id='dept_chosen']/a/span")
        dept.click()
        Browser.find_element_by_xpath(".//*[@id='dept_chosen']/div/ul/li[2]").click()
        #输入用户名和密码及确认密码
        Browser.find_element_by_xpath(".//*[@id='account']").send_keys(data.keys()[element])
        Browser.find_element_by_xpath(".//*[@id='realname']").send_keys(data.values()[element])
        Browser.find_element_by_xpath(".//*[@id='password1']").send_keys("123456")
        Browser.find_element_by_xpath(".//*[@id='password2']").send_keys("123456") 
        #职位选择,下拉列表
        b1 = Browser.find_element_by_xpath(".//*[@id='role']")  
        b1.find_element_by_xpath("//option[@value='dev']").click()
        
        Browser.find_element_by_xpath(".//*[@id='group_chosen']/a").click()
        Browser.find_element_by_xpath(".//*[@id='group_chosen']/div/ul/li[3]").click()
        
        
        Browser.find_element_by_xpath(".//*[@id='email']").send_keys(email[data.keys()[element]])   
        Browser.find_element_by_xpath(".//*[@id='commiter']").send_keys("001")
        
        Browser.find_element_by_xpath(".//*[@id='join']").send_keys("2015-12-01")
        
        Browser.find_element_by_xpath(".//*[@id='verifyPassword']").send_keys("123456")
        Browser.find_element_by_xpath(".//*[@id='submit']").click()
    
    
#     Browser.find_element_by_xpath(".//*[@id='account']").send_keys("Tan")
#     Browser.find_element_by_xpath(".//*[@id='realname']").send_keys(u"̷谭xx")
#     Browser.find_element_by_xpath(".//*[@id='password1']").send_keys("123456")
#     Browser.find_element_by_xpath(".//*[@id='password2']").send_keys("123456") 
#     
#     b1 = Browser.find_element_by_xpath(".//*[@id='role']")  
#     b1.find_element_by_xpath("//option[@value='dev']").click()
#     
#     Browser.find_element_by_xpath(".//*[@id='email']").send_keys("tan@xx.com")   
#     Browser.find_element_by_xpath(".//*[@id='commiter']").send_keys("001")
#     
#     Browser.find_element_by_xpath(".//*[@id='join']").send_keys("2015-12-01")
#     
#     Browser.find_element_by_xpath(".//*[@id='verifyPassword']").send_keys("123456")
#     Browser.find_element_by_xpath(".//*[@id='submit']").click()
    
