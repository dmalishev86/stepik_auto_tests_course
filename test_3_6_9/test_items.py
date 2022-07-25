from selenium.webdriver.common.by import By
import time

link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"


def test_find_add_to_basket_button(browser):
    browser.get(link)
    time.sleep(2)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn-add-to-basket")
    assert button.is_displayed(), ('No button :(')
    print(f'----------> Button name: {button.text}')
    print(f'----------> Button language: {browser.find_element(By.CSS_SELECTOR, "option[selected]").text}')

# команда для запуска: pytest -s -v --language=fr test_items.py
