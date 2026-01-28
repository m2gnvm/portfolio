import json
import os
from datetime import datetime
from django.shortcuts import render
from django.http import JsonResponse

def load_portfolio_data():
    """Load portfolio data from JSON file"""
    try:
        # Try multiple possible paths
        base_dir = os.path.dirname(os.path.dirname(__file__))
        json_path = os.path.join(base_dir, 'static', 'portfolio_data.json')
        
        if not os.path.exists(json_path):
            # Fallback to project root
            json_path = os.path.join(base_dir, 'portfolio_data.json')
        
        with open(json_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Convert string dates to date objects for experience entries
        for experience in data.get('experience', []):
            if experience.get('start_date'):
                experience['start_date'] = datetime.strptime(experience['start_date'], '%Y-%m-%d').date()
            if experience.get('end_date'):
                experience['end_date'] = datetime.strptime(experience['end_date'], '%Y-%m-%d').date()
        
        return data
    except Exception as e:
        # Return minimal data structure if file can't be loaded
        return {
            'personal_info': {'name': 'Error', 'title': 'Portfolio', 'summary': 'Error loading data'},
            'skills': {'backend': [], 'data': [], 'devops': []},
            'projects': [],
            'experience': []
        }

def home(request):
    """Homepage view"""
    data = load_portfolio_data()
    
    # Get featured projects (first 3)
    featured_projects = data['projects'][:3]
    
    # Get skills by category
    backend_skills = data['skills']['backend']
    data_skills = data['skills']['data']
    devops_skills = data['skills']['devops']
    
    # Get recent experience
    recent_experience = data['experience'][0] if data['experience'] else None
    
    context = {
        'personal_info': data['personal_info'],
        'featured_projects': featured_projects,
        'backend_skills': backend_skills,
        'data_skills': data_skills,
        'devops_skills': devops_skills,
        'recent_experience': recent_experience,
    }
    return render(request, 'main/home.html', context)

def about(request):
    """About page view"""
    data = load_portfolio_data()
    
    context = {
        'personal_info': data['personal_info'],
        'experiences': data['experience'],
    }
    return render(request, 'main/about.html', context)

def projects(request):
    """Projects listing page"""
    data = load_portfolio_data()
    projects_list = data['projects']

    # Split into personal vs professional/industry projects
    personal_projects = [p for p in projects_list if p.get('group', 'personal') == 'personal']
    professional_projects = [p for p in projects_list if p.get('group') == 'professional']
    
    context = {
        'personal_info': data['personal_info'],
        'personal_projects': personal_projects,
        'professional_projects': professional_projects,
    }
    return render(request, 'main/projects.html', context)

def project_detail(request, project_id):
    """Individual project detail page"""
    data = load_portfolio_data()
    
    # Find project by ID
    project = None
    for p in data['projects']:
        if p['id'] == project_id:
            project = p
            break
    
    if not project:
        return render(request, 'main/404.html', status=404)
    
    context = {
        'personal_info': data['personal_info'],
        'project': project,
    }
    return render(request, 'main/project_detail.html', context)

def contact(request):
    """Contact page"""
    data = load_portfolio_data()
    
    context = {
        'personal_info': data['personal_info'],
    }
    return render(request, 'main/contact.html', context)

def skills(request):
    """Skills page with detailed skill information"""
    data = load_portfolio_data()
    
    context = {
        'personal_info': data['personal_info'],
        'backend_skills': data['skills']['backend'],
        'data_skills': data['skills']['data'],
        'devops_skills': data['skills']['devops'],
    }
    return render(request, 'main/skills.html', context)

def health_check(request):
    """Health check endpoint for Docker/Coolify"""
    return JsonResponse({'status': 'healthy', 'service': 'portfolio'})