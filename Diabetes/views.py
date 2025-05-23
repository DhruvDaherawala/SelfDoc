from django.shortcuts import render, redirect
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from Diabetes.models import Diabetes_data, FeedBack
from django.contrib.auth import get_user_model
from django.http import HttpResponse
import csv, datetime
import os
from django.conf import settings


User = get_user_model()

def export_diabetes(request):
    diabetes = Diabetes_data.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;' 'filename=Diabetes_data.csv'
    writer = csv.writer(response)
    # Write a first row with header information
    writer.writerow(['name', 'gender', 'pregnancy', 'glucose', 'blood_pressure', 'insulin', 'bmi', 'age', 'time'])
    # Write data rows
    diabetes_fields = diabetes.values_list('name', 'gender', 'pregnancy', 'glucose', 'blood_Pressure', 'insulin', 'bmi', 'age', 'time')

    for diabetes in diabetes_fields:
        writer.writerow(diabetes)

    return response

def export_feedback(request):
    feedback = FeedBack.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment;' 'filename=Feedback_Data.csv'
    writer = csv.writer(response)
    # Write a first row with header information
    writer.writerow(['Name', 'Email', 'Mobile_no.', 'Feedback'])
    # Write data rows
    feedback_fields = feedback.values_list('name', 'email', 'mobile', 'feedback')

    for feedback in feedback_fields:
        writer.writerow(feedback)

    return response

def index(request):
    if request.method == "POST":
        # Get form data
        name = request.POST.get('name')
        email = request.POST.get('email')
        mobile = request.POST.get('mobile')
        feedback = request.POST.get('feedback')

        # Insert data into the Django admin
        FeedBack.objects.create(
            name=name,
            email=email,
            mobile=mobile,
            feedback=feedback
        )
    return render(request, 'index.html')

def predict(request):
    return render(request, 'predict.html')

def result(request):

    if request.method == "POST":
        # Get form data
        name = request.POST.get('name')
        gender = request.POST.get('gender')
        pregnancy = request.POST.get('a1')
        glucose = request.POST.get('a2')
        bp = request.POST.get('a3')
        insulin = request.POST.get('a4')
        bmi = request.POST.get('a5')
        age = request.POST.get('a6')

        # Insert data into the Django admin
        Diabetes_data.objects.create(
            name=name,
            gender=gender,
            pregnancy=pregnancy,
            glucose=glucose,
            blood_Pressure=bp,
            insulin=insulin,
            bmi=bmi,
            age=age
        )

    # Load the dataset for prediction
    # data = pd.read_csv("D:\Dhruv College Coding + Lab Manual + Projects\Dhruv DE Projects\Diabetes Prediction System\Dataset\main_data.csv")
    file_path = os.path.join(settings.DATA_DIR, 'main_data.csv')

    # Read the dataset
    data = pd.read_csv(file_path)

    # Assuming 'Outcome' is the target variable
    x = data.drop('Outcome', axis=1)
    y = data['Outcome']
    x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2)

    # Train a logistic regression model
    model = LogisticRegression()
    model.fit(x_train, y_train)

    # Get values for prediction
    val1 = float(request.POST.get('a1'))
    val2 = float(request.POST.get('a2'))
    val3 = float(request.POST.get('a3'))
    val4 = float(request.POST.get('a4'))
    val5 = float(request.POST.get('a5'))
    val6 = float(request.POST.get('a6'))

    # Make a prediction
    prediction = model.predict([[val1, val2, val3, val4, val5, val6]])

    # Determine the result and suggestions
    if prediction == 1:
        result = "You have Diabetes."
        suggestions = "Suggestions"
    else:
        result = "You do not have Diabetes."
        suggestions = "suggestions"

    return render(request, 'predict.html', {"result1": result, "suggestions": suggestions})

def suggestions(request):
    return render(request, 'suggestions.html')

def developerTeam(request):
    return render(request, 'developerTeam.html')
