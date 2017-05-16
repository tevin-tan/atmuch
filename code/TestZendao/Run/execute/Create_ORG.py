'''
    name: Create_ORG.py
    function: create an organization
    Autor:¡¡tsx
    date: 2015-11-15
    
'''

from  LoginZendao import login
from create_organrization import create_org
import time

if __name__ == "__main__":
	# login zendao
	# Initialization instance
	br = login()
	driver = br.login_browser()

	time.sleep(5)
	#     import pdb
	#     pdb.set_trace()
	create_org(driver)
