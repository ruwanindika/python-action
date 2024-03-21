from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains


def main():
    item_list = []
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")



    driver=webdriver.Chrome(options=options)
    driver.get('https://devops1.com.au/')
    # driver.maximize_window()
    
    toggle_link = driver.find_element(By.CSS_SELECTOR,'.nav-link.dropdown-toggle')
    ActionChains(context.driver).click(toggle_link).perform()
    
    service_list = driver.find_element(By.CSS_SELECTOR,'.dropdown-menu.show')
    
    for i in (service_list.text).splitlines():
        print(i)
        
    driver.close()

if __name__ == "__main__":
  main()
