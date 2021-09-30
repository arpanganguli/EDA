import inspect
import os
from statistics import multimode

from pandas import DataFrame

from EDA import if_to_csv, if_to_html, if_display, create_directory

_HOME = os.getcwd()
_prefix = 'ct_'


def calculate_mean(dataframe, *args, display=True, to_csv=False, to_html=False) -> DataFrame:
    """
    This function calculates the mean of all *numeric* columns within a Pandas dataframe. Alternately, users can
    specify a list of columns for which they would want to calculate the mean. If the list contains non-numeric columns,
    then the function displays exceptions to the column names.
    :param dataframe: Pandas dataframe.
    :param args: list of column names for which users would like to calculate the mean. Without arguments, Python will
    calculate mean of all numeric columns of the dataframe by default.
    :param display: DEFAULT: True. If display is True, then the function displays the resulting dataframe, else it just
    returns the resulting dataframe.
    :param to_csv: DEFAULT: False. Saves the dataframe in a .csv format within the export/csv folder.
    :param to_html: DEFAULT: False. Saves the dataframe in a .html format within the export/html folder.
    :return: if no arguments are specified, the function returns a Pandas dataframe containing the mean of all numeric
    columns; otherwise it returns a Pandas dataframe containing the mean of the specified list of columns.
    """
    create_directory('export/csv')
    create_directory('export/html')
    _columns = ['Column Name', 'Mean']
    _dataframe = DataFrame([], columns=_columns)
    _filename = inspect.getframeinfo(inspect.currentframe()).function

    for _colname in args or dataframe.columns:
        try:
            _mean_of_column = dataframe[_colname].mean()
            _dataframe = _dataframe.append({'Column Name': _colname, 'Mean': _mean_of_column}, ignore_index=True)
        except TypeError:
            print(f"{_colname}: the mean for this column could not be calculated since it contains non-numeric "
                  f"values.")
    _dataframe.dropna(axis=1, how='all', inplace=True)

    if_display(_dataframe, "Mean of Columns:", "Mean of Dataframe:", args) if display else None
    if_to_csv(_dataframe, _prefix, _filename, args) if to_csv else None
    if_to_html(_dataframe, _prefix, _filename, args) if to_html else None

    return _dataframe


def calculate_median(dataframe, *args, display=True, to_csv=False, to_html=False) -> DataFrame:
    """
    This function calculates the median of all *numeric* columns within a Pandas dataframe. Alternately, users can
    specify a list of columns for which they would want to calculate the median. If the list contains non-numeric
    columns, then the function displays exceptions to the column names.
    :param dataframe: Pandas dataframe.
    :param args: list of column names for which users would like to calculate the median. Without arguments, Python will
    calculate median of all numeric columns of the dataframe by default.
    :param display: DEFAULT: True. If display is True, then the function displays the resulting dataframe, else it just
    returns the resulting dataframe.
    :param to_csv: DEFAULT: False. Saves the dataframe in a .csv format within the export/csv folder.
    :param to_html: DEFAULT: False. Saves the dataframe in a .html format within the export/html folder.s
    :return: if no arguments are specified, the function returns a Pandas dataframe containing the median of all numeric
    columns; otherwise it returns a Pandas dataframe containing the median of the specified list of columns.
    """
    create_directory('export/csv')
    create_directory('export/html')
    _columns = ['Column Name', 'Median']
    _dataframe = DataFrame([], columns=_columns)
    _filename = inspect.getframeinfo(inspect.currentframe()).function

    for _colname in args or dataframe.columns:
        try:
            _median_of_column = dataframe[_colname].median()
            _dataframe = _dataframe.append({'Column Name': _colname, 'Median': _median_of_column},
                                           ignore_index=True)
        except TypeError:
            print(f"{_colname}: the median for this column could not be calculated since it contains non-numeric "
                  f"values.")
    _dataframe.dropna(axis=1, how='all', inplace=True)

    if_display(_dataframe, "Median of Columns:", "Median of Dataframe:", args) if display else None
    if_to_csv(_dataframe, _prefix, _filename, args) if to_csv else None
    if_to_html(_dataframe, _prefix, _filename, args) if to_html else None

    return _dataframe


def calculate_mode(dataframe, *args, display=True, to_csv=False, to_html=False) -> DataFrame:
    """
    This function calculates the mode of all columns within a Pandas dataframe. Alternately, users can
    specify a list of columns for which they would want to calculate the median.
    :param dataframe: Pandas dataframe.
    :param args: list of column names for which users would like to calculate the mode. Without arguments, Python will
    calculate mode of all columns of the dataframe by default.
    :param display: DEFAULT: True. If display is True, then the function displays the resulting dataframe, else it just
    returns the resulting dataframe.
    :param to_csv: DEFAULT: False. Saves the dataframe in a .csv format within the export/csv folder.
    :param to_html: DEFAULT: False. Saves the dataframe in a .html format within the export/html folder.
    :return: if no arguments are specified, the function returns a Pandas dataframe containing the mode of all
             columns; otherwise it returns a Pandas dataframe containing the mode of the specified list of columns.
    """
    create_directory('export/csv')
    create_directory('export/html')
    _columns = ['Column Name', 'Mode']
    _dataframe = DataFrame([], columns=_columns)
    _filename = inspect.getframeinfo(inspect.currentframe()).function

    for _colname in args or dataframe.columns:
        _mode_of_column = multimode(dataframe[_colname])
        _dataframe = _dataframe.append({'Column Name': _colname, 'Mode': _mode_of_column},
                                       ignore_index=True)
    _dataframe.dropna(axis=1, how='all', inplace=True)

    if_display(_dataframe, "Mean of Columns:", "Mean of Dataframe:", args) if display else None
    if_to_csv(_dataframe, _prefix, _filename, args) if to_csv else None
    if_to_html(_dataframe, _prefix, _filename, args) if to_html else None

    return _dataframe
