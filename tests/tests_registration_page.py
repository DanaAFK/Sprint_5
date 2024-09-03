from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site/')

account_button = driver.find_element(By.CSS_SELECTOR, "a[href='/account']")
account_button.click()

register_link = driver.find_element(By.CSS_SELECTOR, "a[href='/register']")
register_link.click()

name = driver.find_element(By.XPATH, "//label[text()='Имя']/following-sibling::input[@type='text']")
name.send_keys("Дана98")

email = driver.find_element(By.XPATH, "//label[text()='Email']/following-sibling::input")
email.send_keys("fairy98@mail.com")

password = driver.find_element(By.XPATH, "//label[text()='Пароль']/following-sibling::input[@type='password']")
password.send_keys("ILoveMinions098")

register_button = driver.find_element(By.XPATH, "//button[text()='Зарегистрироваться']")
register_button.click()

login_page_header = WebDriverWait(driver, 10).until(
    expected_conditions.presence_of_element_located((By.XPATH, "//h2[text()='Вход']"))
)

assert login_page_header.text == "Вход"

driver.quit()







