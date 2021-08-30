import matplotlib.pyplot as plt


def format_label(s):
    """Return `s` as a capitalized string with spaces instead of "_"

    Arguments:
      s: label to be formated

    **Usage:**
      ```python
      from paper_utils.plots import format_label

      label = "nb_patentees"
      format_label(label)
      # >>> "Number patentees"
      ```
    """
    return s.replace("_", " ").replace("nb", "number").capitalize()


def df_plot(
    df,
    subplots: bool = False,
    ylabel: str = "",
    legend: bool = True,
    ncol: int = None,
    **kwargs
):
    """
    A simple wrapper around pd.Dataframe.plot

    Arguments:
      df: the dataframe to be plotted
      subplots: whether each columns should be plotted as a subplot
      ylabel: name of the y-axis label
      legend: whether there should be a legend
      ncol: number of columns in legend
      kwargs: key-worded arguments to be passed to pd.Dataframe.plot()

    **Usage:**
        ```python
        from paper_utils.plots import df_plot
        df_plot(tmp)
        ```

    """
    tmp = df.copy()
    tmp.plot(
        subplots=subplots,
        sharey=True,
        sharex=True,
        legend=subplots,
        linewidth=1.5,
        **kwargs
    )  # ,style
    if not subplots:
        plt.ylabel(ylabel)
        if legend:
            ncol = min(5, len(tmp.columns)) if not ncol else ncol
            plt.legend(
                loc="upper center", bbox_to_anchor=(0.5, -0.1), ncol=ncol, frameon=False
            )
