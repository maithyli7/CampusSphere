from django.shortcuts import render
from .models import Student, Notice, Event, StudyMaterial, LostFound, Calendar
from django.contrib.auth.decorators import login_required

@login_required(login_url='login')
def notices(request):
    notices = Notice.objects.all().order_by("-date")
    return render(request, "notices.html", {"notices": notices})

@login_required(login_url='login')
def events(request):
    events = Event.objects.all().order_by("date")

    return render(request, "events.html", {
        "events": events
    })
@login_required(login_url='login')
def study_materials(request):
    materials = StudyMaterial.objects.all().order_by('-uploaded_on')

    return render(request, 'study_materials.html', {
        'materials': materials
    })

@login_required(login_url='login')
def lost_found(request):
    items = LostFound.objects.all().order_by('-date')
    return render(request, 'lost_found.html', {'items': items})

from .models import Calendar
@login_required(login_url='login')
def calendar(request):
    calendars = Calendar.objects.all().order_by("date")
    return render(request, "calendar.html", {
        "calendars": calendars
    })


def admin_dashboard(request):
    context = {
        "student_count": Student.objects.count(),
        "notice_count": Notice.objects.count(),
        "event_count": Event.objects.count(),
        "lost_count": LostFound.objects.count(),
        "study_count": StudyMaterial.objects.count(),
        "calendar_count": Calendar.objects.count(),
    }

    return render(request, "admin_dashboard.html", context)

def home(request):
    return render(request, 'home.html')

def login_view(request):
    return render(request, 'login.html')


from django.shortcuts import get_object_or_404

from django.shortcuts import render, get_object_or_404

def student_dashboard(request):
    student = get_object_or_404(Student, user=request.user)

    notices = Notice.objects.all().order_by("-date")[:5]
    events = Event.objects.all().order_by("date")[:5]
    materials = StudyMaterial.objects.all().order_by("-uploaded_on")[:5]
    lost_items = LostFound.objects.all().order_by("-date")[:5]

    context = {
        "student": student,

        "notices": notices,
        "events": events,
        "materials": materials,
        "lost_items": lost_items,

        "notice_count": Notice.objects.count(),
        "event_count": Event.objects.count(),
        "material_count": StudyMaterial.objects.count(),
        "lost_count": LostFound.objects.count(),
    }

    return render(request, "student_dashboard.html", context)