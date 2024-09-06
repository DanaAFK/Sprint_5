import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Data

class TestLogin:
    def test_login_using_personal_account_button(self, driver):
        driver = driver

        personal_account_button = driver.find_element(By.XPATH, Locators.PERSONAL_ACC_BUTTON)
        personal_account_button.click()

        email = driver.find_element(By.XPATH, Locators.EMAIL_FIELD)
        email.send_keys(Data.VALID_EMAIL)

        password_field = driver.find_element(By.XPATH, Locators.PASSWORD_FIELD)
        password_field.send_keys(Data.VALID_PASSWORD)

        login_button = driver.find_element(By.XPATH, Locators.LOGIN_BUTTON)
        login_button.click()

        place_in_order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Locators.PLACE_ORDER_BUTTON))
        )

        assert place_in_order_button.text == Data.ORDER_BUTTON_TEXT

    def test_login_using_recover_password(self,driver):
        driver = driver

        account_button = driver.find_element(By.XPATH, Locators.GO_TO_ACC)
        account_button.click()

        recover_password_button = driver.find_element(By.CSS_SELECTOR, Locators.RECOVER_PASSWORD)
        recover_password_button.click()

        login_button = driver.find_element(By.CSS_SELECTOR, Locators.LOGIN_BUTTON_DOWN)
        login_button.click()

        email = driver.find_element(By.XPATH, Locators.EMAIL_FIELD)
        email.send_keys(Data.VALID_EMAIL)

        password_field = driver.find_element(By.XPATH, Locators.PASSWORD_FIELD)
        password_field.send_keys(Data.VALID_PASSWORD)

        login_button = driver.find_element(By.XPATH, Locators.LOGIN_BUTTON)
        login_button.click()

        place_in_order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Locators.PLACE_ORDER_BUTTON))
        )

        assert place_in_order_button.text == Data.ORDER_BUTTON_TEXT

    def test_login_and_order(self, register_user):
        driver, generated_email = register_user

        email = driver.find_element(By.XPATH, Locators.EMAIL_FIELD)
        email.send_keys(Data.VALID_EMAIL)

        password_field = driver.find_element(By.XPATH, Locators.PASSWORD_FIELD)
        password_field.send_keys(Data.VALID_PASSWORD)

        login_button = driver.find_element(By.XPATH, Locators.LOGIN_BUTTON)
        login_button.click()

        place_in_order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Locators.PLACE_ORDER_BUTTON))
        )

        assert place_in_order_button.text == Data.ORDER_BUTTON_TEXT

    def test_login_using_the_login_button(self, driver):
        driver = driver

        login_in_form_button = driver.find_element(By.XPATH, Locators.GO_TO_ACC)
        login_in_form_button.click()

        email = driver.find_element(By.XPATH, Locators.EMAIL_FIELD)
        email.send_keys(Data.VALID_EMAIL)

        password_field = driver.find_element(By.XPATH, Locators.PASSWORD_FIELD)
        password_field.send_keys(Data.VALID_PASSWORD)

        login_button = driver.find_element(By.XPATH, Locators.LOGIN_BUTTON)
        login_button.click()

        place_in_order_button = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Locators.PLACE_ORDER_BUTTON))
        )

        assert place_in_order_button.text == Data.ORDER_BUTTON_TEXT


