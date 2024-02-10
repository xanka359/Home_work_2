from selene import browser, be, have
import pytest


@pytest.fixture(autouse=True)
def setting_browser():
    browser.config.window_height = 1080  # задает высоту окна браузера
    browser.config.window_width = 1920  # задает ширину окна браузера

    yield
    browser.quit()