import time
from selenium import webdriver
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.support.expected_conditions import staleness_of
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

# Create a new instance of the chrome driver with desired capabilities
dc = DesiredCapabilities.CHROME
dc['loggingPrefs'] = {'browser': 'ALL'}
chrome_profile = webdriver.ChromeOptions()
# change default_directory
profile = {"download.default_directory": "C:\\Users\\x\\Downloads\\",
           "download.prompt_for_download": False,
           "download.directory_upgrade": True}

chrome_profile.add_experimental_option("prefs", profile)
chrome_profile.add_argument("--disable-extensions")
driver = webdriver.Chrome(executable_path="C:\\Users\\x\\Downloads\\chromedriver.exe", chrome_options=chrome_profile,service_args=["--log-path=C:\\Users\\vadim\\Downloads\\chromedriver.log"],  desired_capabilities=dc)
# go to the FS page
driver.get("https://familysearch.org/ark:/61903/3:1:3Q9M-CS97-T9WN-N?i=66&cat=834000")
while True:
    # grab the data
    # click next link
    try:
        driver.find_element_by_xpath("//*[@id='saveLi']/a").click()
        element = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH,"//span[@class='next pager-icon fs-civ-circle-chevron-right enabled']")))
        element.click()
        print "Ready"
        time.sleep(30)
    except TimeoutException:
        break