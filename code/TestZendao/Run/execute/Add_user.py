
'''
    name: Add_user.py
    function:add some users
    Autor:tsx
    date: 2015-11-15   
'''


import time

from  AddUsers import add_user
from  LoginZendao import login

if __name__ == "__main__":
    
     #login zendao
    #Initialization instance
    br = login()
    driver = br.login_browser()
    
    time.sleep(5)
    add_user(driver)
    