def get_technology(table: str, technology: str):
    technology = technology if technology else table.split("_")[-3]
    return technology


def get_model(table: str, model: str = None):
    model = model if model else table.split("_")[-1]
    return model


import numpy as np
from typing import Dict, List


def query_country_timespan(
    df,
    technology_timespan: Dict,
    technology: str = "technology",
    publication_year: str = "publication_year",
):
    """
    Truncate `df` based on `technology` and `publication_year` as defined in `technology_timespan`

    Arguments:
        df: dataframe
        technology_timespan: dict defining the timespan to be considered for each technology
        technology: name of the technology variable
        publication_year: name of the publication_year variable

    **Usage:**
        ```python
        from paper_utils.techdiff import query_technology_timespan
        from paper_utils.lib import TECHNOLOGY_TIMESPAN

        tmp = query_country_timespan(df, COUNTRY_TIMESPAN)
        ```
    """
    country_timespan_clause = (
        lambda cc, y: f"""({technology}=="{cc}" and {y[0]}<={publication_year}<={y[1]})"""
    )
    tmp = df.query(
        " or ".join(
            [country_timespan_clause(cc, y) for cc, y in technology_timespan.items()]
        )
    ).copy()

    return tmp
