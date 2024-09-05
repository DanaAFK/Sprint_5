import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestSectionsSause:
    @pytest.mark.usefixtures("register_and_login_user")
    def test_spicy(self, register_and_login_user):
        driver = register_and_login_user

        spicy = driver.find_element(By.XPATH, Locators.SPICY_SAUSE)
        spicy.click()

        wait_description = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locators.SPICY_SAUSE_DESCRIPTION))
        )

        assert wait_description.text == "Соус Spicy-X"

    @pytest.mark.usefixtures("register_and_login_user")
    def test_space(self, register_and_login_user):
        driver = register_and_login_user

        space = driver.find_element(By.XPATH, Locators.SPACE_SAUSE)
        space.click()

        wait_description = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locators.SPACE_SAUSE_DESCRIPTION))
        )
        assert wait_description.text == "Соус фирменный Space Sauce"

    @pytest.mark.usefixtures("register_and_login_user")
    def test_yellow(self, register_and_login_user):
        driver = register_and_login_user

        yellow = driver.find_element(By.XPATH, Locators.YELLOW_SAUSE)
        yellow.click()

        wait_description = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locators.YELLOW_SAUSE_DESCRIPTION))
        )
        assert wait_description.text == "Соус традиционный галактический"

    @pytest.mark.usefixtures("register_and_login_user")
    def test_read(self, register_and_login_user):
        driver = register_and_login_user

        read = driver.find_element(By.XPATH, Locators.READ_SAUSE)
        read.click()

        wait_description = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locators.READ_SAUSE_DESCRIPTION))
        )
        assert wait_description.text == "Соус с шипами Антарианского плоскоходца"

