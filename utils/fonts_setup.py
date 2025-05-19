import matplotlib.pylab as plt
import matplotlib.colors as pltcol
import altair as alt

# Fonts and colours
FONT = "Averta"
TITLE_FONT = "Averta"
FONTSIZE_TITLE = 16
FONTSIZE_SUBTITLE = 13
FONTSIZE_NORMAL = 13

NESTA_COLOURS = [
    "#0000FF",
    "#18A48C",
    "#9A1BBE",
    "#EB003B",
    "#FF6E47",
    "#646363",
    "#0F294A",
    "#97D9E3",
    "#A59BEE",
    "#F6A4B7",
    "#FDB633",
    "#D2C9C0",
    "#FFFFFF",
    "#000000",
]


def nestafont():
    """Define Nesta fonts"""
    return {
        "config": {
            "title": {"font": TITLE_FONT, "anchor": "start"},
            "axis": {"labelFont": FONT, "titleFont": FONT},
            "header": {"labelFont": FONT, "titleFont": FONT},
            "legend": {"labelFont": FONT, "titleFont": FONT},
            "range": {
                "category": NESTA_COLOURS,
                "ordinal": {
                    "scheme": NESTA_COLOURS
                },
            },
        }
    }