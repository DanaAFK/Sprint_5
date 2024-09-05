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
