import pytest
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators

class TestSectionsFilling:
    @pytest.mark.usefixtures("register_and_login_user")
    def test_meat(self, register_and_login_user):
        driver = register_and_login_user

        meat = driver.find_element(By.XPATH, Locators.MEAT_FILLING)
        meat.click()

        wait_description = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locators.MEAT_FILLING_DESCRIPTION))
        )

        assert wait_description.text == "Мясо бессмертных моллюсков Protostomia"

    @pytest.mark.usefixtures("register_and_login_user")
    def test_meat(self, register_and_login_user):
        driver = register_and_login_user

        meteor = driver.find_element(By.XPATH, Locators.METEOR_FILLING)
        meteor.click()

        wait_description = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locators.METEOR_FILLING_DESCRIPTION))
        )

        assert wait_description.text == "Говяжий метеорит (отбивная)"

    @pytest.mark.usefixtures("register_and_login_user")
    def test_magnolian(self, register_and_login_user):
        driver = register_and_login_user

        magnolian = driver.find_element(By.XPATH, Locators.MAGNOLIAN_FILLING)
        magnolian.click()

        wait_description = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locators.MAGNOLIAN_FILLING_DESCRIPTION))
        )

        assert wait_description.text == "Биокотлета из марсианской Магнолии"

    @pytest.mark.usefixtures("register_and_login_user")
    def test_blue_fish(self, register_and_login_user):
        driver = register_and_login_user

        blue_fish = driver.find_element(By.XPATH, Locators.BLUE_FISH_FILLING)
        blue_fish.click()

        wait_description = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locators.BLUE_FISH_FILLING_DESCRIPTION))
        )

        assert wait_description.text == "Филе Люминесцентного тетраодонтимформа"

    @pytest.mark.usefixtures("register_and_login_user")
    def test_mineral(self, register_and_login_user):
        driver = register_and_login_user

        mineral = driver.find_element(By.XPATH, Locators.MINERAL_FILLING)
        mineral.click()

        wait_description = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locators.MINERAL_FILLING_DESCRIPTION))
        )

        assert wait_description.text == "Хрустящие минеральные кольца"

    @pytest.mark.usefixtures("register_and_login_user")
    def test_falenial(self, register_and_login_user):
        driver = register_and_login_user

        falenial = driver.find_element(By.XPATH, Locators.FALENIAL_FILLING)
        falenial.click()

        wait_description = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locators.FALENIAL_FILLING_DESCRIPTION))
        )

        assert wait_description.text == "Плоды Фалленианского дерева"

    @pytest.mark.usefixtures("register_and_login_user")
    def test_alfa(self, register_and_login_user):
        driver = register_and_login_user

        alfa = driver.find_element(By.XPATH, Locators.ALFA_FILLING)
        alfa.click()

        wait_description = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locators.ALFA_FILLING_DESCRIPTION))
        )

        assert wait_description.text == "Кристаллы марсианских альфа-сахаридов"

    @pytest.mark.usefixtures("register_and_login_user")
    def test_salat(self, register_and_login_user):
        driver = register_and_login_user

        salat = driver.find_element(By.XPATH, Locators.SALAT_FILING)
        salat.click()

        wait_description = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locators.SALAT_FILING_DESCRIPTION))
        )

        assert wait_description.text == "Мини-салат Экзо-Плантаго"

    @pytest.mark.usefixtures("register_and_login_user")
    def test_chees(self, register_and_login_user):
        driver = register_and_login_user

        chees = driver.find_element(By.XPATH, Locators.CHEES_FILLING)
        chees.click()

        wait_description = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((By.XPATH, Locators.CHEES_FILLING_DESCRIPTION))
        )

        assert wait_description.text == "Сыр с астероидной плесенью"


