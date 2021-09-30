from pandas import DataFrame, Series
import os
import inspect
import warnings
from EDA import create_directory

warnings.filterwarnings('ignore')

_HOME = os.getcwd()
_prefix = 'mt_'


def describe_dataframe(dataframe, display=True, to_csv=False, to_html=False) -> DataFrame:
    """
    This function publishes descriptive statistics of different columns of a dataframe.
    *NOTE:* It publishes the descriptive statistics of *numeric* columns only.
    :param display: DEFAULT: True. If display is True, then the function displays the resulting dataframe, else it just
    returns the resulting dataframe.
    :param to_csv: DEFAULT: False. Saves the dataframe in a .csv format within the export/csv folder.
    :param to_html: DEFAULT: False. Saves the dataframe in a .html format within the export/html folder.
    :param dataframe: dataframe
    :return: descriptive statistics of a dataframe in a dataframe format.
    """
    create_directory('export/csv')
    create_directory('export/html')
    _dataframe_describe = dataframe.describe()
    _other_desc_stats = dataframe.agg(['median', 'var', 'skew', 'kurt'])
    _dataframe = _dataframe_describe.append(_other_desc_stats)
    _filename = inspect.getframeinfo(inspect.currentframe()).function

    print(_dataframe) if display else None
    if to_csv:
        _extension = _prefix + _filename + '.csv'
        _path_to_file = os.path.join(_HOME, 'export', 'csv', _extension)
        _dataframe.to_csv(_path_to_file, index=True)
    else:
        pass
    if to_html:
        _extension = _prefix + _filename + '.html'
        _path_to_file = os.path.join(_HOME, 'export', 'html', _extension)
        _dataframe.to_html(_path_to_file, index=True)
    else:
        pass
    return _dataframe


def display_column_names(dataframe, display=True, to_csv=False, to_html=False) -> DataFrame:
    """
    This function displays the names of columns of a dataframe as a list of column names.
    :param dataframe: name of the dataframe.
    :param display: DEFAULT: True. If display is True, then the function displays the resulting dataframe, else it just
    returns the resulting dataframe.
    :param to_csv: DEFAULT: False. Saves the dataframe in a .csv format within the export/csv folder.
    :param to_html: DEFAULT: False. Saves the dataframe in a .html format within the export/html folder.
    :return: list of column names.
    """
    create_directory('export/csv')
    create_directory('export/html')
    list_of_columns = list(dataframe.columns.values.tolist())
    _dataframe = DataFrame(list_of_columns, columns=['List of columns'])
    _filename = inspect.getframeinfo(inspect.currentframe()).function
    if display:
        print(_dataframe)
    else:
        pass
    if to_csv:
        _extension = _prefix + _filename + '.csv'
        _path_to_file = os.path.join(_HOME, 'export', 'csv', _extension)
        _dataframe.to_csv(_path_to_file, index=False)
    else:
        pass
    if to_html:
        _extension = _prefix + _filename + '.html'
        _path_to_file = os.path.join(_HOME, 'export', 'html', _extension)
        _dataframe.to_html(_path_to_file, index=False)
    else:
        pass
    return _dataframe


def display_data_types(dataframe, display=True, to_csv=False, to_html=False) -> DataFrame:
    """
    This function displays the data types of all (specified) columns in a dataframe.
    :param dataframe: name of the dataframe.
    :param display: DEFAULT: True. If display is True, then the function displays the resulting dataframe, else it just
    returns the resulting dataframe.
    :param to_csv: DEFAULT: False. Saves the dataframe in a .csv format within the export/csv folder.
    :param to_html: DEFAULT: False. Saves the dataframe in a .html format within the export/html folder.
    :return: returns the dataframe with data types.
    """
    create_directory('export/csv')
    create_directory('export/html')
    type_list = list()
    for _colname in dataframe.columns:
        type_list.append(dataframe[_colname].dtypes.__str__())
    _dataframe = DataFrame([], columns=['Variable', 'Data Types'])
    _dataframe['Variable'] = Series(dataframe.columns)
    _dataframe['Data Types'] = Series(type_list)
    _filename = inspect.getframeinfo(inspect.currentframe()).function
    if display:
        print(_dataframe)
    else:
        pass
    if to_csv:
        _extension = _prefix + _filename + '.csv'
        _path_to_file = os.path.join(_HOME, 'export', 'csv', _extension)
        _dataframe.to_csv(_path_to_file)
    else:
        pass
    if to_html:
        _extension = _prefix + _filename + '.html'
        _path_to_file = os.path.join(_HOME, 'export', 'html', _extension)
        _dataframe.to_html(_path_to_file)
    else:
        pass
    return _dataframe


def display_shape(dataframe, display=True, to_csv=False, to_html=False) -> DataFrame:
    """
    This function displays the rows and columns of the dataframe.
    :param dataframe: Pandas dataframe.
    :param display: DEFAULT: True. If display is True, then the function displays the resulting dataframe, else it just
    returns the resulting dataframe.
    :param to_csv: DEFAULT: False. Saves the dataframe in a .csv format within the export/csv folder.
    :param to_html: DEFAULT: False. Saves the dataframe in a .html format within the export/html folder.
    :return: the shape of the dataframe.
    """
    create_directory('export/csv')
    create_directory('export/html')
    _dataframe_shape = dataframe.shape
    _rows = _dataframe_shape[0]
    _columns = _dataframe_shape[1]
    _dataframe = DataFrame(dataframe.shape, columns=['Shape'])
    _dataframe.insert(0, 'Features', ['Number of rows', 'Number of columns'])
    _filename = inspect.getframeinfo(inspect.currentframe()).function
    if display:
        print("Number of rows:", _dataframe.iloc[0][1])
        print("Number of columns:", _dataframe.iloc[1][1])
    else:
        pass
    if to_csv:
        _extension = _prefix + _filename + '.csv'
        _path_to_file = os.path.join(_HOME, 'export', 'csv', _extension)
        _dataframe.to_csv(_path_to_file, index=False)
    else:
        pass
    if to_html:
        _extension = _prefix + _filename + '.html'
        _path_to_file = os.path.join(_HOME, 'export', 'html', _extension)
        _dataframe.to_html(_path_to_file, index=False)
    else:
        pass
    return _dataframe
