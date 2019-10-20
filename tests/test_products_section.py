import time
from urllib import parse as urllib
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from locators import Products


def get_user_token(url):
    '''
    Функция принимает на вход url;
    возвращает значение параметра user_token
    '''
    data = urlparse(url)
    query_data = urllib.parse_qs(data.query)
    return query_data['user_token'][0]


def test_create_product(browser, login_admin):
    token = get_user_token(browser.current_url)
    browser.get(f'http://localhost/admin/index.php?route=catalog/product&user_token={token}')
    browser.find_element(*Products.add_new_btn).click()
    browser.find_element(*Products.general).click()
    browser.find_element(*Products.name).send_keys('Test Product')
    browser.find_element(*Products.description).send_keys('Product descripton is here')
    browser.find_element(*Products.meta_tag).send_keys('tag')
    browser.find_element(*Products.product_tag).send_keys('ptag')

    browser.find_element(*Products.data).click()
    browser.find_element(*Products.model).send_keys('Model 1')
    browser.find_element(*Products.tax_class).click()
    Select(browser.find_element(*Products.tax_class)).select_by_visible_text('Taxable Goods')
    browser.find_element(*Products.save).click()
    time.sleep(3)
    assert browser.find_element(*Products.success_message)


def test_edit_product(browser):
    pass


def test_delete_product(browser):
    pass
