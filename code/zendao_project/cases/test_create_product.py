# coding:utf-8
__author__ = "TanSx"
import time
import unittest
from  common.page import Login
from common import model
from config.locator import PO_locate
from selenium.common import exceptions as EC
import datetime
import random


class Product(unittest.TestCase):
    '''产品测试'''

    def setUp(self):
        self.page = Login()
        self.params = self.init_params()

    def init_params(self):
        params = dict(
            name="ZoneDirector",
            code="odc-001",
            des=" This is product descriptions!",
        )
        return params

    def tearDown(self):
        self.page.quit()

    def click_action(self, locate, how="xpath"):
        try:
            if self.page.is_element_present(how, locate):
                self.page.driver.find_element_by_xpath(locate).click()
        except EC.NoSuchElementException as e:
            raise e

    def sendkey_action(self, locate, name, how="xpath"):
        if self.page.is_element_present(how, locate):
            time.sleep(1)
            self.page.driver.find_element_by_xpath(locate).clear()
            self.page.driver.find_element_by_xpath(locate).send_keys(name)

    def delete_product_is_exist(self, name):
        '''删除已经存在同名的产品'''
        time.sleep(1)
        self.click_action(PO_locate["product"])
        time.sleep(1)
        self.click_action(PO_locate["currentItem"])
        time.sleep(1)
        self.sendkey_action(PO_locate["serachItem"], name)
        time.sleep(1)

        if self.page.is_element_present("xpath", PO_locate["Item"]):
            e3 = self.page.driver.find_element_by_xpath(PO_locate["Item"])  # 匹配结果
            print(e3.text)
            if e3.text == name:  # 判断是否找到项目
                self.click_action(PO_locate["all_product"])
                for i in range(10):
                    xpath = ".//*[@id='productTableList']/tr[" + str(i) + "]/td[2]/a"
                    print xpath
                    if self.page.is_element_present("xpath", xpath):
                        if self.page.driver.find_element_by_xpath(xpath).text == name:  # 查找产品
                            self.click_action(xpath)  # 点击产品名称
                            if self.click_action(PO_locate["delete_product"]):  # 点击删除
                                if self.page.is_alert_present():
                                    print("点击确认, 删除!")
                                    time.sleep(1)
                                    res = self.page.close_alert_and_get_its_text()
                                    model.logger_init().info("res:" + res)
                                    break
                        else:
                            continue
        else:
            print("not found %s" % (PO_locate["Item"]))

    def _serach_product(self, name):
        '''搜索产品'''
        time.sleep(1)
        self.click_action(PO_locate["product"])
        time.sleep(1)
        self.click_action(PO_locate["currentItem"])
        time.sleep(1)
        self.sendkey_action(PO_locate["serachItem"], name)
        time.sleep(1)

        if self.page.is_element_present("xpath", PO_locate["Item"]):
            e3 = self.page.driver.find_element_by_xpath(PO_locate["Item"])  # 匹配结果
            print(e3.text)
            if e3.text == name:  # 判断是否找到项目
                e3.click()
                model.logger_init().info(u"产品已被找到")
                return True
            else:
                model.logger_init().ERROR(u"该产品未添加")
                return False
        else:
            print("not found %s" % (PO_locate["Item"]))

    def _create_product(self):

        # 判断该产品是否已经存在，如果存在则先删除。
        self.delete_product_is_exist(self.params["name"])
        # Product
        time.sleep(2)
        self.click_action(PO_locate["product"])
        time.sleep(1)
        self.page.driver.find_element_by_xpath(".//*[@id='submenucreate']").click()
        time.sleep(1)
        # Product name
        self.sendkey_action(PO_locate["name"], self.params["name"])
        # product code
        self.sendkey_action(PO_locate["code"], self.params["code"])
        # product owner
        self.click_action(PO_locate["PO_chosen"])
        time.sleep(1)
        # select owner
        self.click_action(PO_locate["PO_owner"])
        time.sleep(1)
        # Test owner
        self.click_action(PO_locate["QD_chosen"])
        # select test owner
        self.click_action(PO_locate["test_owner"])
        # public owner
        self.click_action(PO_locate["RD_chosen"])
        # select public owner
        self.click_action(PO_locate["select_RD_chosen"])
        # product discription
        self.sendkey_action(PO_locate["product_des"], self.params["des"])
        # check access control
        self.click_action(PO_locate["access_private"])
        # save
        self.click_action(PO_locate["save"])
        model.logger_init().info(u'产品创建成功')


class product_publish(Product):
    '''[发布]产品发布测试'''

    def setUp(self):
        Product.setUp(self)
        model.logger_init().info(u'产品发布测试开始')

    def tearDown(self):
        Product.tearDown(self)
        model.logger_init().info(u'产品发布测试结束')

    def test_06_create_product_publish(self):
        '''创建产品发布'''

        conf = dict(
            relase=".//*[@id='submenurelease']",
            cre_publish=".//*[@id='titlebar']/div[2]/a",
            select_version=".//*[@id='build_chosen']/a",
            name=".//*[@id='name']",
            date=".//*[@id='date']",
            des=".//*[@id='dataform']/table/tbody/tr[4]/td/div/div[2]/iframe",
            fileBox=".//*[@id='fileBox1']/tbody/tr/td[1]/div/input",
            save=".//*[@id='submit']",
        )

        data = dict(
            po_name="ZoneDirector",
            name="ZD",
            version="1001",
            date="2017-01-30",
            description=u"发布产品测试验证",
            file="D:\\ui.rar",

        )

        if self._serach_product(data["po_name"]):  # 查找产品
            self.click_action(conf['relase'])
            self.click_action(conf['cre_publish'])
            self.sendkey_action(conf['name'], data['name'])
            if self.page.is_element_present("xpath", conf['select_version']):
                self.page.driver.find_element_by_xpath(conf['select_version']).send_keys(data['version'])
            self.sendkey_action(conf['date'], data['date'])
            if self.page.is_element_present("xpath", conf['des']):
                self.page.driver.find_element_by_xpath(conf['des']).send_keys(data['description'])
            if self.page.is_element_present("xpath", conf["fileBox"]):
                self.page.driver.find_element_by_xpath(conf["fileBox"]).send_keys(data['file'])
            self.click_action(conf['save'])
            model.logger_init().info(u"产品发布成功")

        else:
            self._create_product()  # 创建产品
            self.click_action(conf['relase'])
            self.click_action(conf['cre_publish'])
            self.sendkey_action(conf['name'], data['name'])
            if self.page.is_element_present("xpath", conf['select_version']):
                self.page.driver.find_element_by_xpath(conf['select_version']).send_keys(data['version'])
            self.sendkey_action(conf['date'], data['date'])
            if self.page.is_element_present("xpath", conf['des']):
                self.page.driver.find_element_by_xpath(conf['des']).send_keys(data['description'])
            if self.page.is_element_present("xpath", conf["fileBox"]):
                self.page.driver.find_element_by_xpath(conf["fileBox"]).send_keys(data['file'])
            self.click_action(conf['save'])
            model.logger_init().info(u"产品发布成功")


class create_product(Product):
    '''[产品]产品创建测试'''

    def setUp(self):
        Product.setUp(self)
        model.logger_init().info(u'产品创建测试开始')

    def tearDown(self):
        Product.tearDown(self)
        model.logger_init().info(u'产品创建测试结束')

    def test_02_delete_product(self):
        '''删除产品'''
        self.delete_product_is_exist(self.params["name"])

    def test_01_create_product(self):
        '''创建产品'''
        self._create_product()

    def test_03_select_product(self):
        '''查找产品'''
        name = "ZoneDirector"
        self._serach_product(name)


class product_document(Product):
    '''[文档]产品文档测试'''

    def setUp(self):
        Product.setUp(self)  # 继承父类构造函数
        self.name = "ZoneDirector"
        self.locate = dict(
            click_doc=".//*[@id='submenudoc']",
            cre_doc=".//*[@id='titlebar']/div[2]/a",
            doc_type=".//*[@id='typefile']",  # 文件
            doc_type_1=".//*[@id='typeurl']",  # 链接
            doc_type_2=".//*[@id='typetext']",  # 网页

            title=".//*[@id='title']",  # 文档标题
            key=".//*[@id='keywords']",  # 关键字
            digst=".//*[@id='digest']",  # 文档摘要
            fixBox=".//*[@id='fileBox1']/tbody/tr/td[1]/div/input",  # 上传附件
            fixBox_title=".//*[@id='fileBox1']/tbody/tr/td[2]/input",  # 附件标题
            doc_url=".//*[@id='url']",
            doc_description=".//*[@id='contentBox']/td/div/div[2]/iframe",
            save=".//*[@id='submit']",
        )

        self.data = dict(
            title=time.time()
        )
        model.logger_init().info(u'产品文档用例测试开始')

    def tearDown(self):
        Product.tearDown(self)
        model.logger_init().info(u'产品文档用例测试结束')

    def test_07_create_product_document_fileType(self):
        '''创建文件类型的产品文档'''

        if self._serach_product(self.name):
            self.click_action(self.locate["click_doc"])
            self.click_action(self.locate['cre_doc'])
            self.click_action(self.locate['doc_type'])
            self.sendkey_action(self.locate['title'], u'文章' + str(self.data['title']))
            self.sendkey_action(self.locate['key'], u"用户类型")
            self.sendkey_action(self.locate['digst'], u'语言')

            # 上传附件
            if self.page.is_element_present("xpath", self.locate['fixBox']):
                self.page.driver.find_element_by_xpath(self.locate['fixBox']).send_keys('D:\\ui.rar')
            if self.page.is_element_present("xpath", self.locate['fixBox_title']):
                self.page.driver.find_element_by_xpath(self.locate['fixBox_title']).send_keys(u'代码1')

            # 保存
            self.click_action(self.locate['save'])
        else:
            msg = u'产品没有创建，或查找失败，请确认！'
            raise msg

    def test_08_create_product_document_linkType(self):
        '''创建链接类型文档'''
        if self._serach_product(self.name):
            self.click_action(self.locate["click_doc"])
            self.click_action(self.locate['cre_doc'])
            self.click_action(self.locate['doc_type_1'])
            self.sendkey_action(self.locate['title'], u'文章' + str(self.data['title']))
            if self.page.is_element_present("xpath", self.locate['doc_url']):
                self.page.driver.find_element_by_xpath(self.locate['doc_url']).send_keys("http://www.baidu.com")
            self.sendkey_action(self.locate['digst'], u'界面')
            # 保存
            self.click_action(self.locate['save'])
        else:
            msg = u'产品没有创建，或查找失败，请确认！'
            raise msg

    def test_09_create_product_document_webType(self):
        '''创建网
        页类型文档'''
        if self._serach_product(self.name):
            self.click_action(self.locate["click_doc"])
            self.click_action(self.locate['cre_doc'])
            self.click_action(self.locate['doc_type_2'])
            self.sendkey_action(self.locate['title'], u'文章' + str(self.data['title']))
            # 文档描述
            if self.page.is_element_present("xpath", self.locate['doc_description']):
                self.page.driver.find_element_by_xpath(self.locate['doc_description']).send_keys(u"这是第一篇产品文档描写，并没有写什么")
            self.sendkey_action(self.locate['key'], u"产品类型")
            self.sendkey_action(self.locate['digst'], u'界面')
            # 保存
            self.click_action(self.locate['save'])
        else:
            msg = u'产品没有创建，或查找失败，请确认！'
            raise msg


class product_plan(Product):
    '''[计划]产品计划测试'''

    def setUp(self):
        Product.setUp(self)
        model.logger_init().info(u'产品计划测试开始')

    def tearDown(self):
        Product.tearDown(self)
        model.logger_init().info(u'产品计划测试结束')

    def test_04_create_product_plan(self):
        '''创建产品计划'''
        conf = dict(
            po_plan=".//*[@id='submenuplan']",
            cre_plan=".//*[@id='titlebar']/div[2]/a",
            name=".//*[@id='title']",
            start=".//*[@id='begin']",
            end=".//*[@id='end']",
            check=".//*[@id='dataform']/table/tbody/tr[4]/td[2]/label[1]",
            des=".//*[@id='dataform']/table/tbody/tr[5]/td/div/div[2]/iframe",  # 项目描述
            save=".//*[@id='submit']"
        )

        data = dict(
            po_name="ZoneDirector",
            name=u"交换设备",
            s_t="2017-01-01",
            e_t="2017-02-01",
            description=u"产品计划，要求一星期内完成"
        )

        def _create_plan(conf, data):
            self.click_action(conf['po_plan'])
            self.click_action(conf['cre_plan'])
            self.sendkey_action(conf['name'], data["name"])

            self.sendkey_action(conf['start'], data['s_t'])
            self.sendkey_action(conf['end'], data['e_t'])
            self.click_action(conf['check'])
            # self.sendkey_action(conf['des'], data['description'])
            if self.page.is_element_present("xpath", conf["des"]):
                self.page.driver.find_element_by_xpath(conf["des"]).send_keys(data['description'])
            self.click_action(conf['save'])
            model.logger_init().info(u"产品计划已经创建成功")

        # step 1
        if self._serach_product(data["po_name"]):  # 查找产品
            _create_plan(conf, data)  # 创建计划
        else:
            self._create_product()  # 创建产品
            _create_plan(conf, data)  # 创建计划

    '''
        设置产品计划周期为1星期
    '''

    def test_05_create_product_plan_use_period(self):
        '''产品计划设置周期'''
        '''创建产品计划'''
        conf = dict(
            po_plan=".//*[@id='submenuplan']",
            cre_plan=".//*[@id='titlebar']/div[2]/a",
            name=".//*[@id='title']",
            start=".//*[@id='begin']",
            end=".//*[@id='end']",
            check=".//*[@id='dataform']/table/tbody/tr[4]/td[2]/label[1]",
            des=".//*[@id='dataform']/table/tbody/tr[5]/td/div/div[2]/iframe",  # 项目描述
            save=".//*[@id='submit']"
        )

        data = dict(
            po_name="ZoneDirector",
            name=u"交换设备",
            s_t="2017-01-01",
            e_t="2017-02-01",
            description=u"产品计划，要求一星期内完成"
        )

        def _set_time(conf, data):
            self.click_action(conf['po_plan'])
            self.click_action(conf['cre_plan'])
            # step 3
            self.sendkey_action(conf['name'], data["name"] + str(random.randrange(1000)))

            self.sendkey_action(conf['start'], data['s_t'])
            self.sendkey_action(conf['end'], data['e_t'])
            self.click_action(conf['check'])
            res = self.page.driver.find_element_by_xpath(conf['end']).get_attribute('value')
            print("res:" + res)
            d1 = datetime.datetime.strptime(data["s_t"], '%Y-%m-%d')
            d2 = datetime.datetime.strptime(res, '%Y-%m-%d')
            delt = d2 - d1
            print(delt)
            if delt.days == 7:
                model.logger_init().info(u'计划周期设置为一星期')

            if self.page.is_element_present("xpath", conf["des"]):
                self.page.driver.find_element_by_xpath(conf["des"]).send_keys(data['description'])
            self.click_action(conf['save'])
            model.logger_init().info(u"产品计划已经创建成功")

        if self._serach_product(data["po_name"]):  # 查找产品
            _set_time(conf, data)  # 创建计划
        else:
            self._create_product()  # 创建产品
            _set_time(conf, data)  # 创建计划


if __name__ == '__main__':
    Product()
