from django.shortcuts import render

def home(request):
    import requests
    import json
    # pk_5fc4d58980834899affc6a6e7e28b287

    api_request = requests.get("https://cloud.iexapis.com/stable/aapl/quote?token=pk_5fc4d58980834899affc6a6e7e28b287")

    try:
        api = json.loads(api_request.content)
    except Exception as e:
        api = "Error..."

    return render(request, 'home.html', {'api':api})

def about(request):
    return render(request, 'about.html', {})