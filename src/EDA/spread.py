import inspect

from pandas import DataFrame, Series, concat

from EDA import if_to_csv, if_to_html, if_display, del_non_numeric, create_directory

_prefix = 'sp_'


def calculate_max_and_min(dataframe, *args, display=True, to_csv=False, to_html=False) -> DataFrame:
    """
    This function calculates the maximum and minimum value of all *numeric* columns within a Pandas dataframe.
    Alternately, users can specify a list of columns for which they would want to calculate the maximum and minimum
    value. If the list contains non-numeric columns, then the function displays exceptions to the column names.
    :param dataframe: Pandas dataframe.
    :param args: list of column names for which users would like to calculate the maximum and minimum value. Without
    arguments, Python will calculate maximum and minimum value of all numeric columns of the dataframe by default.
    :param display: DEFAULT: True. If display is True, then the function
    displays the resulting dataframe, else it just returns the resulting dataframe.
    :param to_csv: DEFAULT: False. Saves the dataframe in a .csv format within the export/csv folder.
    :param to_html: DEFAULT: False. Saves the dataframe in a .html format within the export/html folder.
    :return: if no arguments are specified, the function returns a Pandas dataframe containing the maximum and minimum
    value of all numeric columns; otherwise it returns a Pandas dataframe containing the maximum and minimum value of
    the specified list of columns.
    """
    create_directory('export/csv')
    create_directory('export/html')
    _columns = ['Column Name', 'Maximum', 'Minimum']
    _dataframe = DataFrame([], columns=_columns)
    _filename = inspect.getframeinfo(inspect.currentframe()).function

    for _colname in args or dataframe.columns:
        try:
            _max_of_column = dataframe[_colname].max(skipna=True)
            _min_of_column = dataframe[_colname].min(skipna=True)
            _dataframe = _dataframe.append({'Column Name': _colname, 'Maximum': _max_of_column,
                                            'Minimum': _min_of_column}, ignore_index=True)
        except TypeError or _dataframe[_colname].dtype in ['O', '<M8[ns]', 'bool', 'numpy.bool_']:
            print(f"{_colname}: the maximum and minimum for this column could not be calculated since it contains "
                  f"non-numeric values.")
    _dataframe.dropna(axis=1, how='all', inplace=True)
    # del_non_numeric(_dataframe)

    if_display(_dataframe, "Maximum and Minimum of Columns:", "Maximum and Minimum of Dataframe:",
               args) if display else None
    if_to_csv(_dataframe, _prefix, _filename, args) if to_csv else None
    if_to_html(_dataframe, _prefix, _filename, args) if to_html else None

    return _dataframe


def calculate_std_and_var(dataframe, *args, display=True, to_csv=False, to_html=False) -> DataFrame:
    """
    This function calculates the standard deviation and variance of all *numeric* columns within a Pandas dataframe.
    Alternately, users can specify a list of columns for which they would want to calculate the standard deviation and
    variance. If the list contains non-numeric columns, then the function displays exceptions to the column names.
    :param dataframe: Pandas dataframe.
    :param args: list of column names for which users would like to calculate the standard deviation and variance.
    Without arguments, Python will calculate standard deviation and variance of all numeric columns of the dataframe
    by default.
    :param display: DEFAULT: True. If display is True, then the function displays the resulting dataframe, else it just
    returns the resulting dataframe.
    :param to_csv: DEFAULT: False. Saves the dataframe in a .csv format within the export/csv folder.
    :param to_html: DEFAULT: False. Saves the dataframe in a .html format within the export/html folder.
    :return: if no arguments are specified, the function returns a Pandas dataframe containing the standard deviation
    and variance of all numeric columns; otherwise it returns a Pandas dataframe containing the standard deviation and
    variance of the specified list of columns.
    """
    create_directory('export/csv')
    create_directory('export/html')
    _columns = ['Column Name', 'Standard Deviation', 'Variance']
    _dataframe = DataFrame([], columns=_columns)
    _filename = inspect.getframeinfo(inspect.currentframe()).function
    for _colname in args or dataframe.columns:
        try:
            _std_of_column = dataframe[_colname].std(skipna=True)
            _var_of_column = dataframe[_colname].var(skipna=True)
            _dataframe = _dataframe.append({'Column Name': _colname, 'Standard Deviation': _std_of_column,
                                            'Variance': _var_of_column}, ignore_index=True)
        except TypeError:
            print(f"{_colname}: the standard deviation and variation for this column could not be calculated since "
                  f"it contains non-numeric values.")
    _dataframe.dropna(axis=1, how='all', inplace=True)

    if_display(_dataframe, "Standard Deviation and Variance of columns:", "Standard Deviation and "
                                                                          "Variance of dataframe:",
               args) if display else None
    if_to_csv(_dataframe, _prefix, _filename, args) if to_csv else None
    if_to_html(_dataframe, _prefix, _filename, args) if to_html else None

    return _dataframe


def calculate_iqr(dataframe, *args, display=True, to_csv=False, to_html=False) -> DataFrame:
    """
    This function calculates the interquartile range of all *numeric* columns within a Pandas dataframe.
    Alternately, users can specify a list of columns for which they would want to calculate the interquartile range.
    If the list contains non-numeric columns, then the function displays exceptions to the column names.
    :param dataframe: Pandas dataframe.
    :param args: list of column names for which users would like to calculate the interquartile range.
    Without arguments, Python will calculate the interquartile range of all numeric columns of the dataframe
    by default.
    :param display: DEFAULT: True. If display is True, then the function displays the resulting dataframe, else it just
    returns the resulting dataframe.
    :param to_csv: DEFAULT: False. Saves the dataframe in a .csv format within the export/csv folder.
    :param to_html: DEFAULT: False. Saves the dataframe in a .html format within the export/html folder.
    :return: if no arguments are specified, the function returns a Pandas dataframe containing the interquartile range
    of all numeric columns; otherwise it returns a Pandas dataframe containing the interquartile range of the specified
    list of columns.
    """
    create_directory('export/csv')
    create_directory('export/html')
    _columns = ['Column Name', 'Interquartile Range']
    _dataframe = DataFrame([], columns=_columns)
    _filename = inspect.getframeinfo(inspect.currentframe()).function

    for _colname in args or dataframe.columns:
        try:
            _iqr_of_column = dataframe[_colname].quantile(q=0.75) - dataframe[_colname].quantile(q=0.25)
            _dataframe = _dataframe.append({'Column Name': _colname, 'Interquartile Range': _iqr_of_column},
                                           ignore_index=True)
        except TypeError:
            print(f"{_colname}: the interquartile range for this column could not be calculated since "
                  f"it contains non-numeric values.")
    _dataframe.dropna(axis=1, how='all', inplace=True)

    if_display(_dataframe, "Interquartile Range of Columns:", "Interquartile Range of Dataframe:",
               args) if display else None
    if_to_csv(_dataframe, _prefix, _filename, args) if to_csv else None
    if_to_html(_dataframe, _prefix, _filename, args) if to_html else None

    return _dataframe


def calculate_zscore(dataframe, *args, ddof=0, display=True, to_csv=False, to_html=False) -> DataFrame:
    """
    This function calculates the z-score of all *numeric* columns within a Pandas dataframe.
    Alternately, users can specify a list of columns for which they would want to calculate the z-score.
    If the list contains non-numeric columns, then the function displays exceptions to the column names.
    :rtype: object
    :param dataframe: Pandas dataframe.
    :param args: list of column names for which users would like to calculate the z-score.
    Without arguments, Python will calculate the z-score of all numeric columns of the dataframe
    by default.
    :param ddof: DEFAULT: 0. Degrees of freedom.
    :param display: DEFAULT: True. If display is True, then the function displays the resulting dataframe, else it just
    returns the resulting dataframe.
    :param to_csv: DEFAULT: False. Saves the dataframe in a .csv format within the export/csv folder.
    :param to_html: DEFAULT: False. Saves the dataframe in a .html format within the export/html folder.
    :return: if no arguments are specified, the function returns a Pandas dataframe containing the z-score
    of all numeric columns; otherwise it returns a Pandas dataframe containing the z-score of the specified
    list of columns.
    """
    create_directory('export/csv')
    create_directory('export/html')
    _colnames = args if len(args) != 0 else dataframe.columns
    _filename = inspect.getframeinfo(inspect.currentframe()).function
    _zscore_series = Series([])

    for _colname in args or dataframe.columns:
        try:
            _zscore_of_column = ((dataframe[_colname] - dataframe[_colname].mean()) / dataframe[_colname].std(
                ddof=ddof)).T
            _zscore_series = concat([_zscore_series, _zscore_of_column], axis=1)
        except TypeError:
            print(f"{_colname}: the z-score for this column could not be calculated since "
                  f"it contains non-numeric values.")
    _dataframe = DataFrame(_zscore_series, columns=_colnames)
    _dataframe.dropna(axis=1, how='all', inplace=True)

    if_display(_dataframe, "ZScore of Columns:", "ZScore of Dataframe:", args) if display else None
    if_to_csv(_dataframe, _prefix, _filename, args) if to_csv else None
    if_to_html(_dataframe, _prefix, _filename, args) if to_html else None

    return _dataframe
