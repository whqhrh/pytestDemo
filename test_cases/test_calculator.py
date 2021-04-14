# -*- coding:utf-8 -*-
import os
import allure
import pytest
import yaml


@allure.feature('计算器')
class TestCalculator:

    @allure.story('加法运算')
    @pytest.mark.smoke
    @pytest.mark.run(oder=3)
    @allure.severity('noraml')
    def test_add(self, initcalc_class, get_add_datas):
        with allure.step('1.开始计算'):
            result = initcalc_class.add(get_add_datas[0], get_add_datas[1])
            allure.attach(f"计算结果:{result}",
                          attachment_type=allure.attachment_type.TEXT)
        with allure.step('2.断言：判断实际输出=预期结果'):
            expect = get_add_datas[2]
            allure.attach(f"实际结果：{result},预期结果：{expect}",
                          attachment_type=allure.attachment_type.TEXT)
            assert expect == result

    @allure.story('float加法')
    @pytest.mark.run(oder=2)
    @allure.severity('noraml')
    def test_add_float(self, initcalc_class, get_add_datas1):
        with allure.step('1.开始计算'):
            result = initcalc_class.add(get_add_datas1[0], get_add_datas1[1])
            result1 = round(result, 3)
            allure.attach(f"计算结果:{result1}",
                          attachment_type=allure.attachment_type.TEXT)
        with allure.step(f'2.断言：判断实际输出=预期结果'):
            expect = get_add_datas1[2]
            allure.attach(f"实际结果：{result1},预期结果：{expect}",
                          attachment_type=allure.attachment_type.TEXT)
            assert expect == result1

    @allure.story('除法运算')
    @pytest.mark.run(oder=1)
    @allure.severity('noraml')
    def test_div(self, initcalc_class, get_div_datas):
        try:
            with allure.step('1.开始计算'):
                result = initcalc_class.div(get_div_datas[0], get_div_datas[1])
                result1 = round(result, 3)
                allure.attach(f"计算结果:{result1}",
                              attachment_type=allure.attachment_type.TEXT)
            with allure.step(f'2.断言：判断实际输出=预期结果'):
                expect = get_div_datas[2]
                allure.attach(f"实际结果：{result1},预期结果：{expect}",
                              attachment_type=allure.attachment_type.TEXT)
                assert expect == result1
        except ZeroDivisionError as e:
            print(f'出现错误{e},被除数为0，无法计算，测试通过')


if __name__ == "__main__":
    pytest.main()
    os.system(r'allure generate ../outputs/results  -o ../outputs/reports --clean')
