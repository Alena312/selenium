import time
import pytest
import selenium
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains

from locators import DartDnD


def test_drag_and_drop(browser):
    '''
    Тест проверяет работоспособность функционала drag&drop
    '''
    browser.get('https://code.makery.ch/library/dart-drag-and-drop/')
    target_block = browser.find_element(*DartDnD.target_block)
    target_block.location_once_scrolled_into_view
    browser.switch_to.frame(target_block)

    docs = browser.find_elements(*DartDnD.documents)
    basket = browser.find_element(*DartDnD.basket)
    action = ActionChains(browser)
    for doc in docs:
        action.drag_and_drop(doc, basket)
    action.perform()

    assert browser.find_elements(*DartDnD.documents) == [], 'Документы не в корзине!'
