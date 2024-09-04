from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions


def test_constructor_button(register_user, login_user):
    driver = register_user

    constructor = driver.find_element(By.CSS_SELECTOR, "a[href='/_']")
    constructor.click()

    logo = WebDriverWait(driver,2).until(
        expected_conditions.visibility_of_element_located((By.XPATH,"//h1[text()='Соберите бургер']"))
    )

    assert logo.text == 'Соберите бургер'








