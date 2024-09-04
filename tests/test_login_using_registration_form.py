import pytest
import selenium
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_login_and_order(register_user):
    driver = register_user

    email = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']")
    email.send_keys("fairy_1@mail.com")

    password = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input[@type='password']")
    password.send_keys("ILoveMinions098")

    login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    login_button.click()

    place_in_order = WebDriverWait(driver, 20).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']"))
    )

    assert place_in_order.text == "Оформить заказ"

