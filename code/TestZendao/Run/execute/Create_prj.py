'''
    #name: Create_prj.py
    #function: Login web and create an project
    #autor: tsx
    #date: 2015-11-14
'''

from  LoginZendao import login
from  CreateAnProject import create_an_project
import time


def init_data():
	conf = {'pro_name': '9.14_zonedirector_test',
	        'pro_code': 'odc-0005',
	        'date_start': '2015-11-14',
	        'date_end': '2015-11-30',
	        'avilable_work_days': '16',
	        'team_name': 'automation',

	        'pro_type': 'ops',
	        'pro_des': "hello automation, congratulation to your",
	        'pro_access': 'access_private',

	        }
	return conf


def main():
	conf = init_data()
	prj_name = conf['pro_name']
	prj_code = conf['pro_code']
	date_start = conf['date_start']
	date_end = conf['date_end']
	awd = conf['avilable_work_days']
	team_name = conf['team_name']
	prj_type = conf['pro_type']
	prj_des = conf['pro_des']
	prj_access = conf['pro_access']

	# login zendao
	br = login()
	driver = br.login_browser()

	time.sleep(8)
	#     import pdb
	#     pdb.set_trace()
	create_an_project(driver, prj_name, prj_code, date_start, date_end, awd, team_name, prj_type, prj_des, prj_access)


if __name__ == "__main__":
	main()
