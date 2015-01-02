#!/usr/bin/python3

from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):

    def get_error_element(self):
        return self.browser.find_element_by_css_selector('.has-error')

    def test_cannot_add_empty_list_items(self):
        # Edith goes home, hits enter on an empty box
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')

        # Gets error message saying no blank items
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # Tries again with text, which works
        self.get_item_input_box().send_keys('Buy milk\n')
        self.check_for_row_in_list_table('1: Buy milk')

        # Perversely, submits second blank
        self.get_item_input_box().send_keys('\n')

        # Same warning on the list page
        self.check_for_row_in_list_table('1: Buy milk')
        error = self.get_error_element()
        self.assertEqual(error.text, "You can't have an empty list item")

        # Can correct the error by adding text
        self.get_item_input_box().send_keys("Make tea\n")
        self.check_for_row_in_list_table('1: Buy milk')
        self.check_for_row_in_list_table('2: Make tea')

    def test_cannot_add_duplicate_items(self):
        # Edith starts a new list from the home page
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('Buy willies\n')
        self.check_for_row_in_list_table('1: Buy willies')

        # She tries to enter the item again out of sheer enthusiasm
        self.get_item_input_box().send_keys('Buy willies\n')

        # There's an error with a message
        self.check_for_row_in_list_table('1: Buy willies')
        error = self.get_error_element()
        self.assertEqual(error.text, "You've already got this in your list")

    def test_error_messages_are_cleared_on_input(self):
        # E. starts a new list in a way that causes a validation error
        self.browser.get(self.server_url)
        self.get_item_input_box().send_keys('\n')
        error = self.get_error_element()
        self.assertTrue(error.is_displayed())

        # She starts typing in the input box to clear the error
        self.get_item_input_box().send_keys('n')

        # Error message disappears
        error = self.get_error_element()
        self.assertFalse(error.is_displayed())



