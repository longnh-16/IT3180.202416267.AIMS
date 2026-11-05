
"""Main entry point for the AIMS-mini application."""

from aims import Cart, DigitalVideoDisc, __version__
from aims.search import search_by_title


def build_demo_cart():
    """
    Create a shopping cart containing sample DVDs.

    The total cost of the sample cart is 63.89 $.
    """
    cart = Cart()

    dvd1 = DigitalVideoDisc(
        "The Lion King",
        "Animation",
        "19.95"
    )

    dvd2 = DigitalVideoDisc(
        "Star Wars",
        "Science Fiction",
        "24.95"
    )

    dvd3 = DigitalVideoDisc(
        "Aladdin",
        "Animation",
        "18.99"
    )

    cart.add_dvd(dvd1)
    cart.add_dvd(dvd2)
    cart.add_dvd(dvd3)

    return cart


def demonstrate_cart(cart):
    """Display the contents and total cost of the shopping cart."""
    print("\n========== SHOPPING CART ==========")

    # Display all DVDs in the cart.
    cart.print_cart()

    print("===================================")


def demonstrate_search(cart):
    """Demonstrate searching DVDs by title."""
    keyword = "lion"

    print(f"\nSearch results for '{keyword}':")

    matches = search_by_title(cart.items, keyword)

    if not matches:
        print("No matching DVDs found.")
        return

    for index, dvd in enumerate(matches, start=1):
        print(
            f"{index}. {dvd.title} "
            f"({dvd.category}) - {dvd.cost:.2f} $"
        )


def main():
    """Run the AIMS-mini demonstration."""
    print("=" * 50)
    print(f"Welcome to AIMS-mini v{__version__}")
    print("=" * 50)

    # Step 1: Create a sample shopping cart.
    cart = build_demo_cart()

    # Step 2: Display the shopping cart.
    demonstrate_cart(cart)

    # Step 3: Display the total cost.
    print(f"\nTotal cost: {cart.total_cost():.2f} $")

    # Step 4: Demonstrate searching DVDs by title.
    demonstrate_search(cart)

    print("\nAIMS-mini demonstration completed.")


if __name__ == "__main__":
    main()
