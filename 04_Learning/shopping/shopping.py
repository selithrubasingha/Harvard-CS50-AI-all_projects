import csv
import sys
import pandas as pd
import numpy as np

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import classification_report

TEST_SIZE = 0.4


def main():

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python shopping.py data")

    # Load data from spreadsheet and split into train and test sets
    evidence, labels = load_data(sys.argv[1])
    X_train, X_test, y_train, y_test = train_test_split(
        evidence, labels, test_size=TEST_SIZE
    )

    # Train model and make predictions
    model = train_model(X_train, y_train)
    predictions = model.predict(X_test)
    sensitivity, specificity = evaluate(y_test, predictions)

    # Print results
    print(f"Correct: {(y_test == predictions).sum()}")
    print(f"Incorrect: {(y_test != predictions).sum()}")
    print(f"True Positive Rate: {100 * sensitivity:.2f}%")
    print(f"True Negative Rate: {100 * specificity:.2f}%")


def load_data(filename):
    """
    Load shopping data from a CSV file `filename` and convert into a list of
    evidence lists and a list of labels. Return a tuple (evidence, labels).

    evidence should be a list of lists, where each list contains the
    following values, in order:
        - Administrative, an integer
        - Administrative_Duration, a floating point number
        - Informational, an integer
        - Informational_Duration, a floating point number
        - ProductRelated, an integer
        - ProductRelated_Duration, a floating point number
        - BounceRates, a floating point number
        - ExitRates, a floating point number
        - PageValues, a floating point number
        - SpecialDay, a floating point number
        - Month, an index from 0 (January) to 11 (December)
        - OperatingSystems, an integer
        - Browser, an integer
        - Region, an integer
        - TrafficType, an integer
        - VisitorType, an integer 0 (not returning) or 1 (returning)
        - Weekend, an integer 0 (if false) or 1 (if true)

    labels should be the corresponding list of labels, where each label
    is 1 if Revenue is true, and 0 otherwise.
    """
    df = pd.read_csv(filename)

    print(df.head())

    month_mapping = {
        "Jan": 0,
        "Feb": 1,
        "Mar": 2,
        "Apr": 3,
        "May": 4,
        "June": 5,
        "Jul": 6,
        "Aug": 7,
        "Sep": 8,
        "Oct": 9,
        "Nov": 10,
        "Dec": 11
    }

    weekend_revenue_mapping = {
        False: 0,
        True: 1
    }

    visitor_mapping = {
        "New_Visitor": 0,
        "Returning_Visitor": 1,
        "Other": 0

    }

    df["Month"] = df["Month"].map(month_mapping)
    df["Weekend"] = df["Weekend"].map(weekend_revenue_mapping)
    df['VisitorType'] = df['VisitorType'].map(visitor_mapping)
    df["Revenue"] = df["Revenue"].map(weekend_revenue_mapping)

    int_cols = [
        "Administrative", "Informational", "ProductRelated", "Month",
        "OperatingSystems", "Browser", "Region", "TrafficType",
        "VisitorType", "Weekend"
    ]
    float_cols = [
        "Administrative_Duration", "Informational_Duration",
        "ProductRelated_Duration", "BounceRates", "ExitRates",
        "PageValues", "SpecialDay"
    ]
    # Ensure labels are also integers
    df["Revenue"] = df["Revenue"].astype(int)

    for col in int_cols:
        df[col] = df[col].astype(int)
    for col in float_cols:
        df[col] = df[col].astype(float)

    evidence = df.drop("Revenue", axis=1)
    labels = df["Revenue"]

    evidence_lists = evidence.to_numpy().tolist()
    labels_list = labels.to_numpy().tolist()

    return (evidence_lists, labels_list)


def train_model(evidence, labels):
    """
    Given a list of evidence lists and a list of labels, return a
    fitted k-nearest neighbor model (k=1) trained on the data.
    """
    classifier = KNeighborsClassifier(n_neighbors=1)
    classifier.fit(evidence, labels)

    return classifier


def evaluate(labels, predictions):
    """
    Given a list of actual labels and a list of predicted labels,
    return a tuple (sensitivity, specificity).

    Assume each label is either a 1 (positive) or 0 (negative).

    `sensitivity` should be a floating-point value from 0 to 1
    representing the "true positive rate": the proportion of
    actual positive labels that were accurately identified.

    `specificity` should be a floating-point value from 0 to 1
    representing the "true negative rate": the proportion of
    actual negative labels that were accurately identified.
    """
    report = classification_report(labels, predictions, output_dict=True)

    sensitivity = report['1']['recall']
    specificity = report['0']['recall']

    return (sensitivity, specificity)


if __name__ == "__main__":
    main()
