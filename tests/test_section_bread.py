import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestSectionsBread:
    @pytest.mark.usefixtures("register_and_login_user")
    def test_section_fluarescently_bread(self, register_and_login_user):
        driver = register_and_login_user

        fluarescently_bread = driver.find_element(By.XPATH, Locators.F_BREAD)
        fluarescently_bread.click()

        wait_description = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locators.F_BREAD_DESCRIPTION))
        )

        assert wait_description.text == "Флюоресцентная булка R2-D3"

        @pytest.mark.usefixtures("register_and_login_user")
        def test_section_krator_bread(self, register_and_login_user):
            driver = register_and_login_user

            krator_bread = driver.find_element(By.XPATH, Locators.K_BREAD)
            krator_bread.click()

            wait_description = WebDriverWait(driver, 5).until(
                EC.presence_of_element_located((By.XPATH, Locators.K_BREAD_DESCRIPTION))
            )

            assert wait_description.text == "Краторная булка N-200i"


