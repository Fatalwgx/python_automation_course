import pytest
from selene.support.shared import browser


def pytest_addoption(parser):
    parser.addoption('--resolution', action='store', default='desktop', help='desktop: 1920x1080, mobile: 390x844')


@pytest.fixture(scope="function")
def set_browser_resolution(request):
    resolution = request.config.getoption('resolution')
    if resolution == 'desktop':
        browser.config.window_width, browser.config.window_height = 1920, 1080
    elif resolution == 'mobile':
        browser.config.window_width, browser.config.window_height = 390, 844
    else:
        print(f'Please choose between "desktop" or "mobile", "{resolution}" is not an option ')
    yield
    print('\nquitting browser')
    browser.quit()
