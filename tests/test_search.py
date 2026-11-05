import unittest

from aims.dvd import DigitalVideoDisc
from aims.search import search_by_category, search_by_title
from aims.cart import sort_by_title, sort_by_cost


class TestSearchAndSort(unittest.TestCase):
    def setUp(self):
        self.items = [
            DigitalVideoDisc("The Lion King", "Animation", 19.95),
            DigitalVideoDisc("Star Wars", "Science Fiction", 24.95),
            DigitalVideoDisc("Aladdin", "Animation", 18.99),
        ]

    def test_search_title_case_insensitive(self):
        result = search_by_title(self.items, "lion")
        self.assertEqual(
            [dvd.title for dvd in result],
            ["The Lion King"]
    )

    def test_search_category_case_insensitive(self):
        self.assertEqual([d.title for d in search_by_category(self.items, "animation")],
                         ["The Lion King", "Aladdin"])

    def test_search_category_case_insensitive(self):
        self.assertEqual(
            [d.title for d in search_by_category(self.items, "animation")],
            ["The Lion King", "Aladdin"]
    )

    def test_sort_by_title_and_cost(self):
        self.assertEqual([d.title for d in sort_by_title(self.items)],
                         ["Aladdin", "Star Wars", "The Lion King"])
        self.assertEqual([d.title for d in sort_by_cost(self.items)],
                         ["Aladdin", "The Lion King", "Star Wars"])


if __name__ == "__main__":
    unittest.main()
