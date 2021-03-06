# Exploratory Data Analysis (EDA)

**`Current version: 0.1`**

## Introduction

This Python package enables the user to perform exploratory data analysis (EDA) by being able to run a
customisable set of EDA functions on their data, so they can understand the data and judge where data quality issues
may lie. This will also help users avoid writing duplicate code to solve equivalent problems.

## Installation

There are a few steps required to install the package. These are as follows -

* Type in the command: `pip install git+https://github.com/arpanganguli/EDA.git#egg=EDA`.
* You can check if the package has correctly installed by just type `import EDA` into a new Python module.

## Usage

There are multiple commands that will allow the users to conduct various forms of EDA, plot them, publish and export
interactive HTMLs (which the user can share with others).

### Import

* Users can import the package by using the `import` command: `import EDA`.
* If users want to import a particular subpackage, then they can import it directly by typing
  `from EDA import <subpackage>`. E.g. if you want to import `central_tendency`, you can type in
  `from EDA import central_tendency`.

### Generic functions

These functions provide auxiliary support to main functions.

* **`list_files`:** This functions lists all the files in a directory in a tree-like structure.

  * Parameters:
    * **`start_path`:** The top-level directory for which you want the tree-like structure.
  * Returns:
    * Tree-like structure of the entire directory.

* **`create_directory`:** This function first checks if a directory exists, and creates the directory if it does not exist.

  * Parameters:
    * **`dir_name`:** Name of the directory.
  * Returns:
    * Directory.

* **`import_csv`:** This function imports csv files. This is an interim function for the purpose of development. It will be deprecated
    once the package is pushed into production.
  * Parameters:
    * **`filepath`:** path of the csv file to import.
  * Returns:
    * Reads the csv into a Pandas dataframe.

* **`import_sql`:** This function connects to the SQL Server and reads a table into a Pandas dataframe. :param query_string: the SQL
    query to fetch relevant data. This is an interim function for the purpose of development. It will be deprecated
    once the package is pushed into production.
  * **`query_string`:** SQL
  * **`server`:** the server in which contains the database.
  * **`database`:** the database in which contains the table.

* **`clear_all`:** This function clears all files in the html and csv directories. Operationally, it deletes the html and csv directories and then recreates them. This function should be run before running all other functions.
  * Clears `export/html` and `export/csv` directories, which the package creates in the same directory as the user created Python module.

* **`if_columns:`** This function suffixes `_columns` to a dataframe (when saving it as a file) if columns are specified and
    suffixes `_dataframe` no columns are specified (i.e. when the user wants to do EDA of the entire dataset).

* if_to_csv: This function saves the resultant dataframe to the csv directory if the to_csv parameter within standard or custom
    functions is set to `True`.

### Metadata

* **`describe_dataframe`:** This function publishes descriptive statistics of different columns of a dataframe.
  **NOTE:** It publishes the descriptive statistics of *numeric* columns only.
* **`display_column_names`:** This function displays the names of columns of a dataframe as a list of column names.
* **`display_data_types`:** This function displays the data types of all (specified) columns in a dataframe.
* **`display_shape`:** This function displays the rows and columns of the dataframe.

### Central Tendency

* **`calculate_mean`:** This function calculates the mean of all *numeric* columns within a Pandas dataframe.
  Alternately, users can specify a list of columns for which they would want to calculate the mean. If the list contains non-numeric columns, then the function displays exceptions to the column names.

  * Parameters:
    * **`dataframe`:** Pandas dataframe.
    * **`args`:** List of column names for which users would like to calculate the mean. Without arguments, Python will
      calculate mean of all numeric columns of the dataframe by default.
    * **`display`:** DEFAULT: `True`. If display is True, then the function displays the resulting dataframe, else it just
      returns the resulting dataframe.
    * **`to_csv`:** DEFAULT: `False`. Saves the dataframe in a .csv format within the export/csv folder.
    * **`to_html`:** DEFAULT: `False`. Saves the dataframe in a .html format within the export/html folder.
  * Returns:
    * If no arguments are specified, the function returns a Pandas dataframe containing the mean of all numeric
      columns;
    * Otherwise, it returns a Pandas dataframe containing the mean of the specified list of columns.
* **`calculate_median`:** This function calculates the median of all *numeric* columns within a Pandas dataframe.
  Alternately, users can specify a list of columns for which they would want to calculate
  the median. If the list contains non-numeric columns, then the function displays exceptions to
  the column names.

  * Parameters:
    * **`dataframe`:** Pandas dataframe.
    * **`args`:** List of column names for which users would like to calculate the median. Without arguments, Python will
      calculate median of all numeric columns of the dataframe by default.
    * **`display`:** DEFAULT: `True`. If display is True, then the function displays the resulting dataframe, else it just
      returns the resulting dataframe.
    * **`to_csv`:** DEFAULT: `False`. Saves the dataframe in a .csv format within the export/csv folder.
    * **`to_html`:** DEFAULT: `False`. Saves the dataframe in a .html format within the export/html folder.
  * Returns:
    * If no arguments are specified, the function returns a Pandas dataframe containing the median of all numeric
      columns
    * Otherwise, it returns a Pandas dataframe containing the median of the specified list of columns.
* **`calculate_mode`:** This function calculates the mode of all columns within a Pandas dataframe. Alternately, users can
  specify a list of columns for which they would want to calculate the median.

  * Parameters:
    * **`dataframe`:** Pandas dataframe.
    * **`args`:** List of column names for which users would like to calculate the mode. Without arguments, Python will
      calculate the mode of all columns of the dataframe by default.
    * **`display`:** DEFAULT: `True`. If display is True, then the function displays the resulting dataframe, else it just
      returns the resulting dataframe.
    * **`to_csv`:** DEFAULT: `False`. Saves the dataframe in a .csv format within the export/csv folder.
    * **`to_html`:** DEFAULT: `False`. Saves the dataframe in a .html format within the export/html folder.
  * Returns:
    * If no arguments are specified, the function returns a Pandas dataframe containing the mode of all columns
    * Otherwise, it returns a Pandas dataframe containing the mode of the specified list of columns.

### Spread

* **`calculate_max_and_min`:** This function calculates the maximum and minimum value of all *numeric* columns within a Pandas dataframe. Alternately, users can specify a list of columns for which they would want to calculate the maximum and minimum value. If the list contains non-numeric columns, then the function displays exceptions to the column names.
  * Parameters:
    * **`dataframe`:** Pandas dataframe.
    * **`args`:** List of column names for which users would like to calculate the maximum and minimum value. Without
      arguments, Python will calculate maximum and minimum value of all numeric columns of the dataframe by default.
    * **`display`:** DEFAULT: `True`. If display is True, then the function
      displays the resulting dataframe, else it just returns the resulting dataframe.
    * **`to_csv`:** DEFAULT: `False`. Saves the dataframe in a .csv format within the export/csv folder.
    * **`to_html`:** DEFAULT: `False`. Saves the dataframe in a .html format within the export/html folder.
  * Returns:
    * If no arguments are specified, the function returns a Pandas dataframe containing the maximum and minimum
    value of all numeric columns
    * Otherwise, it returns a Pandas dataframe containing the maximum and minimum value of the specified list of columns.
* **`calculate_std_and_var`:** This function calculates the standard deviation and variance of all *numeric* columns within a Pandas dataframe. Alternately, users can specify a list of columns for which they would want to calculate the standard deviation and variance. If the list contains non-numeric columns, then the function displays exceptions to the column names.
  * Parameters:
    * **`dataframe`:** Pandas dataframe.
    * **`args`:** List of column names for which users would like to calculate the standard deviation and variance.
    Without arguments, Python will calculate standard deviation and variance of all numeric columns of the dataframe
    by default.
    * **`display`:** DEFAULT: `True`. If display is True, then the function displays the resulting dataframe, else it just
    returns the resulting dataframe.
    * **`to_csv`:** DEFAULT: `False`. Saves the dataframe in a .csv format within the export/csv folder.
    * **`to_html`:** DEFAULT: `False`. Saves the dataframe in a .html format within the export/html folder.
  * Returns:
    * If no arguments are specified, the function returns a Pandas dataframe containing the standard deviation
    and variance of all numeric columns
    * Otherwise, it returns a Pandas dataframe containing the standard deviation and variance of the specified list of columns.
* **`calculate_iqr`:** This function calculates the interquartile range of all *numeric* columns within a Pandas dataframe. Alternately, users can specify a list of columns for which they would want to calculate the interquartile range. If the list contains non-numeric columns, then the function displays exceptions to the column names.
  * Parameters:
    * **`dataframe`:** Pandas dataframe.
    * **`args`:** List of column names for which users would like to calculate the interquartile range. Without arguments, Python will calculate the interquartile range of all numeric columns of the dataframe
      by default.
    * **`display`:** DEFAULT: `True`. If display is True, then the function displays the resulting dataframe, else it just
      returns the resulting dataframe.
    * **`to_csv`:** DEFAULT: `False`. Saves the dataframe in a .csv format within the export/csv folder.
    * **`to_html`:** DEFAULT: `False`. Saves the dataframe in a .html format within the export/html folder.
  * Returns:
    * If no arguments are specified, the function returns a Pandas dataframe containing the interquartile range of all numeric columns
    * Otherwise, it returns a Pandas dataframe containing the interquartile range of the specified list of columns.
* **`calculate_zscore`:** This function calculates the z-score of all *numeric* columns within a Pandas dataframe. Alternately, users can specify a list of columns for which they would want to calculate the z-score. If the list contains non-numeric columns, then the function displays exceptions to the column names.
  * Parameters:
    * **`dataframe`:** Pandas dataframe.
    * **`args`:** List of column names for which users would like to calculate the z-score. Without arguments, Python will calculate the z-score of all numeric columns of the dataframe by default.
    * **`ddof`:** DEFAULT: `0`. Degrees of freedom.
    * **`display`:** DEFAULT: `True`. If display is True, then the function displays the resulting dataframe, else it just returns the resulting dataframe.
    * **`to_csv`:** DEFAULT: `False`. Saves the dataframe in a .csv format within the export/csv folder.
    * **`to_html`:** DEFAULT: `False`. Saves the dataframe in a .html format within the export/html folder.
  * Returns:
    * If no arguments are specified, the function returns a Pandas dataframe containing the z-score of all numeric columns
    * Otherwise, it returns a Pandas dataframe containing the z-score of the specified list of columns.

### Plots

* **`histogram`:** This function generates an interactive histogram in HTML based on a dataframe and saves the plot in the same
    folder as the codes.
* Parameters:
  * **`dataframe`:** Pandas dataframe.
  * **`xaxis`:** the column of the Pandas dataframe for which you want the histogram.
  * **`bins`**: Number of bins in the histogram.
  * **`title`**: Title of the histogram.
  * **`xlabel`**: Label of the x-axis of the histogram.
  * **`to_html`**: DEFAULT: `True`. Saves the interactive plot in a .html format within the export/html folder.
* Returns:
  * Figure.

* **`lineplot`:** This function generates an interactive line plot in HTML based on a dataframe.
  * Parameters:
    * **`dataframe`:** Pandas dataframe.
    * **`xaxis`:** The column of the Pandas dataframe for which you want the line plot's x-axis.
    * **`yaxis`:** The column of the Pandas dataframe for which you want the line plot's y-axis.
    * **`title`:** Title of the line plot.
    * **`xlabel`:** Label of the x-axis of the line plot.
    * **`ylabel`:** Label of the y-axis of the line plot.
    * **`to_html`:** DEFAULT: `True`. Saves the interactive plot in a .html format within the export/html folder.
    * **`hover_text`:** Text to display when the user hovers over specific datapoints on the plot.
  * Returns:
    * Figure.

* **`barplot`:** This function generates an interactive barplot plot in HTML based on a dataframe.
  * Parameters:
    * **`dataframe`:** Pandas dataframe.
    * **`xaxis`:** The column of the Pandas dataframe for which you want the bar plot's x-axis.
    * **`yaxis`:** The column of the Pandas dataframe for which you want the bar plot's y-axis.
    * **`title`:** Title of the bar plot.
    * **`xlabel`:** Label of the x-axis of the bar plot.
    * **`ylabel`:** Label of the y-axis of the bar plot.
    * **`to_html`:** DEFAULT: `True`. Saves the interactive plot in a .html format within the export/html folder.
    * **`hover_text`:** Text to display when the user hovers over specific datapoints on the plot.
    * **`barmode`:** DEFAULT: `stack`. The type of barplot the user requires. The user can choose between two options - '`stack`' and '`group`'.
  * Returns:
    * Figure.

* **`boxplot`:** This function generates an interactive box plot in HTML based on a dataframe.
  * Parameters:
    **`dataframe`:** Pandas dataframe.
    **`title`:** Title of the box plot.
    **`to_html`:** DEFAULT: `True`. Saves the interactive plot in a .html format within the export/html folder.
  * Returns:
    * Figure.

### Export

* **`run_html`:** This function publishes the interactive report on the browser. This function also saves an interactive HTML file in the export directory, which is created by the function in the same directory as the user-createdPython module running the function.

## License

Copyright 2021 Arpan Ganguli

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated
documentation files (the "Software"), to deal in the Software without restriction, including without limitation the
rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit
persons to whom the Software is furnished to do so, subject to the following conditions:
The above copyright notice and this permission notice shall be included in all copies or substantial portions of the
Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO TH
WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR
COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR
OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
