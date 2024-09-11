from django.shortcuts import render, get_object_or_404
from .models import Project, TeamMember


def index(request):
    projects = Project.objects.all()  # Fetch all projects
    return render(request, 'index.html', {'projects': projects})


def team_nepal(request):
    team_members = TeamMember.objects.all()
    return render(request, 'team_nepal.html', {'team_members': team_members})

# Similarly, you can create views for other teams like team_netherlands, members_world, etc.
