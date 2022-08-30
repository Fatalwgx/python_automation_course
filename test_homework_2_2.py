from selene.support.shared import browser
from selene import be, have
from pages.locators import MainPageLocators


GOOGLE_MAINPAGE = 'https://google.com/ncr'    # No country redirect main page for consistent results


def test_selene_present_in_google(set_browser_resolution):
    browser.open(GOOGLE_MAINPAGE)
    browser.element(MainPageLocators.SEARCH_FIELD).should(be.blank).type('selene').press_enter()
    assert browser.element(MainPageLocators.SEARCH_OUTPUT).should(have.text(
        'Selene - User-oriented Web UI browser tests in Python'))


def test_selene_not_present_in_google(set_browser_resolution):
    browser.open(GOOGLE_MAINPAGE)
    browser.element(MainPageLocators.SEARCH_FIELD).should(be.blank).type('selene goddess').press_enter()
    assert browser.element(MainPageLocators.SEARCH_OUTPUT).should_not(have.text(
        'Selene - User-oriented Web UI browser tests in Python'))
