# coding=utf-8
from selenium import webdriver
import unittest
from time import sleep
from pages.LoginPage import *


class TestLogin(unittest.TestCase):
    # def setUp(self):
    #     self.driver = webdriver.Chrome()
    #     # 窗口最大化
    #     self.driver.maximize_window()
    #
    # def tearDown(self):
    #     self.driver.close()
    #
    # def test_login_01(self):
    #     sleep(2)
    #     """
    #     测试登陆
    #     :return:
    #     """
    def setUp(self):
        self.driver = None

    def tearDown(self):
        self.driver.close()

    def function_initial(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.page = LoginPage(self.driver)

    # TestCase1-03
    # 输入正确的用户名、密码并点击登录
    def test_01_login_success(self):
        # 学生教师账户各登一次
        list = User().users
        for user in list:
            self.function_initial()
            self.driver.get(self.page.url)
            self.page.email = user['email']
            self.page.passwd = user['passwd']
            self.page.btn.click()
            sleep(1)
            self.assertIn(user['username'], self.driver.page_source)
            # 判断主页中的菜单、任务广场、侧边栏等部分是否加载成功
            navbar = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.navbar.navbar_css)))
            # task = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.user_main.task_css)))
            sidebar = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, self.user_main.sidebar_css)))
            # print(navbar.text)
            sleep(2)
            if user['role'] == '学生':
                self.assertEqual('首页\n练习\n考试\n班级\n学生', navbar.text)
            else:
                self.assertEqual('首页\n题库\n试卷\n练习\n考试\n比赛\n班级\n教师', navbar.text)
            self.assertEqual('大赛官网\n慕测论坛\n工具下载\n使用帮助\n大赛入口\n成为教师', sidebar.text)

    # TestCase1-04
    # 输入错误的密码并点击登录
    def test_02_login_wrong_passwd(self):
        user = User().user_wrong_pwd
        self.function_initial()
        self.driver.get(self.page.url)
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        sleep(1)
        self.assertEqual("密码错误", self.page.passwd_error.text)
        self.assertEqual(self.page.url, self.driver.current_url)

    # TestCase1-05
    # 输入尚未注册的用户名并点击登录
    def test_03_login_not_register(self):
        user = User().user_no_register
        self.function_initial()
        self.driver.get(self.page.url)
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        sleep(1)
        self.assertEqual("登录失败,请检查账户名密码", self.page.email_error.text)
        self.assertEqual(self.page.url, self.driver.current_url)

    # TestCase1-06
    # 对完善信息的用户进行登录
    def test_04_login_full_info(self):
        user = User().user_stu
        self.function_initial()
        self.driver.get(self.page.url)
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        sleep(1)
        print(self.driver.current_url)
        # current_url = self.driver.current_url
        # self.page.get('/user/info')
        # sleep(1)
        # if self.user_info.school.text != '' and self.user_info.phone.text != '':
        # 完善信息的用户登陆后应该是大赛页面
        #     self.assertEqual("http://www.mooctest.net/contest/list",current_url)
        # else:
        #     print('未完善用户信息！')

    # TestCase1-07
    # 对未完善信息的用户进行登录
    def test_05_login_uncomplete_info(self):
        user = User().user_uncomlete_info
        self.function_initial()
        self.driver.get(self.page.url)
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        sleep(1)
        print(self.driver.current_url)
        # current_url = self.driver.current_url
        # self.page.get('/user/info')
        # sleep(1)
        # if self.user_info.school.text == '' or self.user_info.phone.text == '':
        #     self.assertEqual("http://www.mooctest.net/usr/info",current_url)
        # else:
        #     print('用户信息已完善！')

    # TestCase1-08 & TestCase1-09
    # 登录后点"参加考试",再退出登录返回登录界面
    # 再次登录，进入退出前的参加考试界面
    def test_06_join_exam_logout(self):
        user = User().user_stu
        self.function_initial()
        self.driver.get(self.page.url)
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        sleep(1)
        self.navbar.exam_s.click()
        self.navbar.join_exam_s.click()
        sleep(2)
        self.assertEqual(self.exam_list.exam_url, self.driver.current_url)
        self.navbar.head_img.click()
        sleep(1)
        self.navbar.logout.click()
        sleep(1)
        self.assertEqual(self.page.url, self.driver.current_url)
        self.page.email = user['email']
        self.page.passwd = user['passwd']
        self.page.btn.click()
        sleep(1)
        self.assertEqual(self.exam_list.exam_url, self.driver.current_url)



if __name__ == "__main__":
        unittest.main()

