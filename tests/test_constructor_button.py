import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators



class TestConstructorButton:
    @pytest.mark.usefixtures("register_and_login_user")
    def test_constructor_button(self, register_and_login_user):
        driver = register_and_login_user

        personal_account = driver.find_element(By.XPATH, "//p[text()='Личный Кабинет']")
        personal_account.click()

        constructor_button = driver.find_element(By.CSS_SELECTOR, Locators.CONSTRUCTOR_BUTTON)
        constructor_button.click()

        logo = WebDriverWait(driver, 2).until(
            EC.visibility_of_element_located((By.XPATH, Locators.CONSTRUCTOR_LOGO))
        )

        assert logo.text == 'Соберите бургер'










