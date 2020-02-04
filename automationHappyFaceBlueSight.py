from selenium.webdriver import Firefox
from selenium.webdriver.firefox.options import Options
import config_cognos
from password_handler import password, password_test
from time import sleep
from selenium.webdriver.firefox.options import Options

def happy_face(password, headless=False):

	opt = Options()
	opt.headless=headless
	driver = Firefox(options=opt)
	driver.implicitly_wait(30)
	driver.get('https://www.bluesight.io/')
	driver.find_element_by_class_name('btn-primary').click()
	driver.find_element_by_id('username').send_keys(config_cognos.email)
	driver.find_element_by_id('continue-button').click()
	driver.find_element_by_id('desktop').send_keys(config_cognos.email)
	driver.find_element_by_name('password').send_keys(password)
	sleep(5)
	driver.find_element_by_id('btn_signin').click()
	sleep(25)
	driver.find_element_by_class_name('pl-4').click()
	driver.find_element_by_css_selector('.fa-smile-o').click()
	driver.find_element_by_css_selector('div.text-center:nth-child(4) > div:nth-child(1) > img:nth-child(1)').click()
	driver.find_element_by_css_selector('#createMoodModal > div:nth-child(1) > div:nth-child(1) > div:nth-child(3) > div:nth-child(1) > button:nth-child(2)').click()
	driver.quit()
	

if __name__ == '__main__':

	password = password_test(hash_key=config_cognos.password_hash)
	happy_face(password)