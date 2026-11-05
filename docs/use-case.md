# AIMS-mini – Use cases

## Actors
- **Customer**: views the demonstration catalogue, searches DVDs and reviews the cart.
- **Developer**: maintains the catalogue, cart and automated tests.

## Main use cases
1. Add a DVD to the cart (maximum 20 items).
2. Remove a DVD from the cart.
3. Display cart contents and total cost.
4. Calculate a discounted total for a valid percentage from 0 to 100.
5. Search DVDs by title (case-insensitive substring).
6. Search DVDs by category (case-insensitive exact category).
7. Sort DVDs by title or by cost.

## Acceptance rules
- The 21st DVD must be rejected; the cart remains at 20 items.
- Searching for `lion` must find `The Lion King` regardless of letter case.
- Empty-cart display must say `The cart is empty`.
- Invalid discount percentages must raise `ValueError`.
