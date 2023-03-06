from collections import namedtuple
import altair as alt
import math
import pandas as pd
import streamlit as st

import streamlit as st
import numpy as np
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix
import matplotlib.pyplot as plt

"""
# Welcome to Streamlit!

Edit `/streamlit_app.py` to customize this app to your heart's desire :heart:

If you have any questions, checkout our [documentation](https://docs.streamlit.io) and [community
forums](https://discuss.streamlit.io).

In the meantime, below is an example of what you can do with just a few lines of code:
"""


with st.echo(code_location='below'):
    total_points = st.slider("Number of points in spiral", 1, 5000, 2000)
    num_turns = st.slider("Number of turns in spiral", 1, 100, 9)

    Point = namedtuple('Point', 'x y')
    data = []

    points_per_turn = total_points / num_turns

    for curr_point_num in range(total_points):
        curr_turn, i = divmod(curr_point_num, points_per_turn)
        angle = (curr_turn + 1) * 2 * math.pi * i / points_per_turn
        radius = curr_point_num / total_points
        x = radius * math.cos(angle)
        y = radius * math.sin(angle)
        data.append(Point(x, y))

    st.altair_chart(alt.Chart(pd.DataFrame(data), height=500, width=500)
        .mark_circle(color='#0068c9', opacity=0.5)
        .encode(x='x:Q', y='y:Q'))
    



st.title('Handwritten Digit Classification')

# Load the digits dataset
digits = load_digits()

# Split the data into training and test sets
X_train, X_test, y_train, y_test = train_test_split(digits.data, digits.target, test_size=0.2, random_state=42)

# Train a logistic regression model
model = LogisticRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Compute the accuracy of the model
accuracy = accuracy_score(y_test, y_pred)

# Compute the confusion matrix of the model
cm = confusion_matrix(y_test, y_pred)

# Display the accuracy and confusion matrix
st.write('Accuracy:', accuracy)
st.write('Confusion matrix:', cm)

# Allow the user to input a digit image
image = st.file_uploader('Upload an image of a digit:', type='png')

if image is not None:
    # Load the image and preprocess it
    img = plt.imread(image)
    img = np.mean(img, axis=2)
    img = np.reshape(img, (1, -1))

    # Make sure the image has the same shape as the training data
    if img.shape[1] > X_train.shape[1]:
        img = np.hstack((img, np.zeros((1, X_train.shape[1] - img.shape[1]))))

    # Make a prediction on the input image
    pred = model.predict(img)

    # Display the prediction
    st.write('Prediction:', pred[0])

