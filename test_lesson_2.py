    from selene.support.shared import browser
    from selene import be, have

    browser.open('https://google.com')
    browser.element('[name="q"]').should(be.blank).type('yashaka/selene').press_enter()
    browser.element('[id="search"]').should(have.text('Selene - User-oriented Web UI browser tests in Python'))


import pytest


@pytest.fixture()
def browser():
        return  "Chrome"


def test_addition(browser):
    assert browser == "Chrome"
    a = 1 + 2
    assert a == 3