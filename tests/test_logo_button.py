import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
from data import Data

class TestTopButton:
    @pytest.mark.usefixtures("register_and_login_user")
    def test_logo_button(self, register_and_login_user):
        driver = register_and_login_user

        personal_account = driver.find_element(By.XPATH, Locators.PERSONAL_ACC_BUTTON)
        personal_account.click()

        logo_button = driver.find_element(By.XPATH, Locators.LOGO_BUTTON)
        logo_button.click()

        logo = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.XPATH, Locators.CONSTRUCTOR_LOGO))
        )

        assert logo.text == Data.ORDER_CONSTRUCTOR_LOGO_TEXT