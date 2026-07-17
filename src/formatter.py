
from math import isnan

from src.constants import CURRENCY_SYMBOL


def format_currency(value):
    """
    Format numeric value into readable currency.
    """

    if value is None:
        return f"{CURRENCY_SYMBOL}0"

    try:
        value = float(value)
    except (TypeError, ValueError):
        return f"{CURRENCY_SYMBOL}0"

    absolute = abs(value)

    if absolute >= 1_000_000_000:
        return f"{CURRENCY_SYMBOL}{value / 1_000_000_000:.2f}B"

    if absolute >= 1_000_000:
        return f"{CURRENCY_SYMBOL}{value / 1_000_000:.2f}M"

    if absolute >= 1_000:
        return f"{CURRENCY_SYMBOL}{value / 1_000:.2f}K"

    return f"{CURRENCY_SYMBOL}{value:,.2f}"


def format_number(value):
    """
    Format large numbers using K, M and B.
    """

    if value is None:
        return "0"

    try:
        value = float(value)
    except (TypeError, ValueError):
        return "0"

    absolute = abs(value)

    if absolute >= 1_000_000_000:
        return f"{value / 1_000_000_000:.2f}B"

    if absolute >= 1_000_000:
        return f"{value / 1_000_000:.2f}M"

    if absolute >= 1_000:
        return f"{value / 1_000:.2f}K"

    if value.is_integer():
        return str(int(value))

    return f"{value:.2f}"


def format_percentage(value):
    """
    Format percentage values.
    """

    if value is None:
        return "0.00%"

    try:
        value = float(value)
    except (TypeError, ValueError):
        return "0.00%"

    return f"{value:.2f}%"


def format_days(value):
    """
    Format shipping days.
    """

    if value is None:
        return "0 Days"

    try:
        value = float(value)
    except (TypeError, ValueError):
        return "0 Days"

    return f"{value:.1f} Days"


def format_decimal(value, digits=2):
    """
    Format decimal values.
    """

    if value is None:
        return "0"

    try:
        value = float(value)
    except (TypeError, ValueError):
        return "0"

    return f"{value:.{digits}f}"


def safe_round(value, digits=2):
    """
    Round values safely.
    """

    try:
        value = float(value)

        if isnan(value):
            return 0

        return round(value, digits)

    except (TypeError, ValueError):
        return 0


def format_profit_margin(profit, sales):
    """
    Calculate and format profit margin.
    """

    try:
        if sales == 0:
            return "0.00%"

        margin = (profit / sales) * 100

        return format_percentage(margin)

    except Exception:
        return "0.00%"


def format_change(value):
    """
    Format positive/negative changes.
    """

    try:
        value = float(value)
    except (TypeError, ValueError):
        return "0.00%"

    if value > 0:
        return f"▲ {value:.2f}%"

    if value < 0:
        return f"▼ {abs(value):.2f}%"

    return "0.00%"


def format_title(title):
    """
    Convert snake_case into Title Case.
    """

    return str(title).replace("_", " ").title()