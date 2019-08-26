from selenium import webdriver

def test_opencart(browser, base_url):
    browser.get(f'http://{base_url}/opencart/')
    assert '/opencart/' in browser.current_url, 'URL неверный!'
