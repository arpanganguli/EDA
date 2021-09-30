# Exploratory Data Analysis (EDA)

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

### Metadata

* **`describe_dataframe`:** This function publishes descriptive statistics of different columns of a dataframe.
  **NOTE:** It publishes the descriptive statistics of *numeric* columns only.
* **`display_column_names`:** This function displays the names of columns of a dataframe as a list of column names.
* **`display_data_types`:** This function displays the data types of all (specified) columns in a dataframe.
* **`display_shape`:** This function displays the rows and columns of the dataframe.

### Central Tendency

* **`calculate_mean`:** This function calculates the mean of all *numeric* columns within a Pandas dataframe.
  Alternately, users can specify a list of columns for which they would want to calculate
  the mean. If the list contains non-numeric columns, then the function displays exceptions
  to the column names.

  * Parameters:
    * **`dataframe`:** Pandas dataframe.
    * **`args`:** list of column names for which users would like to calculate the mean. Without arguments, Python will
      calculate mean of all numeric columns of the dataframe by default.
    * **`display`:** DEFAULT: True. If display is True, then the function displays the resulting dataframe, else it just
      returns the resulting dataframe.
    * **`to_csv`:** DEFAULT: False. Saves the dataframe in a .csv format within the export/csv folder.
    * **`to_html`:** DEFAULT: False. Saves the dataframe in a .html format within the export/html folder.
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
    * **`args`:** list of column names for which users would like to calculate the median. Without arguments, Python will
      calculate median of all numeric columns of the dataframe by default.
    * **`display`:** DEFAULT: True. If display is True, then the function displays the resulting dataframe, else it just
      returns the resulting dataframe.
    * **`to_csv`:** DEFAULT: False. Saves the dataframe in a .csv format within the export/csv folder.
    * **`to_html`:** DEFAULT: False. Saves the dataframe in a .html format within the export/html folder.
  * Returns:
    * If no arguments are specified, the function returns a Pandas dataframe containing the median of all numeric
      columns
    * Otherwise, it returns a Pandas dataframe containing the median of the specified list of columns.
* **`calculate_mode`:** This function calculates the mode of all columns within a Pandas dataframe. Alternately, users can
  specify a list of columns for which they would want to calculate the median.

  * Parameters:
    * **`dataframe`:** Pandas dataframe.
    * **`args`:** list of column names for which users would like to calculate the mode. Without arguments, Python will
      calculate the mode of all columns of the dataframe by default.
    * **`display`:** DEFAULT: True. If display is True, then the function displays the resulting dataframe, else it just
      returns the resulting dataframe.
    * **`to_csv`:** DEFAULT: False. Saves the dataframe in a .csv format within the export/csv folder.
    * **`to_html`:** DEFAULT: False. Saves the dataframe in a .html format within the export/html folder.
  * Returns:
    * If no arguments are specified, the function returns a Pandas dataframe containing the mode of all columns
    * Otherwise, it returns a Pandas dataframe containing the mode of the specified list of columns.

### Spread

### Plots

### Export

## License

Copyright 2021 Department for Business, Energy and Industrial Strategy

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
