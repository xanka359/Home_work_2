from selene import browser, be, have
import pytest

def test_search():
    browser.open("https://www.ecosia.org")
    browser.element('[name="q"]').should(be.blank).type("????????????????????????????????|||||||||||||||||||||||||||||||||||||||||||||||||||").press_enter()
    browser.element('[data-test-id="message-tips-message"]').should(have.text("Yikes! We didn't find any results for"))

def test_search_1():
    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))