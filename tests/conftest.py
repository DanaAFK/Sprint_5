import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


@pytest.fixture(scope="function")
def register_user():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    account_button = driver.find_element(By.CSS_SELECTOR, "a[href='/account']")
    account_button.click()

    register_link = driver.find_element(By.CSS_SELECTOR, "a[href='/register']")
    register_link.click()

    name = driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input[@type='text']")
    name.send_keys("Дана_1")

    emaill = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
    emaill.send_keys("fairy_1@mail.com")

    password = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input[@type='password']")
    password.send_keys("ILoveMinions098")

    register_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    register_button.click()

    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//h2[text()='Вход']"))
    )

    yield driver
    driver.quit()


@pytest.fixture(scope="function")
def register_and_login_user():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')

    account_button = driver.find_element(By.CSS_SELECTOR, "a[href='/account']")
    account_button.click()

    register_link = driver.find_element(By.CSS_SELECTOR, "a[href='/register']")
    register_link.click()

    name = driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input[@type='text']")
    name.send_keys("Дана_2")

    emaill = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
    emaill.send_keys("fairy_2@mail.com")

    password = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input[@type='password']")
    password.send_keys("ILoveMinions098")

    register_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
    register_button.click()

    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//h2[text()='Вход']"))
    )

    email = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input[@type='text']")
    email.send_keys("fairy87@mail.com")

    password = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input[@type='password']")
    password.send_keys("ILoveMinions098")

    login_button = driver.find_element(By.XPATH, "//button[text()='Войти']")
    login_button.click()

    WebDriverWait(driver, 10).until(
        expected_conditions.presence_of_element_located((By.XPATH, "//button[text()='Оформить заказ']"))
    )

    yield driver
    driver.quit()