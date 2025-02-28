import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.firefox.options import Options

from locators import AdminPanel


def pytest_addoption(parser):
    parser.addoption('--browser', default='chrome', help='You need to choose a browser')
    parser.addoption('--base_url', default='localhost', help='You need to specify a base url')


@pytest.fixture
def browser(request):
    '''
    Фикстура для настройки вебдрайвера, переданного
    в командной строке при запуске тестов
    '''

    parameter = request.config.getoption('--browser')

    if parameter == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('--start-maximized')
        chrome_options.add_argument('--headless')
        browser = webdriver.Chrome(options=chrome_options)

    elif parameter == 'firefox':
        firefox_options = webdriver.FirefoxOptions()
        firefox_options.add_argument('--start-maximized')
        firefox_options.add_argument('--headless')
        browser = webdriver.Firefox(options=firefox_options)
        browser.maximize_window()

    else:
        raise Exception('Браузер указан неверно!')

    yield browser

    browser.quit()


@pytest.fixture
def base_url(request):
    return request.config.getoption('--base_url')


@pytest.fixture
def login_admin(browser):
    browser.get('http://localhost/admin')
    browser.find_element_by_css_selector(AdminPanel.username).send_keys('user')
    browser.find_element_by_css_selector(AdminPanel.password).send_keys('bitnami1')
    browser.find_element_by_css_selector(AdminPanel.login_button).click()
    assert 'dashboard' in browser.current_url, 'Error Login'
