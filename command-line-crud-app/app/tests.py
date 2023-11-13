from django.test import TestCase
from app import models

# Create your tests here.

class TestTheList(TestCase):
    def test_can_create_list(self):
        todolist = models.create_list("Milk", False)

        self.assertEqual(todolist.items, "Milk")
        self.assertEqual(todolist.complete, False)

    def test_can_view_list(self):
        todolist = [
            {
                "items": "Bananas",
                "complete": True
            },
            {
                "items": "Toilet Paper",
                "complete": False
            },
            {
                "items": "Water",
                "complete": True
            },
            {
                "items": "Oil",
                "complete": False
            },
        ]


        for itemslist in todolist:
            models.create_list(
                itemslist["items"],
                itemslist["complete"]
            )

        todolist_s = models.view_list()

        self.assertEqual(len(todolist_s), len(todolist))

    def test_can_findby_item(self):
        finditems = [
            {
                "items": "Bananas",
                "complete": True
            },
            {
                "items": "Toilet Paper",
                "complete": True
            },
            {
                "items": "Water",
                "complete": True
            },
            {
                "items": "Oil",
                "complete": False
            },
        ]


        for itemslist in finditems:
            models.create_list(
                itemslist["items"],
                itemslist["complete"]
            )

        self.assertIsNone(models.search_list("Kiwi"))

        todo_item = models.search_list("Bananas")


        self.assertIsNotNone(todo_item)
        self.assertEqual(todo_item.items, "Bananas")

    def test_can_filter_complete(self):
        filteritems = [
            {
                "items": "Bananas",
                "complete": True
            },
            {
                "items": "Toilet Paper",
                "complete": True
            },
            {
                "items": "Water",
                "complete": True
            },
            {
                "items": "Oil",
                "complete": False
            },
            {
                "items": "Sunflower Seeds",
                "complete": False
            },
        ]

        for itemslist in filteritems:
            models.create_list(
                itemslist["items"],
                itemslist["complete"]
            )

        self.assertEqual(len(models.filter_complete(True)), 3)

    def test_can_update_list(self):
        updatedlist = [
            {
                "items": "Bananas",
                "complete": True
            },
            {
                "items": "Toilet Paper",
                "complete": True
            },
            {
                "items": "Water",
                "complete": True
            },
            {
                "items": "Oil",
                "complete": False
            },
            {
                "items": "Sunflower Seeds",
                "complete": False
            },
        ]

        for itemslist in updatedlist:
            models.create_list(
                itemslist["items"],
                itemslist["complete"]
            )

        models.update_list("Oil", True)
        self.assertEqual(models.search_list("Oil").complete, True)

    def test_can_delete_items(self):
        deletingitems = [
            {
                "items": "Bananas",
                "complete": True
            },
            {
                "items": "Toilet Paper",
                "complete": True
            },
            {
                "items": "Water",
                "complete": True
            },
            {
                "items": "Oil",
                "complete": False
            },
            {
                "items": "Sunflower Seeds",
                "complete": False
            },
        ]

        for itemslist in deletingitems:
            models.create_list(
                itemslist["items"],
                itemslist["complete"]
            )

        models.delete_item("Sunflower Seeds")
        self.assertEqual(len(models.view_list()), 4)