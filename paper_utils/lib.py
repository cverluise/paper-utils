FIGSIZE_md = (9, 6)
FIGSIZE_lg = (6, 12)

COUNTRY_TIMESPAN = {
    "DD": (1950, 1992),
    "DE": (1877, 2010),
    "FR": (1905, 2010),
    "GB": (1893, 2010),
    "US": (1836, 2010),
}
COUNTRY_PATEE_TIMESPAN = {
    "DD": {"ASG": (1950, 1992), "INV": (1950, 1992)},
    "DE": {"ASG": (1877, 2010), "INV": (1950, 2010)},
    "FR": {"ASG": (1905, 2010), "INV": (1980, 2010)},
    "GB": {"ASG": (1950, 2010), "INV": (1893, 2010)},
    "US": {"ASG": (1930, 2010), "INV": (1836, 2010)},
}

STYLE = (["-"] * 5 + ["--"] * 5 + [".-"] * 5 + [":"] * 5) * 10
COLOR = [
    "#00004d",
    "#2f326d",
    "#53648d",
    "#7999ad",
    "#a8cfcb",
    "#ffb9ab",
    "#e7797a",
    "#ba424e",
    "#801428",
    "#3f0000",
] * 10
# https://gka.github.io/palettes

offices = [
    "US",
    "CN",
    "EP",
    "JP",
    "GB",
    "FR",
    "DE",
    "IT",
    "CA",
    "KR",
    "BR",
    "RU",
    "IN",
    "ZA",
]
technologies = [
    "additivemanufacturing",
    "blockchain",
    "computervision",
    "genomeediting",
    "hydrogenstorage",
    "naturallanguageprocessing",
    "selfdrivingvehicle",
]