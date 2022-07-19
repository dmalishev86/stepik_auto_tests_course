from selenium import webdriver
from selenium.webdriver.common.by import By
import time, os

try:
    browser = webdriver.Chrome()
    browser.get('http://suninjuly.github.io/file_input.html')

    browser.find_element(By.NAME, 'firstname').send_keys('Name')
    browser.find_element(By.NAME, 'lastname').send_keys('LName')
    browser.find_element(By.NAME, 'email').send_keys('Email@email.com')

    current_dir = os.path.abspath(os.path.dirname(__file__))  # получаем путь к директории текущего исполняемого файла
    file_path = os.path.join(current_dir, 'test.txt')  # добавляем к этому пути имя файла
    browser.find_element(By.ID, 'file').send_keys(file_path)

    browser.find_element(By.CSS_SELECTOR, "button.btn").click()
finally:
    # ожидание чтобы визуально оценить результаты прохождения скрипта
    time.sleep(3)
    # закрываем браузер после всех манипуляций
    browser.quit()