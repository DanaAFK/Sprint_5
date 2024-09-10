import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from locators import Locators
from data import Data

fake = Faker()


class TestRegistration:
    def test_registration_true(self, driver):
        driver.get(Data.ACCOUNT_URL)

        driver.find_element(By.CSS_SELECTOR, Locators.REGISTER_LINK).click()

        name_field = driver.find_element(By.XPATH, Locators.NAME_FIELD)
        name_field.send_keys(Data.USER_NAME)

        email_field = driver.find_element(By.XPATH, Locators.EMAIL_FIELD)
        generated_email = fake.email()
        email_field.send_keys(generated_email)

        password_field = driver.find_element(By.XPATH, Locators.PASSWORD_FIELD)
        password_field.send_keys(Data.USER_PASSWORD)

        driver.find_element(By.XPATH, Locators.REGISTER_BUTTON).click()

        registration = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.LOGIN_HEADER))
        )

        assert registration.text == 'Вход'

    def test_registration_error(self, driver):
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








