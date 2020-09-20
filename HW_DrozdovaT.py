from selenium import webdriver
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

#Pages
main_page = "http://selenium1py.pythonanywhere.com/ru"
catalogue = "http://selenium1py.pythonanywhere.com/ru/catalogue/"
basket = "http://selenium1py.pythonanywhere.com/ru/basket"

#Locators
locator_search_input = "input#id_q"
locator_search_button = "input.btn.btn-default"
locator_search_title = "h1"

locator_login_link = "a#login_link"
locator_login_input_email = "input#id_login-username"
locator_login_input_password = "input#id_login-password"
locator_login_submit = "button[name = 'login_submit']"
locator_login_message = "alertinner.wicon"

locator_reg_input_email = "input#id_registration-email"
locator_reg_input_password1 = "input#id_registration-password1"
locator_reg_input_password2 = "input#id_registration-password2"
locator_reg_submit = "button[name = 'registration_submit']"

locator_language_selector = "select[name = 'language']"
locator_language_option = "option[value = 'de']"
locator_language_button = "#language_selector > button"
locator_goods_selector = "#browse > li > a"

locator_book1_choose_button = "//li[8]/article/div[2]/form/button"
locator_book2_choose_button = "//li[1]/article/div[2]/form/button"
locator_book1_title = "li:nth-child(8) > article > h3"
locator_book2_title = "li:nth-child(1) > article > h3"
locator_book1_title_basket = "//div[1]/div/div[2]/h3"
locator_book2_title_basket = "//div[2]/div/div[2]/h3"


#1.Поиск товара по наименованию 

def search():

    #Data
    search_text = "The shellcoder's handbook"

    try:

    #Arrange
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(main_page)

    #Act
        search_input = browser.find_element_by_css_selector(locator_search_input)
        search_input.clear()
        search_input.send_keys(search_text)
        
        browser.find_element_by_css_selector(locator_search_button).click()

        search_result = browser.find_element_by_link_text(search_text)
        search_title = browser.find_element_by_tag_name(locator_search_title)
        search_title = search_title.text

    #Asserts    
        assert "The shellcoder's handbook" in search_title, \
        "Search doesn't contain The shellcoder's handbook"

    finally:
        browser.quit()

    
#2. Авторизация

def login():

    #Data

    login = "test30082020@gmail.com"
    password = "Test202020"

    try:

    #Arrange    
        browser = webdriver.Chrome()
        browser.implicitly_wait(3)
        browser.get(main_page)
    #Act
        browser.find_element_by_css_selector(locator_login_link).click()
        browser.find_element_by_css_selector(locator_login_input_email).send_keys(login)
        browser.find_element_by_css_selector(locator_login_input_password).send_keys(password)
        browser.find_element_by_css_selector(locator_login_submit).click()

        message_auth = browser.find_element_by_class_name(locator_login_message)

    #Asserts    
        assert "Рады видеть вас снова" in message_auth.text, \
        "The user is not logged in"

    finally:
    	browser.quit()

#3. Регистрация 

def registration():

    #Data
    password = "Test202020"    

    def emails():
        email = ''
        for x in range(12):
            email = email + random.choice(list('1234567890qwertyuiopASDFGHJKLZXCVBMNMNM'))
        email = email + '@gmail.com'
        return email

    try:
    #Arrange      
        browser = webdriver.Chrome()
        browser.implicitly_wait(3)
        browser.get(main_page)

    #Act
        browser.find_element_by_css_selector(locator_login_link).click()
        browser.find_element_by_css_selector(locator_reg_input_email).send_keys(emails())
        browser.find_element_by_css_selector(locator_reg_input_password1).send_keys(password)
        browser.find_element_by_css_selector(locator_reg_input_password2).send_keys(password)
        browser.find_element_by_css_selector(locator_reg_submit).click()

        message_reg = browser.find_element_by_class_name(locator_login_message)

    #Asserts
        assert "Спасибо за регистрацию" in message_reg.text, \
        "The user is not registered"

    finally:
        browser.quit()


#4. Смена языка интерфейса

def language():

    try:

    #Arrange       
        browser = webdriver.Chrome()
        browser.implicitly_wait(3)
        browser.get(main_page)

    #Act
        browser.find_element_by_css_selector(locator_language_selector).click()
        browser.find_element_by_css_selector(locator_language_option).click()
        browser.find_element_by_css_selector(locator_language_button).click()
        
        login_link = browser.find_element_by_css_selector(locator_login_link)
        goods_selector = browser.find_element_by_css_selector(locator_goods_selector)
        
    #Asserts
        assert "Einloggen" in login_link.text, "Login link text isn't translated"
        assert "Webshop" in goods_selector.text, "Goods selector text isn't translated"

    finally:
        browser.quit()

#5. Добавление товаров в корзину


def add_to_the_cart():

    try:

    #Arrange       
        browser = webdriver.Chrome()
        browser.implicitly_wait(5)
        browser.get(catalogue)

    #Act
        browser.find_element_by_xpath(locator_book1_choose_button).click()
        book_one_t = browser.find_element_by_css_selector(locator_book1_title).text

        browser.find_element_by_xpath(locator_book2_choose_button).click()
        book_two_t = browser.find_element_by_css_selector(locator_book2_title).text
        
        browser.get(basket)
        book_one_title = browser.find_element_by_xpath(locator_book1_title_basket)
        book_two_title = browser.find_element_by_xpath(locator_book2_title_basket)

    #Asserts
        assert book_one_t in book_one_title.text, "The first book is not in the basket"
        assert book_two_t in book_two_title.text, "The second book is not in the basket"

    finally:
        browser.quit()


#RUN
search()
login()
registration()
language()
add_to_the_cart()