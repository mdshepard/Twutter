from django.shortcuts import render

from .models import Twuut


def feed(request):
    user_ids = [item.id for item in request.user.twutterprofile.follows.all()]
    for id in request.user.twutterprofile.follows.all():
        user_ids.append(id)

    user_ids.append(request.user.id)
    twuuts = list(Twuut.objects.filter(user_id__in=user_ids)[:25])

    return render(request, 'feed.html', {'twuuts': twuuts})
