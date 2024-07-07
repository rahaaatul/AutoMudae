def get_kakera_name(cardsKakera: str) -> str:
    """
    Retrieve the human-readable name corresponding to a given cardsKakera identifier.

    Args:
    cardsKakera (str): The identifier of the cardsKakera, e.g., "kakera", "kakeraP".

    Returns:
    str: The human-readable name associated with the cardsKakera identifier.
         Returns "unknown kakera" if cardsKakera is not found in the mapping.

    Examples:
    >>> get_kakera_name("kakeraP")
    'purple kakera'

    >>> get_kakera_name("kakeraX")
    'unknown kakera'
    """
    kakera_map = {
        "kakera": "kakera",
        "kakeraP": "purple kakera",
        "kakeraB": "blue kakera",
        "kakeraT": "teal kakera",
        "kakeraG": "green kakera",
        "kakeraY": "yellow kakera",
        "kakeraO": "orange kakera",
        "kakeraR": "red kakera",
        "kakeraW": "rainbow kakera",
        "kakeraL": "light kakera",
    }
    return kakera_map.get(cardsKakera, "unknown kakera")


def get_kakera_emoji(cardsKakera: str) -> str:
    """
    Retrieve the emoji corresponding to a given cardsKakera identifier.

    Args:
    cardsKakera (str): The identifier of the cardsKakera, e.g., "kakera", "kakeraP".

    Returns:
    str: The emoji associated with the cardsKakera identifier.
         Returns "❓" if cardsKakera is not found in the mapping.

    Examples:
    >>> get_kakera_emoji("kakeraP")
    '🟣'

    >>> get_kakera_emoji("kakeraX")
    '❓'
    """
    kakera_map = {
        "kakera": "💎",
        "kakeraP": "🟣",
        "kakeraB": "🔵",
        "kakeraT": "🤢",
        "kakeraG": "🟢",
        "kakeraY": "🟡",
        "kakeraO": "🟠",
        "kakeraR": "🔴",
        "kakeraW": "🌈",
        "kakeraL": "⚪",
    }
    return kakera_map.get(cardsKakera, "❓")
