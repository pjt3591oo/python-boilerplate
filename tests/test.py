from tests import url, test_example
import unittest


def makeSuite(testcase, tests):
    return unittest.TestSuite(map(testcase, tests))  # testcase를 이용해서 testsuite생성


if __name__ == '__main__':
    print('tests start~')

    url_suite = makeSuite(url.url, [
        'test_case1'
    ])

    test_package_suite = makeSuite(test_example.test_package1, [
        'test_case1',
        'test_case2'
    ])

    allsuites = unittest.TestSuite([
        url_suite,
        test_package_suite
    ])  # 모든 testsuite를 묶음

    unittest.TextTestRunner(verbosity=2).run(allsuites)  # 모든 tests suite를 수행