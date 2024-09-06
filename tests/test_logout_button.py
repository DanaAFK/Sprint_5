import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestLogoutButton:
    def test_logout_button(self, register_and_login_user):
        driver = register_and_login_user

        personal_account = driver.find_element(By.XPATH, Locators.PERSONAL_ACC_BUTTON)
        personal_account.click()

        logout_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, Locators.LOG_OUT_BUTTON))
        )
        logout_button.click()

        aut_login = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.LOGIN_HEADER))
        )

        assert aut_login.text == 'Вход'