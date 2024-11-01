from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse

from places.models import Places, Images


def show_map(request):
    
    places = Places.objects.all()
    
    features = []
    
    for place in places:
        feature = {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [place.lon, place.lat]
            },
            "properties": {
                "title": place.title,
                "placeId": place.place_id,
                "detailsUrl": f'https://raw.githubusercontent.com/devmanorg/where-to-go-frontend/refs/heads/master/places/{place.place_id}.json'
            }
        }
        features.append(feature)
        
    context = {
        'places_geo' : {
            "type": "FeatureCollection",
            "features": features
        }
    }
    
    return render(request, 'index.html', context=context)


def show_place_detail(request, place_id):
    place = get_object_or_404(Places, id=place_id)
    images = Images.objects.filter(title=place.title)
    
    images_url = [image.image.url for image in images]
    
    context = {
        'title': place.title,
        'images': [images_url],
        'description_short': place.description_short,
        'description_long': place.description_long,
        'coordinates': {
            'lat': place.lat,
            'lon': place.lon
        }
    }
    
    return JsonResponse(context, json_dumps_params={'ensure_ascii': False, 'indent': 2})