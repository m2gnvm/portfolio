from django.core.management.base import BaseCommand
from main.models import (
    PersonalInfo, SkillCategory, Skill, Project, Experience, Education
)


class Command(BaseCommand):
    help = 'Populate the portfolio with initial data from CV'

    def handle(self, *args, **options):
        self.stdout.write('Populating portfolio with CV data...')
        
        # Create Personal Information
        personal_info, created = PersonalInfo.objects.get_or_create(
            name='Kamil Stańkowski',
            defaults={
                'title': 'Software Engineer | Backend Developer | Data Engineer',
                'bio': 'Dynamic and detail-oriented Back End and Data Engineer with over 5 years of experience in software engineering, specializing in building robust backend systems and data processing solutions. Proficient in a range of programming languages and tools, committed to leveraging big data technologies to enhance business operations.',
                'short_bio': 'Software Engineer specializing in Backend, Data Engineering, and DevOps with 5+ years of experience.',
                'email': 'kamilstankowski98@gmail.com',
                'phone': '660 235 016',
                'location': 'Warsaw, Poland',
                'linkedin_url': 'https://www.linkedin.com/in/kamil-sta%C5%84kowski-8b1a661b9/',
                'github_url': 'https://github.com/m2gnvm',
                'meta_title': 'Kamil Stańkowski - Software Engineer',
                'meta_description': 'Software Engineer specializing in Backend, Data Engineering, and DevOps. 5+ years experience with Python, Django, FastAPI, PySpark, Kafka, Docker, and Kubernetes.'
            }
        )
        
        if created:
            self.stdout.write(self.style.SUCCESS('Created personal information'))
        else:
            self.stdout.write('Personal information already exists')

        # Create Skill Categories
        backend_category, created = SkillCategory.objects.get_or_create(
            name='Backend Development',
            defaults={
                'description': 'Server-side development, APIs, and backend systems',
                'icon': 'fas fa-server',
                'color': '#007bff',
                'order': 1
            }
        )
        
        data_category, created = SkillCategory.objects.get_or_create(
            name='Data Engineering',
            defaults={
                'description': 'Big data processing, ETL pipelines, and data analytics',
                'icon': 'fas fa-database',
                'color': '#28a745',
                'order': 2
            }
        )
        
        devops_category, created = SkillCategory.objects.get_or_create(
            name='DevOps & Cloud',
            defaults={
                'description': 'Containerization, orchestration, and cloud platforms',
                'icon': 'fas fa-cloud',
                'color': '#17a2b8',
                'order': 3
            }
        )

        # Create Skills
        backend_skills = [
            ('Python', 9, 5.0, True),
            ('Django', 8, 4.0, True),
            ('FastAPI', 8, 2.0, True),
            ('RESTful API', 8, 4.0, True),
            ('PostgreSQL', 7, 4.0, False),
            ('MySQL', 7, 3.0, False),
            ('Redis', 6, 2.0, False),
            ('PHP', 6, 2.0, False),
        ]

        data_skills = [
            ('PySpark', 8, 3.0, True),
            ('Kafka', 7, 2.0, True),
            ('Hadoop', 6, 2.0, True),
            ('MongoDB', 7, 3.0, False),
            ('Pandas', 8, 4.0, False),
            ('NumPy', 7, 4.0, False),
            ('Airflow', 6, 2.0, False),
        ]

        devops_skills = [
            ('Docker', 8, 3.0, True),
            ('Kubernetes', 6, 1.0, True),
            ('Linux', 7, 5.0, True),
            ('AWS', 6, 2.0, False),
            ('Git', 8, 5.0, False),
            ('Selenium', 6, 2.0, False),
        ]

        for skill_name, proficiency, years, featured in backend_skills:
            Skill.objects.get_or_create(
                name=skill_name,
                category=backend_category,
                defaults={
                    'proficiency_level': proficiency,
                    'years_experience': years,
                    'is_featured': featured
                }
            )

        for skill_name, proficiency, years, featured in data_skills:
            Skill.objects.get_or_create(
                name=skill_name,
                category=data_category,
                defaults={
                    'proficiency_level': proficiency,
                    'years_experience': years,
                    'is_featured': featured
                }
            )

        for skill_name, proficiency, years, featured in devops_skills:
            Skill.objects.get_or_create(
                name=skill_name,
                category=devops_category,
                defaults={
                    'proficiency_level': proficiency,
                    'years_experience': years,
                    'is_featured': featured
                }
            )

        # Create Experience
        experiences = [
            {
                'company': 'Cyfrowy Polsat S.A.',
                'position': 'Back-End | BI Developer',
                'location': 'Warsaw, Poland',
                'start_date': '2024-12-01',
                'current': True,
                'description': 'Design and develop BI pipelines to process and analyze data from the Polsat Box Go platform. Build REST endpoints to distribute and expose business data. Create data models and reporting solutions to support business intelligence needs.',
                'technologies': ['Python', 'PostgreSQL', 'PySpark', 'Kafka', 'Redis', 'MongoDB', 'Docker', 'RESTful API']
            },
            {
                'company': 'REDS S.A.',
                'position': 'Back-End | Data Engineer',
                'location': 'Warsaw, Poland',
                'start_date': '2022-09-01',
                'end_date': '2024-11-30',
                'current': False,
                'description': 'Built real-time data processing pipelines with PySpark for ingesting and transforming streaming data. Designed and documented data models and flows to improve architecture. Developed an end-to-end data warehouse integrating Kafka and PySpark for analytics. Delivered ETL pipelines to process and analyze railway telemetry in near real-time.',
                'technologies': ['PySpark', 'Kafka', 'Hadoop', 'Airflow']
            },
            {
                'company': 'Abis Sp. z o.o.',
                'position': 'Software Engineer',
                'location': 'Warsaw, Poland',
                'start_date': '2020-06-01',
                'end_date': '2022-08-31',
                'current': False,
                'description': 'Develop backend systems and optimize database infrastructure. Build reporting platforms and analytical dashboards. Design and maintain MySQL databases and schemas. Automate workflows with Python scripts and PyQt applications. Support PHP-based web development and system integrations.',
                'technologies': ['MySQL', 'Python', 'PyQt', 'PHP', 'Linux']
            },
            {
                'company': 'Giganci Programowania',
                'position': 'Programming Teacher',
                'location': 'Warsaw, Poland',
                'start_date': '2020-03-01',
                'end_date': '2022-06-30',
                'current': False,
                'description': 'Taught programming concepts and best practices to students. Developed curriculum and learning materials for various programming languages and frameworks.',
                'technologies': ['Python', 'Django', 'JavaScript']
            }
        ]

        for exp_data in experiences:
            technologies = exp_data.pop('technologies')
            experience, created = Experience.objects.get_or_create(
                company=exp_data['company'],
                position=exp_data['position'],
                defaults=exp_data
            )
            
            if created:
                # Add technologies
                for tech_name in technologies:
                    try:
                        skill = Skill.objects.get(name=tech_name)
                        experience.technologies.add(skill)
                    except Skill.DoesNotExist:
                        pass

        # Create Education
        education_data = [
            {
                'institution': 'Warsaw University of Life Sciences',
                'degree': 'Master of Science',
                'field_of_study': 'Computer Science and Econometrics',
                'start_date': '2023-10-01',
                'current': True,
                'description': 'Specialization: Big Data'
            },
            {
                'institution': 'Military University of Technology',
                'degree': 'Master of Science in Engineering',
                'field_of_study': 'Electronics and Telecommunication',
                'start_date': '2022-03-01',
                'end_date': '2024-07-31',
                'current': False,
                'description': 'Specialization: Safety Systems Engineering'
            },
            {
                'institution': 'Warsaw University of Technology',
                'degree': 'Bachelor of Science in Engineering',
                'field_of_study': 'Electronics',
                'start_date': '2017-10-01',
                'end_date': '2022-02-28',
                'current': False,
                'description': 'Specialization: Electronics and Computer Engineering'
            }
        ]

        for edu_data in education_data:
            Education.objects.get_or_create(
                institution=edu_data['institution'],
                degree=edu_data['degree'],
                defaults=edu_data
            )

        # Create Projects
        projects_data = [
            {
                'title': 'Elemental Circle Game Backend',
                'slug': 'elemental-circle-game',
                'description': 'A strategic card game with elemental combat system built with FastAPI, PostgreSQL, and Redis using a hybrid architecture for optimal performance.',
                'long_description': 'This project showcases advanced backend development skills including real-time multiplayer functionality, hybrid database architecture, and scalable system design. The game features WebSocket support for live gameplay, JWT-based authentication, and a sophisticated elemental combat system.',
                'project_type': 'backend',
                'status': 'completed',
                'technologies': ['Python', 'FastAPI', 'PostgreSQL', 'Redis', 'Docker'],
                'github_url': 'https://github.com/m2gnvm/elemental-circle-game',
                'start_date': '2024-01-01',
                'end_date': '2024-06-30',
                'featured': True
            },
            {
                'title': 'Railway Eco-Driving Advisory System',
                'slug': 'railway-eco-driving-system',
                'description': 'Real-time data processing system for railway telemetry with PySpark and Kafka integration.',
                'long_description': 'Developed an end-to-end data warehouse integrating Kafka and PySpark for analytics. Built real-time data processing pipelines for ingesting and transforming streaming data from railway systems. Implemented ETL pipelines to process and analyze railway telemetry in near real-time.',
                'project_type': 'data',
                'status': 'completed',
                'technologies': ['PySpark', 'Kafka', 'Hadoop', 'Airflow'],
                'start_date': '2022-09-01',
                'end_date': '2024-11-30',
                'featured': True
            },
            {
                'title': 'ABIS.PL Backend Platform',
                'slug': 'abis-backend-platform',
                'description': 'Comprehensive backend system with reporting platforms and analytical dashboards.',
                'long_description': 'Developed and maintained the backend infrastructure for ABIS.PL platform. Built reporting platforms and analytical dashboards for business intelligence. Optimized database infrastructure and automated workflows with Python scripts.',
                'project_type': 'backend',
                'status': 'completed',
                'technologies': ['Python', 'MySQL', 'PHP', 'Linux'],
                'start_date': '2020-06-01',
                'end_date': '2022-08-31',
                'featured': False
            }
        ]

        for project_data in projects_data:
            technologies = project_data.pop('technologies')
            project, created = Project.objects.get_or_create(
                slug=project_data['slug'],
                defaults=project_data
            )
            
            if created:
                # Add technologies
                for tech_name in technologies:
                    try:
                        skill = Skill.objects.get(name=tech_name)
                        project.technologies.add(skill)
                    except Skill.DoesNotExist:
                        pass

        self.stdout.write(
            self.style.SUCCESS('Successfully populated portfolio with CV data!')
        )



