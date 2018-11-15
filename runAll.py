import unittest
import HTMLTestRunner


def get_test_cases(dirpath):
    test_cases = unittest.TestSuite()
    suites = unittest.defaultTestLoader.discover(dirpath, 'Test_*.py', top_level_dir=dirpath)
    for suite in suites:
        test_cases.addTests(suite)
    return test_cases


if __name__ == '__main__':
    cases = get_test_cases('test')
    filename = 'report/testReport.html'  # 设置报告文件名
    f = open(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=f, title=u'mooctest', description=u'详细测试结果如下:')
    runner.run(cases)
'''
import unittest

test_dir='./'
discover=unittest.defaultTestLoader.discover(test_dir,pattern='Test_*.py')

if __name__=='__main__':
    runner=unittest.TextTestRunner()
    runner.run(discover)
    '''