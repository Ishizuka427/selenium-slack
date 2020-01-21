import time
import os
import dotenv
from selenium import webdriver

dotenv.load_dotenv(dotenv_path=".env")

WORKSPACE_NAME = os.environ["SUWA_SLACK_WORKSPACE_NAME"]
EMAIL = os.environ["SUWA_SLACK_EMAIL"]
PASSWORD = os.environ["SUWA_SLACK_PASSWORD"]
SEARCH_NAME = os.environ["SUWA_SLACK_SEARCH_NAME"]

driver = webdriver.Chrome(executable_path='./chromedriver')

driver.get('https://app.slack.com/client')
driver.find_element_by_css_selector("#domain").send_keys(WORKSPACE_NAME)
driver.find_element_by_id("submit_team_domain").click()
time.sleep(3)
driver.find_element_by_css_selector("#email").send_keys(EMAIL)
driver.find_element_by_css_selector("#password").send_keys(PASSWORD)
driver.find_element_by_id("signin_btn").click()
time.sleep(2)
driver.find_element_by_class_name("p-classic_nav__right_header").click()
time.sleep(1)
driver.find_element_by_xpath('//div[@aria-label="検索"]/p').send_keys(SEARCH_NAME)
time.sleep(1)
driver.find_element_by_id("c-search_autcomplete__suggestion_0").click()