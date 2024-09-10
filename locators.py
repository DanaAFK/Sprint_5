class Locators:
    REGISTER_LINK = "a[href='/register']"
    NAME_FIELD = "//label[text()='Имя']/following-sibling::input[@type='text']"
    EMAIL_FIELD = "//label[text()='Email']/following-sibling::input"
    PASSWORD_FIELD = "//label[text()='Пароль']/following-sibling::input[@type='password']"
    REGISTER_BUTTON = "//button[text()='Зарегистрироваться']"
    LOGIN_HEADER = "//h2[text()='Вход']"
    LOGIN_BUTTON = "//button[text()='Войти']"
    PLACE_ORDER_BUTTON = "//button[text()='Оформить заказ']"

    CONSTRUCTOR_BUTTON = "a[href='/']"
    CONSTRUCTOR_LOGO = "//h1[text()='Соберите бургер']"

    GO_TO_ACC = "//button[text()='Войти в аккаунт']"

    RECOVER_PASSWORD = "a[href='/forgot-password']"
    LOGIN_BUTTON_DOWN = "a[href='/login']"

    PERSONAL_ACC_BUTTON = "//p[text()='Личный Кабинет']"
    LOGO_BUTTON = "//*[name()='svg' and @xmlns='http://www.w3.org/2000/svg']"

    LOG_OUT_BUTTON = "//button[contains(., 'Выход')]"
    LOGO_IN_PERSONAL_ACC = "a[href='/account/profile']"

    ACC_BUTTON = "a[href='/account']"

    INVALID_PASSWORD = "//p[text()='Некорректный пароль']"

    INACTIVE_SOUSE = '//div[contains(@class, "tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect") and span[text()="Соусы"]]'
    ACTIVE_SOUSE = '//div[contains(@class, "tab_tab_type_current__2BEPc") and span[text()="Соусы"]]'

    INACTIVE_FILLING = '//div[contains(@class, "tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect") and span[text()="Начинки"]]'
    ACTIVE_FILLING = '//div[contains(@class, "tab_tab_type_current__2BEPc") and span[text()="Начинки"]]'

    INACTIVE_BREAD = '//div[contains(@class, "tab_tab__1SPyG  pt-4 pr-10 pb-4 pl-10 noselect") and span[text()="Булки"]]'
    ACTIVE_BREAD = '//div[contains(@class, "tab_tab_type_current__2BEPc") and span[text()="Булки"]]'


















