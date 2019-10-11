from random import random
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

from locators import AdminPanel
from locators import GeneralElements
from locators import MainPage
from locators import ProductCard
from locators import ComponentsSection
from locators import RegisterAccount

def test_opencart(browser, base_url):
    browser.get(f'http://{base_url}/opencart/')
    assert '/opencart/' in browser.current_url, 'URL неверный!'


def test_adminpanel_login(browser):
    browser.get('http://localhost/opencart/admin')
    browser.find_element_by_css_selector(AdminPanel.username).send_keys('admin')
    browser.find_element_by_css_selector(AdminPanel.password).send_keys('123456')
    browser.find_element_by_css_selector(AdminPanel.login_button).click()
    assert 'dashboard' in browser.current_url, 'Error Login'


def test_add_cart(browser):
    browser.get('http://localhost/opencart/')
    time.sleep(1)
    browser.find_element_by_css_selector(GeneralElements.add_to_cart).click()
    product_name = browser.find_element_by_css_selector(GeneralElements.name_of_product).text
    time.sleep(1)
    browser.find_element_by_css_selector(GeneralElements.cart_button).click()
    name_in_cart = browser.find_element_by_css_selector(GeneralElements.product_in_cart).text
    assert product_name == name_in_cart


def test_register_form(browser):
    browser.get('http://localhost/opencart/index.php?route=account/register')
    browser.find_element_by_css_selector(RegisterAccount.fname).send_keys('John')
    browser.find_element_by_css_selector(RegisterAccount.lname).send_keys('Doe')
    browser.find_element_by_css_selector(RegisterAccount.email).send_keys(f'test{random()}@mail.ru')
    browser.find_element_by_css_selector(RegisterAccount.tel).send_keys('5556677')

    browser.find_element_by_css_selector(RegisterAccount.password).send_keys('qwerty')
    browser.find_element_by_css_selector(RegisterAccount.pass_confirm).send_keys('qwerty')

    browser.find_element_by_css_selector(RegisterAccount.ppolicy_check).click()
    browser.find_element_by_css_selector(RegisterAccount.submit).click()

    assert 'account/success' in browser.current_url


def test_searchbar(browser):
    browser.get('http://localhost/opencart/')
    search_text = 'canon'
    browser.find_element_by_css_selector(GeneralElements.search_line).send_keys(search_text)
    browser.find_element_by_css_selector(GeneralElements.search_button).click()
    assert browser.find_element_by_css_selector(GeneralElements.product_card), 'Продукты не найдены'

    found_product = browser.find_element_by_css_selector(GeneralElements.name_of_product).text.lower()
    assert search_text in found_product, 'Найдены нерелевантные продукты'


def test_sort(browser):
    browser.get('http://localhost/opencart/')
    sections = browser.find_elements_by_css_selector(GeneralElements.sections_of_menu)
    sections[5].click()

    browser.find_element_by_css_selector(ComponentsSection.choose_sort).click()
    Select(browser.find_element_by_css_selector(ComponentsSection.choose_sort)).select_by_visible_text('Name (A - Z)')

    sorted_products = []
    [sorted_products.append(product.text) for product in browser.find_elements_by_css_selector(GeneralElements.name_of_product)]

    sorted_products_expect = sorted_products.copy()
    sorted_products_expect.sort(key=str.lower)

    assert sorted_products == sorted_products_expect, 'Продукты сортируются некорректно'
