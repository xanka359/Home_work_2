from selene import browser, be, have
import pytest

@pytest.fixture()
def test_browser():
    browser.open('https://google.com')

    yield

@pytest.fixture()
def test_browser_1():
    browser.open('https://www.ecosia.org/')

    yield