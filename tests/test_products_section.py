import time
import pytest
from urllib import parse as urllib
from urllib.parse import urlparse
from selenium import webdriver
from selenium.webdriver.support.ui import Select

from locators import Products


@pytest.fixture
def get_page_products(browser, login_admin):
    '''
    Функция логинится в панели администратора opencart,
    переходит в раздел "Catalog"/"Products"
    '''
    data = urlparse(browser.current_url)
    token = urllib.parse_qs(data.query)['user_token'][0]
    url = browser.get(f'http://localhost/admin/index.php?route=catalog/product&user_token={token}')
    return url


def test_create_product(browser, get_page_products):
    '''
    Тест, проверяющий функционал создания нового продукта в панели адиминистратора
    '''
    browser.find_element(*Products.add_new_btn).click()
    browser.find_element(*Products.general).click()
    browser.find_element(*Products.name).send_keys('Test Product 1')
    browser.find_element(*Products.description).send_keys('Product descripton is here')
    browser.find_element(*Products.meta_tag).send_keys('tag')
    browser.find_element(*Products.product_tag).send_keys('ptag')

    browser.find_element(*Products.data).click()
    browser.find_element(*Products.model).send_keys('Model 1')
    browser.find_element(*Products.tax_class).click()
    Select(browser.find_element(*Products.tax_class)).select_by_visible_text('Taxable Goods')
    browser.find_element(*Products.save).click()
    time.sleep(2)
    assert browser.find_element(*Products.success_message)


def test_edit_product(browser, get_page_products):
    '''
    Тест, проверяющий функционал редактирования существующего продукта в панели адиминистратора
    '''
    browser.find_element(*Products.edit_product).click()
    browser.find_element(*Products.name).clear()
    browser.find_element(*Products.name).send_keys("Test product")
    browser.find_element(*Products.data).click()
    pname = browser.find_element(*Products.model).get_attribute('value')
    browser.find_element(*Products.model).clear()
    browser.find_element(*Products.model).send_keys(pname.replace('1', '2'))
    browser.find_element(*Products.save).click()
    time.sleep(3)
    assert browser.find_element(*Products.success_message)


def test_delete_product(browser, get_page_products):
    '''
    Тест, проверяющий функционал удаления продукта в панели адиминистратора
    '''
    browser.find_element(*Products.pick_a_product).click()
    browser.find_element(*Products.delete_product).click()
    time.sleep(2)
    browser.switch_to.alert.accept()
    assert browser.find_element(*Products.success_message)
