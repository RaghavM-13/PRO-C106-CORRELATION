import numpy as np
import csv

def getDataSource(data_path):
    marks_in_percentage = []
    days_present = []
    with open(data_path) as csv_file:
        reader = csv.DictReader(csv_file)
        for row in reader:
            marks_in_percentage.append(float(row["Marks In Percentage"]))
            days_present.append(float(row["Days Present"]))

    return {"x" : marks_in_percentage, "y" : days_present}

def findCorrelation(datasource):
    correlation = np.corrcoef(datasource["x"], datasource["y"])
    print("Correlation between Marks and days present: \n--->",correlation[0,1])

def setup():
    data_path = "Student Marks vs Days Present.csv"

    datasource = getDataSource(data_path)
    findCorrelation(datasource)

setup()
