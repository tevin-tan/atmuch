
'''
    name: Create_product.py
    function:add an product
    Autor:tsx
    date: 2015-11-16   
'''


from  LoginZendao import login
from  CreateProduct import create_product
import time



if __name__ == "__main__":
    
     #login zendao
    #Initialization instance
    br = login()
    driver = br.login_browser()
    
    time.sleep(5)
    create_product(driver)
    