from selene import browser, be, have
import pytest

@pytest.fixture()
def test_browser_1():
    browser.open('https://www.ecosia.org/')

    yield


def test_search(test_browser_1):
    browser.element('[name="q"]').should(be.blank).type("????????????????????????????????|||||||||||||||||||||||||||||||||||||||||||||||||||").press_enter()
    browser.element('[data-test-id="message-tips-message"]').should(have.text("Yikes! We didn't find any results for"))
#if browser.element(by.text('Accept all')).matching(be.visible):
 #  browser.element(by.text('Accept all')).click()