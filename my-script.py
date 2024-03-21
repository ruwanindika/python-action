from selenium import webdriver
from selenium.webdriver.common.by import By

def main():
    item_list = []

    driver=webdriver.Chrome()
    driver.get('https://devops1.com.au/')
    driver.maximize_window()

    
    service_list = driver.find_element(By.CSS_SELECTOR,'.dropdown-menu.show')
    
    for i in (service_list.text).splitlines():
        print(i)

if __name__ == "__main__":
  main()
