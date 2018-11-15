# coding = utf-8
from common.pageObject import PageObject,PageElement
from common.url import *


class LoginPage(PageObject):
    base_url = Url().base_url
    url = base_url

    # login页面元素
    input = PageElement(id='kw')
    passwd = PageElement(id='inputPassword')
