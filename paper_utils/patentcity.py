import numpy as np
from typing import Dict, List


def query_country_timespan(
    df,
    country_timespan: Dict,
    to_nan: List,
    country_code: str = "country_code",
    publication_year: str = "publication_year",
):
    """
    Truncate `df` based on `country_code` and `publication_year` as defined in `country_timespan`

    Arguments:
        df: dataframe
        country_timespan: dict defining the timespan to be considered for each country
        to_nan: list of variables to be set to null for DE between 1945 and 1950
        country_code: name of the country_code variable
        publication_year: name of the publication_year variable

    **Usage:**
        ```python
        from paper_utils.patentcity import query_country_timespan
        from paper_utils.lib import COUNTRY_TIMESPAN

        tmp = query_country_timespan(df, COUNTRY_TIMESPAN, ["nb_patentees"])
        ```
    """
    country_timespan_clause = (
        lambda cc, y: f"""({country_code}=="{cc}" and {y[0]}<={publication_year}<={y[1]})"""
    )
    tmp = df.query(
        " or ".join(
            [country_timespan_clause(cc, y) for cc, y in country_timespan.items()]
        )
    ).copy()

    if to_nan:
        force_nan_de = [
            all(bools)
            for bools in zip(
                (tmp["country_code"] == "DE").values,
                (1945 < tmp[publication_year]).values,
                (1950 > tmp[publication_year]).values,
            )
        ]
        tmp.loc[force_nan_de, to_nan] = np.nan

    return tmp
