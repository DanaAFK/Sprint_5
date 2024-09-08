import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestSectionsSause:

    def test_section_spicy_sause(self, register_and_login_user):
        driver = register_and_login_user

        spicy_sause = driver.find_element(By.XPATH, Locators.SPICY_SAUSE)
        spicy_sause.click()

        wait_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.DESCRIPTION))
        )
        assert "tick animation" in wait_description.get_attribute("alt")

    def test_section_space_sause(self, register_and_login_user):
        driver = register_and_login_user

        space_sause = driver.find_element(By.XPATH, Locators.SPACE_SAUSE)
        space_sause.click()

        wait_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.DESCRIPTION))
        )
        assert "tick animation" in wait_description.get_attribute("alt")

    def test_section_yellow_sause(self, register_and_login_user):
        driver = register_and_login_user

        yellow_sause = driver.find_element(By.XPATH, Locators.YELLOW_SAUSE)
        yellow_sause.click()

        wait_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.DESCRIPTION))
        )
        assert "tick animation" in wait_description.get_attribute("alt")

    def test_section_read_sause(self, register_and_login_user):
        driver = register_and_login_user

        read_sause = driver.find_element(By.XPATH, Locators.READ_SAUSE)
        read_sause.click()

        wait_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.DESCRIPTION))
        )
        assert "tick animation" in wait_description.get_attribute("alt")

