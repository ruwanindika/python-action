from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def main():
    item_list = []
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")

    driver=webdriver.Chrome(options=options)
    driver.get('https://devops1.com.au/')
    # driver.maximize_window()

    
    service_list = driver.find_element(By.CSS_SELECTOR,'.dropdown-menu.show')
    
    for i in (service_list.text).splitlines():
        print(i)

if __name__ == "__main__":
  main()
