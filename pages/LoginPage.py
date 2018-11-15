# coding = utf-8
from common.pageObject import PageObject,PageElement
from common.url import *


class LoginPage(PageObject):
    base_url = Url().base_url
    url = base_url + '/login2'

    # login页面元素
    email = PageElement(id='inputEmail')
    passwd = PageElement(id='inputPassword')
