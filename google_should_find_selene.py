from selene import browser, be, have
import pytest


@pytest.fixture()
def test_browser():
    browser.open('https://google.com')

    yield

def test_search(test_browser):
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))
#if browser.element(by.text('Accept all')).matching(be.visible):
 #  browser.element(by.text('Accept all')).click()