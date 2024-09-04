import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_constructor_button(register_and_login_user):
    driver = register_and_login_user

    personal_account = driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']")
    personal_account.click()

    constructor = driver.find_element(By.CSS_SELECTOR, "a[href='/']")
    constructor.click()

    logo = WebDriverWait(driver, 2).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']"))
    )

    assert logo.text == 'Соберите бургер'









