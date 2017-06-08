
'''
    name: Create_product.py
    function:add an product
    Autor:tsx
    date: 2015-11-16   
'''


import time

from  CreateProduct import create_product
from  LoginZendao import login

if __name__ == "__main__":
    
     #login zendao
    #Initialization instance
    br = login()
    driver = br.login_browser()
    
    time.sleep(5)
    create_product(driver)
    