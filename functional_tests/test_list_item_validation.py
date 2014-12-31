#!/usr/bin/python3

from .base import FunctionalTest
from unittest import skip

class ItemValidationTest(FunctionalTest):

    def test_cannot_add_empty_list_items(self):
        # Edith goes home, hits enter on an empty box
        self.browser.get(self.server_url)
        inputbox = self.browser.find_element_by_id('id_new_item')


        # Gets error message saying no blank items

        # Tries again with text, which works

        # Peversely, submits second blank

        # Same warning on the list page

        # Can correct the error by adding text
        self.fail('Write the test')
