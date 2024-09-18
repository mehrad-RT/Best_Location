from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import MinMaxScaler
import os 
from .models import Information, User


def index(request):
    return render(request, "best_location/index.html")

def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "best_location/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "best_location/login.html")

def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))

def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "best_location/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "best_location/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "best_location/register.html")

def predict_profit(a, b, c, d):
    # Reading data from the Excel file
    file_path = os.path.join(os.path.dirname(__file__), 'DataSet', 'data.xlsx')
    data = pd.read_excel(file_path)

    # Defining inputs and outputs
    train_inputs = data.iloc[:, :4].values
    train_targets = data.iloc[:, 4].values

    # Splitting the data into training and testing sets
    x_train, x_test, y_train, y_test = train_test_split(train_inputs, train_targets, test_size=0.2, random_state=42)

    # Normalizing the data
    scaler_inputs = MinMaxScaler()
    scaler_targets = MinMaxScaler()
    x_train = scaler_inputs.fit_transform(x_train)
    x_test = scaler_inputs.transform(x_test)
    y_train = scaler_targets.fit_transform(y_train.reshape(-1, 1)).ravel()
    y_test = scaler_targets.transform(y_test.reshape(-1, 1)).ravel()

    # Creating the multiple linear regression model
    model = LinearRegression()

    # Training the model
    model.fit(x_train, y_train)

    # User inputs
    inputs = np.array([[a, b, c, d]])

    # Normalizing the user inputs
    inputs_normalized = scaler_inputs.transform(inputs)

    # Predicting the output
    output_normalized = model.predict(inputs_normalized)

    # Reverting the normalization for the output
    output = scaler_targets.inverse_transform(output_normalized.reshape(-1, 1))

    return output[0][0]


def try_AI(request):
    if request.method == "POST":
        user = request.user
        district_number = float(request.POST.get('district_number', 0))
        size = float(request.POST.get('size', 0))
        product_grade = float(request.POST.get('product_grade', 0))
        parking_place = request.POST.get('parking_place')
        if parking_place is not None:
            parking_place = float(parking_place)
        else:
            parking_place = 2.0

        # Saving input information
        information = Information(user=user, district_number=district_number, size=size, product_grade=product_grade, parking_place=parking_place)
        information.save()

        # Predicting profit
        predicted_profit = predict_profit(district_number, size, product_grade, parking_place)

        # Updating information with predicted profit
        information.profit = predicted_profit
        information.save()

        # Redirecting to the result page
        return HttpResponseRedirect(reverse("result", args=[information.id]))

    return render(request, "best_location/try_AI.html")


def result_view(request, input_id):
    information = Information.objects.get(id=input_id)
    return render(request, "best_location/result.html", {'predicted_profit': information.profit})


