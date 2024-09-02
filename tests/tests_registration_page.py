import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions

driver = webdriver.Chrome()
driver.get('https://stellarburgers.nomoreparties.site/')

account_button = driver.find_element(By.XPATH, "//a[contains(@class, 'AppHeader_header_link_3') and @href='/account']")
account_button.click()

register_link = driver.find_element(By.XPATH, "//a[contains(@class, 'Auth_link_1f0lj') and @href='/register']")
register_link.click()

name = driver.find_element(By.XPATH, "//input[@class='text input__textfield text_typ_main-default' and @name='name']")
name.send_keys("Дана")

emaill = driver.find_element(By.XPATH, "//input[@class='text input__textfield text_typ_main-default' and @name='email']")
emaill.send_keys("feari@mail.com")

password = driver.find_element(By.XPATH, "//input[@class='text input__textfield text_typ_main-default' and @type='password' and @name='Пароль']")
password.send_keys("1234567890")

register_button = driver.find_element(By.XPATH, "//button[contains(@class, 'button_button') and contains(@class, 'button_button_type_primary_107Bx') and contains(@class, 'button_button_size_medium')]")
register_button.click()

login_page_header = WebDriverWait(driver, 3).until(
    expected_conditions.presence_of_element_located((By.XPATH, "//h2[text()='Вход']"))
)

assert login_page_header.text == "Вход"

driver.quit()






