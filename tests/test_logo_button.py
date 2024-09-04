import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_logo_button(register_and_login_user):
    driver = register_and_login_user

    personal_account = driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']")
    personal_account.click()

    logo_button = driver.find_element(By.XPATH, "//*[name()='svg' and @xmlns='http://www.w3.org/2000/svg']")
    logo_button.click()

    logo = WebDriverWait(driver, 10).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//h1[text()='Соберите бургер']"))
    )

    assert logo.text == 'Соберите бургер'