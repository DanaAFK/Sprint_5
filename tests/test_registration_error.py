import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Data

class TestRegistration:
    @pytest.mark.usefixtures("driver")
    def test_registration_error(self,driver):
        driver = driver

        account_button = driver.find_element(By.CSS_SELECTOR, Locators.ACC_BUTTON)
        account_button.click()

        register_link = driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_LINK)
        register_link.click()

        name_field = driver.find_element(By.XPATH, Locators.NAME_FIELD)
        name_field.send_keys(Data.USER_NAME)

        email_field = driver.find_element(By.XPATH, Locators.EMAIL_FIELD)
        email_field.send_keys(Data.VALID_EMAIL)

        password = driver.find_element(By.XPATH, Locators.PASSWORD_FIELD)
        password.send_keys("I")

        register_button = driver.find_element(By.XPATH, Locators.REGISTER_BUTTON)
        register_button.click()

        error_message = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.INVALID_PASSWORD))
        )

        assert error_message.text == "Некорректный пароль"