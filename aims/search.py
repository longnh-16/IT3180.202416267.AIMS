"""Search helpers for DVD collections."""


def search_by_category(items, category):
    """Find DVDs in a category, ignoring letter case."""
    if not isinstance(category, str):
        raise TypeError("category must be a string")
    key = category.strip().casefold()
    if not key:
        return []
    return [dvd for dvd in items if dvd.category.casefold() == key]


def search_by_title(items, keyword):
    return [
        dvd for dvd in items
        if keyword.lower() in dvd.title.lower()
    ]
