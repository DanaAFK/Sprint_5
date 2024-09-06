import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Data

class TestPersonalAcc:
    def test_personal_account_open(self, register_user):
        driver, generated_email = register_user

        email_field = driver.find_element(By.XPATH, Locators.EMAIL_FIELD)
        email_field.send_keys(Data.VALID_EMAIL)

        password_field = driver.find_element(By.XPATH, Locators.PASSWORD_FIELD)
        password_field.send_keys(Data.USER_PASSWORD)

        login_button = driver.find_element(By.XPATH, Locators.LOGIN_BUTTON)
        login_button.click()

        WebDriverWait(driver, 20).until(
            EC.element_to_be_clickable((By.XPATH, Locators.PLACE_ORDER_BUTTON))
        )

        personal_account = driver.find_element(By.XPATH, Locators.PERSONAL_ACC_BUTTON)
        personal_account.click()

        user_information = WebDriverWait(driver, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, Locators.LOGO_IN_PERSONAL_ACC))
        )

        assert user_information.text == 'Профиль'

