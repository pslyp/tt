from selenium import webdriver
import os

# CHROMEDRIVER_PATH = 'D:\Python\chromedriver'

if __name__ == '__main__':
    return ss()

def ss():
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--no-sandbox")
    driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), options=chrome_options)

    driver.get("https://www.google.com")
    # print(driver.page_source)
    return '{"status": 200}'