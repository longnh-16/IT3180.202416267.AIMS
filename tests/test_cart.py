import unittest

from aims.cart import Cart, MAX_NUMBERS_ORDERED
from aims.dvd import DigitalVideoDisc


class TestCart(unittest.TestCase):
    def test_total_cost(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A", cost=10))
        cart.add_dvd(DigitalVideoDisc("B", cost=12.5))
        self.assertEqual(cart.total_cost(), 22.5)

    def test_add_dvd_until_full(self):
        cart = Cart()
        for index in range(MAX_NUMBERS_ORDERED):
            self.assertTrue(cart.add_dvd(DigitalVideoDisc(f"DVD {index}", cost=1)))
        self.assertFalse(cart.add_dvd(DigitalVideoDisc("DVD 21", cost=1)))
        self.assertEqual(len(cart.items), MAX_NUMBERS_ORDERED)

    def test_remove_dvd(self):
        cart = Cart()
        dvd = DigitalVideoDisc("A", cost=5)
        self.assertTrue(cart.add_dvd(dvd))
        self.assertTrue(cart.remove_dvd(dvd))
        self.assertFalse(cart.remove_dvd(dvd))

    def test_discount_and_validation(self):
        cart = Cart()
        cart.add_dvd(DigitalVideoDisc("A", cost=100))
        self.assertEqual(cart.total_cost_with_discount(20), 80.0)
        with self.assertRaises(ValueError):
            cart.total_cost_with_discount(150)

    def test_print_empty_cart(self):
        cart = Cart()
        self.assertEqual(cart.print_cart(), "The cart is empty")


if __name__ == "__main__":
    unittest.main()
