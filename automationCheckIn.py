from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
from time import sleep
import sys
import config_cognos
from password_handler import *
    




def check_in(password, headless=False):
    opt = Options()
    opt.headless=headless

    driver = Firefox(options=opt)
    driver.get('https://dbs.w3ibm.mybluemix.net/desks')
    login = driver.find_element_by_class_name('desktop')
    login.send_keys(config_cognos.email)
    passwordField = driver.find_elements_by_name('password')
    passwordField[0].send_keys(password)
    btn = driver.find_element_by_id('btn_signin')
    btn.click()
    sleep(30)
    driver.implicitly_wait(45)
    baia = driver.find_element_by_css_selector('path.bayKey\.CG01:nth-child(1)')
    baia.click()
    btn2 = driver.find_element_by_css_selector('.btn-ibm')
    btn2.click()
    driver.quit()


if __name__=='__main__':
    password = password_test(hash_key=config_cognos.password_hash)
    check_in(password)