from django.shortcuts import render

from .models import Twuut


def feed(request):
    userids = [item.user.id for item in request.user.twutterprofile.follows.all()]
    twuuts = Twuut.objects.filter(user_id__in=userids).order_by('-created_at')

    # Sorry for the commented out code **below**, but I've got to keep this and explain it to myself in here for further reading later.
    # the first two double dunders are signifying finding nested foreign relationships.
    # the user to twutter profile relationship is one to tone, then the second double dunder pulls the ID of the user
    # that's connected to the twutter profile. The third double dunder before "in" is a magic method that's directing the filter.
    # twuuts = Twuut.objects.filter(user__twutterprofile__id__in=userids).order_by('-created_at')
    
    return render(request, 'feed.html', {'twuuts':twuuts})
