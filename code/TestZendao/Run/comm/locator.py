'''
Filename: locator.PY
Function: all the xpath of zandao
 
'''

#conding:utf-8

url = "http://localhost/zentao/user-login.html"
locate = dict(
             username = ".//*[@id='account']",
             password = ".//*[@id='login-form']/form/table/tbody/tr[2]/td/input",
             login = ".//*[@id='submit']",
             new_project = ".//*[@id='projectbox']/div[2]/a[1]",
             logout = ".//*[@id='topnav']/a[1]",
             
             pro_name = ".//*[@id='name']",
             pro_code = ".//*[@id='code']",
             date_start = ".//*[@id='begin']",
             date_end = ".//*[@id='end']",
             AWD = ".//*[@id='days']",
             team_name = ".//*[@id='team']",
             #list table
             pro_type = ".//*[@id='type']",
             sprint = "//option[@value='sprint']",
             waterfall = "//option[@value='waterfall']",
             ops = "//option[@value='ops']",
             pro_des = "html",
             
             #checkbutton
             access_default = ".//*[@id='aclopen']",
             access_private = ".//*[@id='aclprivate']",
             access_wihte_name = ".//*[@id='aclcustom']",
             save = ".//*[@id='submit']",
             
             
             )