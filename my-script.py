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

    
    service_list = driver.find_element(By.XPATH,'//dev[@class="section-intro"]//h2[@class="display-3 text-white"]').text
    
    print(f"---->>>>> {service_list}")
        
    driver.close()

if __name__ == "__main__":
  main()
