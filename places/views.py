from django.http import HttpResponse, HttpResponseBadRequest
from django.shortcuts import redirect
from django.template import loader
from places.models import Place
from places.forms import BookingForm


def place_list(request):
    places = Place.objects.all()
    template = loader.get_template('all_places.html')
    context = {
        'places': places,
    }
    return HttpResponse(template.render(context, request))


def booking(request, place_id):
    if request.user.is_authenticated:
        template = loader.get_template('booking.html')
        message = ''
        if request.method == 'GET':
            post_form = BookingForm(initial={
                'place': place_id,
                'user': request.user})
        elif request.method == "POST":
            post_form = BookingForm(request.POST)
            if post_form.is_valid():
                post_form.save()
                message = 'Booking success.'
        else:
            return HttpResponseBadRequest()
        context = {
            'post_form': post_form,
            'message': message,
        }
        return HttpResponse(template.render(context, request))
    return redirect('login')
