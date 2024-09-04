import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

def test_logout_button(register_and_login_user):
    driver = register_and_login_user

    personal_account = driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']")
    personal_account.click()

    logout_button = WebDriverWait(driver, 10).until(
        expected_conditions.element_to_be_clickable((By.XPATH, "//button[contains(., 'Выход')]"))
    )
    logout_button.click()

    aut_login = WebDriverWait(driver, 2).until(
        expected_conditions.visibility_of_element_located((By.XPATH, "//h2[text()='Вход']"))
    )

    assert aut_login.text == 'Вход'