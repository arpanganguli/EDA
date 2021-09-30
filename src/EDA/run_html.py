from EDA.export import app


def run_html():
    """
    This function returns the HTML report.
    :return: HTML report.
    """
    if __name__ != "__main__":
        app.run(debug=True)