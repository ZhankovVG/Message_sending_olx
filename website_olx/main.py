from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from decouple import config


output_file = 'user_links.txt'

driver = webdriver.Chrome()
user_links = []

try:
    driver.get('https://www.olx.ua/uk/')
    time.sleep(1)

    email = config('EMAIL')
    password = config('PASSWORD')

    klick_registration = driver.find_element(By.LINK_TEXT, "Ваш профіль").click()
    time.sleep(1)

    email_input = driver.find_element(By.NAME, 'username')
    email_input.clear()
    email_input.send_keys(email)
    time.sleep(1)

    paswword_input = driver.find_element(By.NAME, 'password')
    paswword_input.clear()
    paswword_input.send_keys(password)
    time.sleep(1)

    login_button = driver.find_element(By.CSS_SELECTOR, 'button.css-ypypxs').click()
    time.sleep(20)

    img_olx = driver.find_element(By.CSS_SELECTOR, 'span.css-1kpgv52').click()
    time.sleep(2)


    for _ in range(10):  
        
        driver.get('https://www.olx.ua/otdam-darom/')
        driver.refresh()
        time.sleep(7)

        block = driver.find_element(By.CLASS_NAME, 'css-odp1qd')        
        block.click()
        time.sleep(5)

        button_massage = driver.find_element(By.CLASS_NAME, 'css-xhd036').click()
        time.sleep(5)

        textarea_element = driver.find_element(By.NAME, 'message.text')
        textarea_element.send_keys("Доброго Дня")
        time.sleep(5)

        button_send = driver.find_element(By.CLASS_NAME, 'css-9x8rrm').click()
        time.sleep(5)
   
        current_url = driver.current_url
        user_links.append(current_url)
        time.sleep(5)


except Exception as ex:
    print(ex)    
finally:
    driver.close()
    driver.quit()


with open(output_file, 'w') as file:
    for link in user_links:
        file.write(link + '\n')