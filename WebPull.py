from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import JobSelection
import stateSelection
job = JobSelection.career_finder_quiz()
state = stateSelection.get_state_recommendation()
def linkList():
    query = f'site:linkedin.com/in "{job}" "{state}"'
    driver = webdriver.Chrome()
    driver.get('http://www.google.com')

    search = driver.find_element(By.NAME, 'q')
    search.send_keys(query)
    search.submit()

# RESULTS_LOCATOR = "//div/h3/a" # GIVING THE FIRST ONES ONLY

    RESULTS_LOCATOR = '//h3[starts-with(@class,"LC20lb")]/..'

    WebDriverWait(driver, 5).until( EC.visibility_of_element_located((By.XPATH, RESULTS_LOCATOR)))

    page_results = driver.find_elements(By.XPATH, RESULTS_LOCATOR)

    links = [element.get_attribute('href') for element in page_results]
    linkList = []
    for link in links:
        linkList.append(link)
        time.sleep(2)
    return linkList
