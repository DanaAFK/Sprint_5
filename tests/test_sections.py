import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators


class TestSections:
    def test_tab_to_sauces_section(self, register_and_login_user):
        driver = register_and_login_user
        wait = WebDriverWait(driver, 5)

        inactive_sauces_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, Locators.INACTIVE_SOUSE)))

        inactive_sauces_tab.click()

        active_sauces_tab = wait.until(EC.presence_of_element_located(
            (By.XPATH, Locators.ACTIVE_SOUSE)))

        assert "tab_tab_type_current__2BEPc" in active_sauces_tab.get_attribute('class')

    def test_tab_to_filling_section(self, register_and_login_user):
        driver = register_and_login_user
        wait = WebDriverWait(driver, 5)

        inactive_filling_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, Locators.INACTIVE_FILLING)))

        inactive_filling_tab.click()

        active_filling_tab = wait.until(EC.presence_of_element_located(
            (By.XPATH, Locators.ACTIVE_FILLING)))

        assert "tab_tab_type_current__2BEPc" in active_filling_tab.get_attribute('class')

    def test_tab_to_bread_section(self, register_and_login_user):
        driver = register_and_login_user
        wait = WebDriverWait(driver, 5)

        another_section = driver.find_element(By.XPATH, Locators.INACTIVE_SOUSE)
        another_section.click()

        inactive_bread_tab = wait.until(
            EC.element_to_be_clickable((By.XPATH, Locators.INACTIVE_BREAD)))

        inactive_bread_tab.click()

        active_bread_tab = wait.until(EC.presence_of_element_located(
            (By.XPATH, Locators.ACTIVE_BREAD)))

        assert "tab_tab_type_current__2BEPc" in active_bread_tab.get_attribute('class')
