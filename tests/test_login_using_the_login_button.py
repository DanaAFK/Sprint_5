import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_login_using_the_login_button():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    login_in_form_button = driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']")
    login_in_form_button.click()

    email = driver.find_element(By.XPATH,  "//label[text()='Email']/following-sibling::input[@type='text']")
    email.send_keys("fairy_4@mail.com")

    password = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input[@type='password']")
    password.send_keys("ILoveMinions098")

    login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    login_button.click()

    place_in_order = WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
    )

    assert place_in_order.text == "Оформить заказ"

    driver.quit()
