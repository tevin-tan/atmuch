
'''
    name:  Add_group.py
    function: add some group
    Autor: tsx
    date:  2015-11-15   
'''

from  LoginZendao import login
from  AddGroup import add_group
import time



if __name__ == "__main__":
    
     #login zendao
    #Initialization instance
    br = login()
    driver = br.login_browser()
    
    time.sleep(5)
    add_group(driver,'Automation', 'Best Automation team')
    