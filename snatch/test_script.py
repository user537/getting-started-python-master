# test_script.py

import pytest
from selene import browser
from page_object import SeleniumPracticePage


def test_set_user_details():
    # Instantiate the page object
    page = SeleniumPracticePage()

    # Open the target URL
    page.open()

    # Set the user details
    page.set_name('qweqwe')
    page.set_email('qweqwe@qwe.qwe')
    page.set_mobile('1234567890')
    page.set_subjects('Science')
    # todo page.set_address('123 Main St')

    # Close the browser
    browser.quit()


# Running the test
if __name__ == "__main__":
    pytest.main([__file__])
