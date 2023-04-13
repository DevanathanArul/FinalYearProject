from django.shortcuts import render
from django.shortcuts import render, redirect
import numpy as np
import joblib

model = joblib.load('C:/Users/devan/Music/PROJECT-DEMENTIA/CODE/deploy/app/model.pkl')

# Create your views here.
def home(request):
    return render(request, "index.html")


def predict(request):
    if request.method == "POST":
        int_features = [x for x in request.POST.values()]
        int_features = int_features[1:]
        print(int_features)
        final_features = [np.array(int_features, dtype=object)]
        print(final_features)
        prediction = model.predict(final_features)
        print(prediction)
        output = prediction[0]
        print(f'output{output}')
        if output == 0:
            return render(request, 'index.html', {"prediction_text":"DEMENTIA IS CONVERTED"})
        elif output == 1:
            return render(request, 'index.html', {"prediction_text":"DEMENTIA IS DEMENTED"})
        elif output == 2:
            return render(request, 'index.html', {"prediction_text":"DEMENTIA IS NON DEMENTED"})
        print(output)
