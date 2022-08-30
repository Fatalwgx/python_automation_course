from selene.support.shared import browser


def test_fill_and_send_form(set_browser_resolution):
    browser.open('https://demoqa.com/automation-practice-form')
    browser.element('[id="firstName"]').type('Lev')
    browser.element('[id="userEmail"]').type('123@mail.ru')
    browser.element('[id="lastName"]').type('Zavodskov')
    browser.element('[for="gender-radio-1"]').click()
    browser.element('[id="userNumber"]').type('79183134727').press_enter()
    
    assert 'Thanks for submitting the form' in browser.element('[id="example-modal-sizes-title-lg"]').text()
