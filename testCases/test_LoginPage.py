# coding=utf-8
from selenium import webdriver
import unittest
from time import sleep


class TestLogin(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        # 窗口最大化
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.close()

    def test_login_01(self):
        sleep(2)
        """
        测试登陆
        :return:
        """

