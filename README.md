# Exploratory Data Analysis (EDA) tool

## Aim

The aim of this tool is to automate the exploratory data analysis (EDA) process as part of the reproducible analytic
pipeline (RAP) for publishing energy statistics.

This tool is available in the form of a Python package.

## Structure
```
EdaPackage:.
│   README.md
│   run_eda.py
│   run_html_report.py
│
├───codes
│   │   __init__.py
│   │
│   ├───custom
│   │       breakdown.py
│   │       regression.py
│   │       sums.py
│   │       time_series.py
│   │
│   ├───plots
│   │       __init__.py
│   │
│   └───standard
│           central_tendency.py
│           metadata.py
│           spread.py
│
├───data
│       import_file.csv
│       RandGen_105.csv
│       RandGen_151.csv
│       RandGen_324.csv
│       RandGen_342.csv
│       RandGen_343.csv
│       RandGen_442.csv
│       RandGen_655.csv
│       RandGen_69.csv
│       RandGen_755.csv
│       RandGen_794.csv
│       random_data_generator.py
│
├───docs
│       file_structure.txt
│       requirements.txt
│
├───export
│   │   eda_file.html
│   │   __init__.py
│   │
│   ├───csv
│   │       ct_calculate_mean_columns.csv
│   │       ct_calculate_mean_dataframe.csv
│   │       ct_calculate_median_columns.csv
│   │       ct_calculate_median_dataframe.csv
│   │       ct_calculate_mode_columns.csv
│   │       ct_calculate_mode_dataframe.csv
│   │       mt_describe_dataframe.csv
│   │       mt_display_column_names.csv
│   │       mt_display_data_types.csv
│   │       mt_display_shape.csv
│   │       sp_calculate_iqr_columns.csv
│   │       sp_calculate_iqr_dataframe.csv
│   │       sp_calculate_max_and_min_columns.csv
│   │       sp_calculate_max_and_min_dataframe.csv
│   │       sp_calculate_std_and_var_columns.csv
│   │       sp_calculate_std_and_var_dataframe.csv
│   │       sp_calculate_zscore_columns.csv
│   │       sp_calculate_zscore_dataframe.csv
│   │
│   ├───html
│   │       ct_calculate_mean_columns.html
│   │       ct_calculate_mean_dataframe.html
│   │       ct_calculate_median_columns.html
│   │       ct_calculate_median_dataframe.html
│   │       ct_calculate_mode_columns.html
│   │       ct_calculate_mode_dataframe.html
│   │       mt_describe_dataframe.html
│   │       mt_display_column_names.html
│   │       mt_display_data_types.html
│   │       mt_display_shape.html
│   │       plt_Histogram of Sample Numeric Data - 1.html
│   │       plt_Histogram of Sample Numeric Data - 2.html
│   │       plt_Sample Bar Plot - 2.html
│   │       plt_Sample Bar Plot - 5.html
│   │       plt_Sample Line Plot - 1.html
│   │       plt_Sample Line Plot - 4.html
│   │       plt_Sample_Boxplot_12.html
│   │       plt_Sample_Boxplot_345.html
│   │       sp_calculate_iqr_columns.html
│   │       sp_calculate_iqr_dataframe.html
│   │       sp_calculate_max_and_min_columns.html
│   │       sp_calculate_max_and_min_dataframe.html
│   │       sp_calculate_std_and_var_columns.html
│   │       sp_calculate_std_and_var_dataframe.html
│   │       sp_calculate_zscore_columns.html
│   │       sp_calculate_zscore_dataframe.html
│   │
│   ├───static
│   │       style.css
│   │
│   └───templates
│           template.html
│
└───test
    │   conftest.py
    │   pytest.ini
    │
    └───standard
            test_central_tendency.py
            test_metadata.py
            test_spread.py
```

## How to install this package

As of 25 May 2021, the package can be downloaded from
the [eda_dev branch of the stats-pipeline repository](http://gitlab/esip/prototype-rap).
