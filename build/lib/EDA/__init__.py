# import packages
import pandas as pd
from sqlalchemy import create_engine
import shutil
import os
from pathlib import Path

_HOME = os.getcwd()
print(_HOME)


# list all files in the directory in a tree-like structure
def list_files(start_path):
    """
    This functions lists all the files in a directory in a tree-like structure.
    :param start_path: The top-level directory for which you want the tree-like structure.
    :return: Tree-like structure.
    """
    for root, dirs, files in os.walk(start_path):
        level = root.replace(start_path, '').count(os.sep)
        indent = ' ' * 4 * level
        print('{}{}/'.format(indent, os.path.basename(root)))
        sub_indent = ' ' * 4 * (level + 1)
        for f in files:
            print('{}{}'.format(sub_indent, f))


# create directory if directory does not exist
def create_directory(dir_name):
    """
    This function first checks if a directory exists, and creates the directory if it does not exist.
    :param dir_name: name of the directory
    :return: directory.
    """
    Path(os.path.join(_HOME, dir_name)).mkdir(parents=True, exist_ok=True)


# import
def import_csv(filepath):
    """
    This function imports csv files. This is an interim function for the purpose of development. It will be deprecated
    once the package is pushed into production.
    :param filepath: path of the csv file to import.
    :return: reads the csv into a Pandas dataframe.
    """
    return pd.read_csv(filepath, dayfirst=True, parse_dates=True, index_col=0)


def import_sql(query_string, server, database):
    """
    This function connects to the SQL Server and reads a table into a Pandas dataframe. :param query_string: the SQL
    query to fetch relevant data. This is an interim function for the purpose of development. It will be deprecated
    once the package is pushed into production.
    :param query_string: SQL
    :param server: the server in which contains the database. For testing it is 'CBAS-PDDB-06'; for production it is
    'CBAS-PDDB-07'.
    :param database: the database in which contains the table.
    :return: dataframe.
    """
    engine_string = 'mssql+pyodbc://' + server + '/' + database + '?driver=ODBC+Driver+17+for+SQL+Server'
    engine = create_engine(engine_string)
    dataframe = pd.read_sql(sql=query_string, con=engine)
    print(dataframe.head())
    return dataframe


# clear all existing files
def clear_all():
    """
    This function clears all files in the html and csv directories. Operationally, it deletes the html and csv directories
    and then recreates them. This function should be run before running all other functions.
    :return: Clears html and csv directories.
    """
    print(_HOME)
    shutil.rmtree(os.path.join(_HOME, 'export', 'html'))
    os.mkdir(os.path.join(_HOME, 'export', 'html'))
    shutil.rmtree(os.path.join(_HOME, 'export', 'csv'))
    os.mkdir(os.path.join(_HOME, 'export', 'csv'))


# checks if columns exist, the suffix _dataframe
def if_columns(x):
    """
    This function suffixes '_columns' to a dataframe (when saving it as a file) if columns are specified and
    suffixes '_dataframe' no columns are specified (i.e. when the user wants to do EDA of the entire dataset).
    :param x: list of columns
    :return: '_columns' suffix if list of columns is provided, else '_dataframe'.
    """
    return '_columns' if len(x) != 0 else '_dataframe'


# save to .csv
def if_to_csv(dataframe, prefix, filename, args):
    """
    This function saves the resultant dataframe to the csv directory if the to_csv parameter within standard or custom
    functions is set to True.
    :param dataframe: the resultant dataframe
    :param prefix: Adds relevant prefix ('mt_' for metadata, 'ct_' for central tendency, 'sp_' for spread, 'plt_' for
    plots to the filename.
    :param filename: the name that the user wants to give the file.
    :param args: list of columns (if columns are specified).
    :return: dataframe is saved as a csv file in the csv directory.
    """
    create_directory('csv')
    extension = prefix + filename + if_columns(args) + '.csv'
    path_to_file = os.path.join(_HOME, 'export', 'csv', extension)
    dataframe.to_csv(path_to_file, index=False)

    return None


# save to .html
def if_to_html(dataframe, prefix, filename, args):
    """
    This function saves the resultant dataframe to the html directory if the to_html parameter within standard or custom
    functions is set to True.
    :param dataframe: the resultant dataframe.
    :param prefix: Adds relevant prefix ('mt_' for metadata, 'ct_' for central tendency, 'sp_' for spread, 'plt_' for
    plots to the filename.
    :param filename: the name that the user wants to give the file.
    :param args: list of columns (if columns are specified).
    :return: dataframe is saved as a html file in the html directory.
    """
    create_directory('html')
    extension = prefix + filename + if_columns(args) + '.html'
    path_to_file = os.path.join(_HOME, 'export', 'html', extension)
    dataframe.to_html(path_to_file, index=False)

    return None


# display if 'display' is set to True
def if_display(dataframe, columns_text, dataframe_text, args):
    """
    Display the dataframe if the 'display' parameter is set to true.
    :param dataframe: resultant dataframe that the user needs to display.
    :param columns_text: text to display if the user is conducting EDA for specified columns.
    :param dataframe_text: text to display if the user does not specify any columns, i.e. if the user is
    conducting EDA for the entire dataset.
    :param args: list of columns.
    :return: displays the resultant dataframe.
    """
    print(columns_text) if len(args) != 0 else print(dataframe_text)
    print(dataframe)

    return None


# delete non-numeric rows of a dataframe
def del_non_numeric(dataframe):
    """
    This function deletes the non-numeric rows of the resultant dataframe. It is particularly useful for those functions
    that sometimes return stastical results for non-numeric function (e.g. calculate_max_and_min()). This is because
    of the underlying structure of certain data types wherein they are stored in the system as numbers, but do not
    serve any practical purpose for the end user.
    :param dataframe: the resultant dataframe with numeric results for non-numeric values (e.g. maximum value of company name)
    :return: the resultant dataframe without the numeric results for non-numeric values.
    """
    for idx, row in dataframe.iterrows():
        if type(dataframe["Maximum"].loc[idx]) in ['float', 'float64', 'int', 'int64']:
            dataframe.drop([idx], inplace=True)
        else:
            pass
    return dataframe


# group by certain columns
def group_by(dataframe):
    """
    This function groups an an existing dataframe into groups of certain columns. This will enable operation of different
    functions on such grouped columns.
    :param dataframe: the imported dataframe
    :return: dataframe with grouped columns on which different functions can be applied.
    """
    dataframe_grouped = pd.groupby(dataframe)
    return dataframe_grouped