import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestSectionsFilling:
    def test_section_meat_filling(self, register_and_login_user):
        driver = register_and_login_user

        meat_filling = driver.find_element(By.XPATH, Locators.MEAT_FILLING)
        meat_filling.click()

        wait_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.DESCRIPTION))
        )
        assert "Modal_modal__ingImage__2_sz2" in wait_description.get_attribute("class")

    def test_section_meteor_filling(self, register_and_login_user):
        driver = register_and_login_user

        meteor_filling = driver.find_element(By.XPATH, Locators.METEOR_FILLING)
        meteor_filling.click()

        wait_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.DESCRIPTION))
        )
        assert "Modal_modal__ingImage__2_sz2" in wait_description.get_attribute("class")

    def test_section_magnolian_filling(self, register_and_login_user):
        driver = register_and_login_user

        magnolian_filling = driver.find_element(By.XPATH, Locators.MAGNOLIAN_FILLING)
        magnolian_filling.click()

        wait_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.DESCRIPTION))
        )
        assert "Modal_modal__ingImage__2_sz2" in wait_description.get_attribute("class")


    def test_section_blue_fish_filling(self, register_and_login_user):
        driver = register_and_login_user

        blue_fish_filling = driver.find_element(By.XPATH, Locators.BLUE_FISH_FILLING)
        blue_fish_filling.click()

        wait_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.DESCRIPTION))
        )
        assert "Modal_modal__ingImage__2_sz2" in wait_description.get_attribute("class")


    def test_section_mineral_filling(self, register_and_login_user):
        driver = register_and_login_user

        mineral_filling = driver.find_element(By.XPATH, Locators.MINERAL_FILLING)
        mineral_filling.click()

        wait_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.DESCRIPTION))
        )
        assert "Modal_modal__ingImage__2_sz2" in wait_description.get_attribute("class")

    def test_section_falenial_filling(self, register_and_login_user):
        driver = register_and_login_user

        falenial_filling = driver.find_element(By.XPATH, Locators.FALENIAL_FILLING)
        falenial_filling.click()

        wait_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.DESCRIPTION))
        )
        assert "Modal_modal__ingImage__2_sz2" in wait_description.get_attribute("class")

    def test_section_alfa_filling(self, register_and_login_user):
        driver = register_and_login_user

        alfa_filling = driver.find_element(By.XPATH, Locators.ALFA_FILLING)
        alfa_filling.click()

        wait_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.DESCRIPTION))
        )
        assert "Modal_modal__ingImage__2_sz2" in wait_description.get_attribute("class")

    def test_section_salat_filing(self, register_and_login_user):
        driver = register_and_login_user

        salat_filing = driver.find_element(By.XPATH, Locators.SALAT_FILING)
        salat_filing.click()

        wait_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.DESCRIPTION))
        )
        assert "Modal_modal__ingImage__2_sz2" in wait_description.get_attribute("class")

    def test_section_chees_filling(self, register_and_login_user):
        driver = register_and_login_user

        chees_filling = driver.find_element(By.XPATH, Locators.CHEES_FILLING)
        chees_filling.click()

        wait_description = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, Locators.DESCRIPTION))
        )
        assert "Modal_modal__ingImage__2_sz2" in wait_description.get_attribute("class")


