from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

if __name__ == "__main__" :
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('headless')
    chrome_options.add_argument('--disable-gpu')
    chrome_options.add_argument('lang=ko_KR')

    driver = webdriver.Firefox(executable_path='C:/Users/user/Downloads/geckodriver.exe')
    driver.get('https://www.haxball.com/play')
    driver.implicitly_wait(3)
    driver.switch_to.frame(driver.find_element(By.XPATH, '/html/body/div/div[2]/iframe'))
    q = driver.find_element(By.XPATH, '/html/body/div/div/div/div/input')
    q.send_keys('인사봇', Keys.ENTER)
    # for i in range(6):
    #     driver.execute_script("window.open('');")
    #     windows = driver.window_handles
    #     driver.switch_to.window(windows[i+1])
    #     driver.get('https://www.haxball.com/play')
    #     driver.implicitly_wait(3)
    #     driver.switch_to.frame(driver.find_element(By.XPATH, '/html/body/div/div[2]/iframe'))
    #     q = driver.find_element(By.XPATH, '/html/body/div/div/div/div/input')
    #     q.send_keys(Keys.ENTER)
    # aa=input()
    # windows = driver.window_handles
    # for i in range(5):
    #     driver.switch_to.window(windows[i])
    #     driver.find_element(By.XPATH,aa).click()
    #     driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div/div[2]/button[2]').click()
    ss=1
    while True:
        a=input()
        spec=driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/div/div[2]/div[3]/div[2]')
        red=driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/div/div[2]/div[2]/div[2]')
        blue=driver.find_element(By.XPATH,'/html/body/div/div/div[1]/div/div/div[2]/div[4]/div[2]')

        s=spec.text.split('\n')
        r=red.text.split('\n')
        b=blue.text.split('\n')
        lst=s+r+b
        n_lst=[]
        t=0
        if lst[0]=='0':
            t=1
        for i in range(t,len(lst),2):
            n_lst.append(lst[i])
        if ss!=0:

            ipt=driver.find_element(By.XPATH,'/html/body/div/div/div[2]/div[2]/div[3]/input')
            for i in n_lst:
                 ipt.send_keys(i+'님 안녕하세요!',Keys.ENTER)
        else:
            ss+=1
