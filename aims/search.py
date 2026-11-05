"""Search helpers for DVD collections."""

def search_by_title(items, keyword):
    """Find DVDs whose title contains keyword, ignoring letter case."""
    if not isinstance(keyword, str):
        raise TypeError("keyword must be a string")
    key = keyword.strip().casefold()
    if not key:
        return []
    return [dvd for dvd in items if key in dvd.title.casefold()]

def search_by_category(items, category):
    """Find DVDs in a category, ignoring letter case."""
    if not isinstance(category, str):
        raise TypeError("category must be a string")

    key = category.strip().casefold()

    if not key:
        return []

    return [
        dvd for dvd in items
        if dvd.category.casefold() == key
    ]
