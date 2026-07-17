def currency(value):

    if abs(value) >= 1_000_000:

        return f"${value/1_000_000:.2f}M"

    if abs(value) >= 1_000:

        return f"${value/1000:.1f}K"

    return f"${value:.2f}"


def number(value):

    if value >= 1_000_000:

        return f"{value/1_000_000:.2f}M"

    if value >= 1000:

        return f"{value/1000:.1f}K"

    return str(value)