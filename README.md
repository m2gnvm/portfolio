# Kamil Stańkowski - Portfolio Website

A modern, responsive portfolio website built with Django showcasing my work as a Software Engineer specializing in Backend Development, Data Engineering, and DevOps.

## 🚀 Features

- **Modern Design**: Clean, responsive design with Bootstrap 5
- **Dynamic Content**: Django admin interface for easy content management
- **Project Showcase**: Detailed project pages with technology tags
- **Skills Display**: Organized by categories with proficiency levels
- **Experience Timeline**: Professional experience with detailed descriptions
- **Contact Form**: Working contact form with email integration
- **SEO Optimized**: Meta tags and structured data for better search visibility
- **Mobile Responsive**: Optimized for all device sizes

## 🛠️ Tech Stack

- **Backend**: Django 4.2, Python 3.11+
- **Frontend**: HTML5, CSS3, JavaScript, Bootstrap 5
- **Database**: SQLite (development), PostgreSQL (production)
- **Styling**: Custom CSS with Bootstrap components
- **Icons**: Font Awesome 6
- **Fonts**: Google Fonts (Inter)

## 📋 Prerequisites

- Python 3.11 or higher
- pip (Python package installer)
- Git

## 🚀 Quick Start

### 1. Clone the Repository

```bash
git clone https://github.com/m2gnvm/portfolio.git
cd portfolio
```

### 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Environment Setup

```bash
cp env.example .env
# Edit .env file with your settings
```

### 5. Database Setup

```bash
python manage.py migrate
python manage.py createsuperuser
python manage.py populate_portfolio
```

### 6. Run Development Server

```bash
python manage.py runserver
```

Visit `http://127.0.0.1:8000` to see your portfolio!

## 🐳 Docker Deployment

### Using Docker Compose (Recommended)

```bash
# Build and run with Docker Compose
docker-compose up --build

# Run in background
docker-compose up -d --build
```

### Using Docker

```bash
# Build the image
docker build -t portfolio .

# Run the container
docker run -p 8000:8000 portfolio
```

## 📁 Project Structure

```
portfolio/
├── main/                    # Main Django app
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── urls.py             # URL patterns
│   ├── admin.py            # Admin interface
│   ├── forms.py            # Django forms
│   └── management/         # Custom management commands
├── portfolio/              # Django project settings
│   ├── settings.py         # Django settings
│   ├── urls.py             # Main URL configuration
│   └── wsgi.py             # WSGI configuration
├── templates/              # HTML templates
│   ├── base.html           # Base template
│   └── main/               # App-specific templates
├── static/                 # Static files
│   ├── css/                # Custom CSS
│   └── js/                 # JavaScript files
├── media/                  # User uploaded files
├── requirements.txt        # Python dependencies
├── Dockerfile             # Docker configuration
├── docker-compose.yml     # Docker Compose configuration
└── README.md              # This file
```

## 🎨 Customization

### Adding New Projects

1. Go to Django Admin (`/admin/`)
2. Navigate to "Projects"
3. Click "Add Project"
4. Fill in the project details
5. Save and publish

### Managing Skills

1. Go to Django Admin (`/admin/`)
2. Navigate to "Skill Categories" to add new categories
3. Navigate to "Skills" to add individual skills
4. Set proficiency levels and years of experience

### Updating Personal Information

1. Go to Django Admin (`/admin/`)
2. Navigate to "Personal Information"
3. Update your details, bio, and contact information
4. Upload a profile image and resume

## 🚀 Production Deployment

### Environment Variables

Set these environment variables for production:

```bash
SECRET_KEY=your-production-secret-key
DEBUG=False
ALLOWED_HOSTS=yourdomain.com,www.yourdomain.com
DATABASE_URL=postgresql://user:password@localhost:5432/portfolio_db
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

### Database Migration

```bash
python manage.py migrate
python manage.py collectstatic --noinput
python manage.py populate_portfolio
```

### Static Files

For production, configure your web server (Nginx/Apache) to serve static files:

```nginx
location /static/ {
    alias /path/to/your/portfolio/staticfiles/;
}

location /media/ {
    alias /path/to/your/portfolio/media/;
}
```

## 📧 Contact Form Setup

To enable the contact form, configure email settings in your `.env` file:

```bash
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your-email@gmail.com
EMAIL_HOST_PASSWORD=your-app-password
```

For Gmail, you'll need to:
1. Enable 2-factor authentication
2. Generate an app-specific password
3. Use the app password in `EMAIL_HOST_PASSWORD`

## 🎯 Features Overview

### Homepage
- Hero section with personal introduction
- Skills overview by category
- Featured projects showcase
- Current role highlight

### About Page
- Detailed personal bio
- Professional experience timeline
- Education background
- Technical skills with proficiency levels

### Projects Page
- Project grid with filtering
- Search functionality
- Project type filtering
- Pagination for large project lists

### Project Detail Pages
- Detailed project descriptions
- Technology stack display
- Project links (GitHub, Live demo)
- Related projects suggestions

### Skills Page
- Skills organized by category
- Proficiency level indicators
- Years of experience
- Featured skills highlighting

### Contact Page
- Working contact form
- Personal contact information
- Social media links
- Resume download option

## 🔧 Management Commands

### Populate Portfolio Data

```bash
python manage.py populate_portfolio
```

This command populates the database with initial data from your CV, including:
- Personal information
- Skill categories and skills
- Work experience
- Education
- Sample projects

## 📱 Responsive Design

The portfolio is fully responsive and optimized for:
- Desktop computers (1200px+)
- Tablets (768px - 1199px)
- Mobile phones (320px - 767px)

## 🎨 Design Features

- **Modern UI**: Clean, professional design
- **Smooth Animations**: CSS transitions and hover effects
- **Interactive Elements**: Dynamic skill bars, project cards
- **Typography**: Google Fonts (Inter) for better readability
- **Color Scheme**: Professional blue and gray palette
- **Icons**: Font Awesome icons throughout the interface

## 🚀 Performance Optimizations

- **Static File Optimization**: Compressed CSS and JavaScript
- **Image Optimization**: Responsive images with proper sizing
- **Database Queries**: Optimized with select_related and prefetch_related
- **Caching**: Ready for Redis caching implementation
- **CDN Ready**: Static files can be served from CDN

## 📈 SEO Features

- **Meta Tags**: Title, description, and keywords
- **Structured Data**: Schema.org markup ready
- **Sitemap**: Django sitemap framework integration
- **URL Structure**: Clean, SEO-friendly URLs
- **Open Graph**: Social media sharing optimization

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add some amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📞 Contact

**Kamil Stańkowski**
- Email: kamilstankowski98@gmail.com
- LinkedIn: [linkedin.com/in/kamil-stańkowski-8b1a661b9](https://www.linkedin.com/in/kamil-sta%C5%84kowski-8b1a661b9/)
- GitHub: [github.com/m2gnvm](https://github.com/m2gnvm)

## 🙏 Acknowledgments

- Django framework and community
- Bootstrap for the responsive framework
- Font Awesome for the icons
- Google Fonts for typography
- All the open-source contributors

---

**Built with ❤️ using Django and modern web technologies**



