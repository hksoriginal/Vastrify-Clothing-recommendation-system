from django.http import HttpResponseBadRequest, HttpResponseNotAllowed
from django.shortcuts import render
import json
from vastrify.recommend_function.recommend_function_implementation import RecommendFunction


# Renders the 'index.html' template
def index(request):
    return render(request, 'index.html')


# Handles the recommendation of clothing items
def recommend_clothing_items(request):
    if request.method == 'POST':  # Checks if the request method is 'POST'
        try:
            input_text = request.POST['input_text']
            top_results = request.POST['top_results']
            # Calls the 'recommend_clothes' function from 'RecommendFunction' class to get recommendations
            recommendations = RecommendFunction().recommend_clothes(input_text, top_results)
            # Renders the 'index.html' template with the recommendations passed as a context variable
            return render(request, 'index.html', {'recommendations': recommendations})
        except json.JSONDecodeError:
            # Handles JSON decoding error and returns an HTTP response with 'Invalid JSON data' message
            return HttpResponseBadRequest('Invalid JSON data')
    else:
        # Handles non-POST requests and returns an HTTP response with '405 Method Not Allowed' status
        return HttpResponseNotAllowed(['POST'])
