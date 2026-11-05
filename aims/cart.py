
"""Shopping cart operations for AIMS-mini."""

from decimal import Decimal
from typing import List

from .dvd import DigitalVideoDisc


# Maximum number of DVDs allowed in a cart
MAX_NUMBERS_ORDERED = 20


class Cart:
    """Represent a shopping cart containing DVDs."""

    def __init__(self):
        """Initialize an empty shopping cart."""
        self.items: List[DigitalVideoDisc] = []

    def add_dvd(self, dvd: DigitalVideoDisc) -> bool:
        """
        Add a DVD to the cart.

        Return True if the DVD is added successfully.
        Return False if the cart has reached its maximum capacity.
        """
        if not isinstance(dvd, DigitalVideoDisc):
            raise TypeError("dvd must be a DigitalVideoDisc")

        if len(self.items) >= MAX_NUMBERS_ORDERED:
            return False

        self.items.append(dvd)
        return True

    def remove_dvd(self, dvd: DigitalVideoDisc) -> bool:
        """
        Remove a DVD from the cart.

        Return True if the DVD is removed.
        Return False if the DVD is not found.
        """
        try:
            self.items.remove(dvd)
            return True
        except ValueError:
            return False

    def total_cost(self) -> float:
        """Calculate and return the total cost of all DVDs."""
        total = sum(
            (dvd.cost for dvd in self.items),
            start=Decimal("0")
        )
        return float(total)

    def total_cost_with_discount(self, percent: float) -> float:
        """
        Calculate the total cost after applying a discount.

        Args:
            percent: Discount percentage, from 0 to 100.

        Raises:
            ValueError: If the discount percentage is invalid.
        """
        if not isinstance(percent, (int, float)):
            raise ValueError("percent must be a number")

        if not 0 <= percent <= 100:
            raise ValueError("percent must be between 0 and 100")

        total = sum(
            (dvd.cost for dvd in self.items),
            start=Decimal("0")
        )

        discounted_total = total * Decimal(str(100 - percent)) / Decimal("100")

        return float(discounted_total)

    def sort_by_title(self) -> List[DigitalVideoDisc]:
        """
        Sort DVDs by title in ascending alphabetical order.

        The sorting is case-insensitive.
        """
        self.items.sort(key=lambda dvd: dvd.title.casefold())
        return list(self.items)

    def sort_by_cost(self) -> List[DigitalVideoDisc]:
        """
        Sort DVDs by cost in ascending order.

        DVDs with the same cost are sorted by title.
        """
        self.items.sort(
            key=lambda dvd: (dvd.cost, dvd.title.casefold())
        )
        return list(self.items)

    def print_cart(self) -> str:
        """
        Display the contents of the cart.

        If the cart is empty, display:
            The cart is empty

        Return the displayed content as a string.
        """
        if not self.items:
            output = "The cart is empty"

        else:
            lines = [
                "*********************** CART ***********************"
            ]

            for index, dvd in enumerate(self.items, start=1):
                lines.append(
                    f"{index}. {dvd.title} - {dvd.cost:.2f} $"
                )

            lines.append(
                f"Total cost: {self.total_cost():.2f} $"
            )

            lines.append(
                "*****************************************************"
            )

            output = "\n".join(lines)

        print(output)
        return output


def sort_by_title(items: List[DigitalVideoDisc]) -> List[DigitalVideoDisc]:
    """
    Return a new list of DVDs sorted by title.

    The original list is not modified.
    """
    return sorted(
        items,
        key=lambda dvd: dvd.title.casefold()
    )


def sort_by_cost(items: List[DigitalVideoDisc]) -> List[DigitalVideoDisc]:
    """
    Return a new list of DVDs sorted by cost, then by title.

    The original list is not modified.
    """
    return sorted(
        items,
        key=lambda dvd: (dvd.cost, dvd.title.casefold())
    )
