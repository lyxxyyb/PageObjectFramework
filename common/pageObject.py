# coding = utf8
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


POSITIONING_ELEMENT = {
    "id": By.ID,
    "css": By.CSS_SELECTOR,
    "xpath": By.XPATH,
    "name": By.NAME,
    "tag_name": By.TAG_NAME,  #通过元素的标签名称来查找元素
    "class_name": By.CLASS_NAME,  # 利用元素的css样式表所引用的伪类名称进行元素查找
    "link_text": By.LINK_TEXT,  # 通过链接文字进行匹配
    "part_link_text": By.PARTIAL_LINK_TEXT,  # 通过部分链接文字进行匹配
}


class PageObject(object):
    def __init__(self, webdriver, root_uri=None):
        self.driver = webdriver
        self.root_uri = root_uri if root_uri else getattr(self.driver, "root_uri", None)
        """getattr(object, attribute, default)"""

    def get(self, uri):
        """
        :param uri: URL to GET
        :return:
        """
        root_uri = self.root_uri or None
        self.driver.get(root_uri + uri)


class PageElement(object):
    def __init__(self, position, context=None):
        """
        :param context:  send_keys()传入值
        :param position:  find_element_by_* 参数定位方式
        """
        if position not in POSITIONING_ELEMENT:
            raise ValueError("Please enter right positioning element method")

    def find(self):
        return




