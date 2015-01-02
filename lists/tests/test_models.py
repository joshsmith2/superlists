from django.test import TestCase
from django.core.exceptions import ValidationError
from lists.models import Item, List

class ItemModelTest(TestCase):

    def test_default_text(self):
        item = Item()
        self.assertEqual(item.text, '')

    def test_item_is_related_to_list(self):
        list_ = List.objects.create()
        item = Item()
        item.list = list_
        item.save()
        self.assertIn(item, list_.item_set.all())

    def test_cannot_save_empty_items(self):
        list_ = List.objects.create()
        item = Item(list=list_, text="")
        with self.assertRaises(ValidationError): #NICE
            item.save()
            item.full_clean()

    def test_duplicate_items_are_invalid(self):
        list_ = List.objects.create()
        Item.objects.create(list=list_, text='bla')
        with self.assertRaises(ValidationError):
            item = Item(list=list_, text='bla')
            item.full_clean()

    def test_can_save_same_item_to_different_lists(self):
        list_1 = List.objects.create()
        list_2 = List.objects.create()
        Item.objects.create(list=list_1, text='bla')
        item = Item(list=list_2, text='bla')
        item.full_clean() # Should not raise

    def test_list_ordering(self):
        list_1 = List.objects.create()
        item_1 = Item.objects.create(list=list_1, text = 'i1')
        item_2 = Item.objects.create(list=list_1, text = 'i2')
        item_3 = Item.objects.create(list=list_1, text = 'i3')
        self.assertEqual(
            list(Item.objects.all()),
            [item_1, item_2, item_3]
        )

    def test_string_representation(self):
        item = Item(text='some_text')
        self.assertEqual(str(item), 'some_text')

class ListModelTest(TestCase):

    def test_get_absolute_url(self):
        list_ = List.objects.create()
        self.assertEqual(list_.get_absolute_url(), '/lists/%d/' % (list_.id))
