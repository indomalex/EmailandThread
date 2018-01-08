#coding:utf-8
import time
from selenium import webdriver


def openBaidu():
    #做在firfox上的自动化测试最最基础版,试一试水
    driver = webdriver.Firefox()
    driver.get("http://baike.baidu.com")
    driver.maximize_window()
    driver.find_element_by_id("query").send_keys("比亚迪唐")
    driver.find_element_by_id("search").click()
    time.sleep(6)
    driver.close()


if __name__ == "__main__":
    openBaidu()
    print("OK！")
