from  selenium import webdriver
import time
from  selenium.webdriver.common.action_chains import ActionChains   # 动作链
from selenium.webdriver.common.by import By
driver=webdriver.Edge()
driver.implicitly_wait(15)
driver.get("https://www.suning.com/")
driver.find_element(By.ID,"searchKeywords").send_keys("华为 WATCH GT Runner")
driver.find_element(By.ID,"searchSubmit").click()
driver.find_element(By.XPATH,"//*[@id='ssdsn_search_pro_baoguang-1-0-1_1_02:0000000000_12342279129']/i/img").click()  # 相对定位值可能会有问题
'''
用例：功能
数据：华为 WATCH GT Runner 功能
定位元素
'''
#元素定位不到该如何解决 1.先确定自己的定位方式的值对不对  2.frame/alert/window 切换   3. 加载慢 → 等待
a=driver.window_handles  #获取窗口
driver.switch_to.window(a[1])
driver.find_element(By.ID,"addCart").click()
driver.find_element(By.XPATH,"/html/body/div[38]/div/div[2]/div/div[1]/a").click()
driver.find_element(By.XPATH,"//*[@id='cart-one-delivery']/div[2]/p/a").click()

time.sleep(2)
driver.switch_to.frame("iframeLogin")
try:
    driver.find_element(By.ID,"userName").send_keys("123")
    driver.find_element(By.ID, "password").send_keys("123")
    time.sleep(2) # 稍等一下滑块
    huakuan = driver.find_element(By.CLASS_NAME,"dt_child_content_knob")
    ac= ActionChains(driver)
    ac.click_and_hold(huakuan).move_by_offset(300,300).perform()
    ac.release()
    driver.find_element(By.ID, "submit").click()
    driver.save_screenshot("error1.png")
except Exception as e:
    print(e)
    driver.save_screenshot("error.png")
finally:
    time.sleep(5)
    driver.quit()



