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

    F_BREAD = '//img[@alt="Флюоресцентная булка R2-D3"]'
    K_BREAD = "//img[@alt='Краторная булка N-200i']"

    DESCRIPTION = '//img[@class="Modal_modal__ingImage__2_sz2"]'

    SPICY_SAUSE = '//img[@alt="Соус Spicy-X"]'
    SPACE_SAUSE = '//img[@alt="Соус фирменный Space Sauce"]'
    YELLOW_SAUSE = '//img[@alt="Соус традиционный галактический"]'
    READ_SAUSE = '//img[@alt="Соус с шипами Антарианского плоскоходца"]'

    MEAT_FILLING = '//img[@alt="Мясо бессмертных моллюсков Protostomia"]'
    METEOR_FILLING = '//img[@alt="Говяжий метеорит (отбивная)"]'
    MAGNOLIAN_FILLING = '//img[@alt="Биокотлета из марсианской Магнолии"]'
    BLUE_FISH_FILLING = '//img[@alt="Филе Люминесцентного тетраодонтимформа"]'
    MINERAL_FILLING = '//img[@alt="Хрустящие минеральные кольца"]'
    FALENIAL_FILLING = '//img[@alt="Плоды Фалленианского дерева"]'
    ALFA_FILLING = '//img[@alt="Кристаллы марсианских альфа-сахаридов"]'
    SALAT_FILING = '//img[@alt="Мини-салат Экзо-Плантаго"]'
    CHEES_FILLING = '//img[@alt="Сыр с астероидной плесенью"]'





















