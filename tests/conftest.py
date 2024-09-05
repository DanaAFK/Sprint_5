import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from faker import Faker
from locators import Locators
from data import Data

fake = Faker()

@pytest.fixture(scope="function")
def driver():
    driver = webdriver.Chrome()
    driver.get(Data.BASE_URL)
    yield driver

    driver.quit()

@pytest.fixture(scope="function")
def register_user(driver):
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

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, Locators.LOGIN_HEADER))
    )

    yield driver, generated_email


@pytest.fixture(scope="function")
def register_and_login_user(driver):
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

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, Locators.LOGIN_HEADER))
    )

    email_login_field = driver.find_element(By.XPATH, Locators.EMAIL_FIELD)
    email_login_field.send_keys(generated_email)

    password_login_field = driver.find_element(By.XPATH, Locators.PASSWORD_FIELD)
    password_login_field.send_keys(Data.USER_PASSWORD)

    login_button = driver.find_element(By.XPATH, Locators.LOGIN_BUTTON)
    login_button.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, Locators.PLACE_ORDER_BUTTON))
    )

    yield driver
