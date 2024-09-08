import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestSectionsBread:
    def test_section_fluarescently_bread(self, register_and_login_user):
        driver = register_and_login_user

        fluarescently_bread = driver.find_element(By.XPATH, Locators.F_BREAD)
        fluarescently_bread.click()

        wait_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.DESCRIPTION))
        )

        assert "tick animation" in wait_description.get_attribute("alt")


    def test_section_krator_bread(self, register_and_login_user):
        driver = register_and_login_user

        krator_bread = driver.find_element(By.XPATH, Locators.K_BREAD)
        krator_bread.click()

        wait_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.DESCRIPTION))
        )
        assert "tick animation" in wait_description.get_attribute("alt")




