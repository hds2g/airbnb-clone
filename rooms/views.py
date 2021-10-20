from django.views.generic import ListView
from . import models

"""
def all_rooms(request):
    page = request.GET.get("page", 1)

    room_list = models.Room.objects.all()
    paginator = Paginator(room_list, 10, orphans=5)
    try:

        rooms = paginator.page(int(page))
        return render(request, "room_views, {"page": rooms})
    except EmptyPage:
        return redirect("/")

    # print(dir(rooms))
"""


class HomeView(ListView):
    """HomeView Definition"""

    model = models.Room

    paginate_by = 10
    paginate_orphans = 5
    ordering = "created"
