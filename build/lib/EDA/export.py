import os
from collections import defaultdict

from flask import Flask, render_template, url_for
from jinja2 import Environment, FileSystemLoader

from pathlib import Path

ABOUT_TEXT = "This report generates the results of Exploratory Data Analysis (EDA) as part of the Reproducible " \
             "Analytic Pipeline (RAP)."
SUMMARY_METADATA = "This section summarises metadata of the database."
SUMMARY_CENTRAL_TENDENCY = "This section summarises the central tendency of the imported data. It contains the " \
                           "mean, median and mode of the data."
SUMMARY_SPREAD = "This section summarises the central tendency of the imported data. It contains the max and min, " \
                 "standard deviation and variance and Z-score the data."
SUMMARY_PLOTS = "This section generates all the relevant plots"

app = Flask(__name__)

_HOME = os.getcwd()

file_list = os.listdir(os.path.join(_HOME, "export", "html"))
FILE_DICT = defaultdict(list)

for file in file_list:
    if file.startswith("mt_"):
        FILE_DICT["metadata"].append(file)
    elif file.startswith("ct_"):
        FILE_DICT["central_tendency"].append(file)
    elif file.startswith("sp_"):
        FILE_DICT["spread"].append(file)
    elif file.startswith("plt_"):
        FILE_DICT["plots"].append(file)
    else:
        FILE_DICT["descriptive_statistics"].append(file)

PLOT_NAME_DICT = {
    FILE_DICT['plots'][j]: 'Plot ' + str(j + 1) for j in range(0, len(FILE_DICT['plots']))
}

package_path = Path(__file__).parent

loader = FileSystemLoader([os.path.join(package_path, 'templates'), 'export\\html', \
                           os.path.join(package_path, 'static')])
env = Environment(loader=loader)
template = env.get_template('template.html')


@app.route("/")
def run_template():
    output = render_template(template,
                             ABOUT_TEXT=ABOUT_TEXT,
                             SUMMARY_METADATA=SUMMARY_METADATA,
                             SUMMARY_CENTRAL_TENDENCY=SUMMARY_CENTRAL_TENDENCY,
                             SUMMARY_SPREAD=SUMMARY_SPREAD,
                             SUMMARY_PLOTS=SUMMARY_PLOTS,
                             FILE_DICT=FILE_DICT,
                             PLOT_NAME_DICT=PLOT_NAME_DICT
                             )
    _PATH = os.path.join(_HOME, 'export', 'eda_file.html')
    with open(_PATH, 'w') as fh:
        fh.write(output)
    return output


if __name__ == "__main__":
    app.run(debug=True)
else:
    app.run(debug=True)
