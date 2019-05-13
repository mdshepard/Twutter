from django.shortcuts import render

from .models import Twuut


def feed(request):
    userids = [item.id for item in request.user.twutterprofile.follows.all()]
    userids.append(request.user.id) 
    twuuts = Twuut.objects.filter(user_id__in=userids)
    return render(
        request, 'feed.html', {'twuuts':twuuts}
        )
