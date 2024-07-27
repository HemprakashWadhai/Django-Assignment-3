# HealthBlog Project

HealthBlog is a comprehensive Django-based web application that integrates user authentication, a blog feature for healthcare professionals, and an appointment booking system.

## Features

### User Authentication and Profile Management

- User registration for doctors and patients.
- User login and logout functionality.
- Profile management including profile pictures and contact information.

### Blogging for Doctors

- Doctors can create, edit, and delete blog posts.
- Blog posts can be categorized into various health topics.
- All blog posts are viewable by patients.

### Appointment Booking System

- Patients can book appointments with doctors.
- Doctors can view their appointment schedules.
- Appointment management including booking and viewing details.

## Directory Structure

- `HealthBlog/` - Main project directory.
    - `__init__.py` - Initializes the Django project.
    - `settings.py` - Configuration settings for the project.
    - `urls.py` - URL routing for the main project.
    - `wsgi.py` - WSGI configuration for the project.
- `accounts/` - User authentication and profile management module.
    - `__init__.py` - Initializes the accounts module.
    - `admin.py` - Admin configuration for user models.
    - `apps.py` - App configuration.
    - `forms.py` - Forms for user registration and profile management.
    - `models.py` - User model with custom fields.
    - `tests.py` - Unit tests for the accounts module.
    - `urls.py` - URL routing for accounts-related views.
    - `views.py` - Views for handling user authentication and profile management.
- `blog/` - Blogging module for doctors.
    - `__init__.py` - Initializes the blog module.
    - `admin.py` - Admin configuration for blog models.
    - `apps.py` - App configuration.
    - `forms.py` - Forms for creating and editing blog posts.
    - `models.py` - Blog post model with categories.
    - `tests.py` - Unit tests for the blog module.
    - `urls.py` - URL routing for blog-related views.
    - `views.py` - Views for creating, editing, and displaying blog posts.
- `appointments/` - Appointment booking system.
    - `__init__.py` - Initializes the appointments module.
    - `admin.py` - Admin configuration for appointment models.
    - `apps.py` - App configuration.
    - `forms.py` - Forms for booking appointments.
    - `models.py` - Appointment model.
    - `tests.py` - Unit tests for the appointments module.
    - `urls.py` - URL routing for appointments-related views.
    - `views.py` - Views for booking and viewing appointments.
- `templates/` - HTML templates for the application.
    - `signup.html` - Template for user registration.
    - `doctor_dashboard.html` - Template for the doctor dashboard.
    - `my_blog_posts.html` - Template for viewing a user's blog posts.
    - `create_blog_post.html` - Template for creating a new blog post.
    - `blog_list.html` - Template for viewing all blog posts.
    - `book_appointment.html` - Template for booking an appointment.
    - `view_appointments.html` - Template for viewing appointments.

## Setup

1. Clone the repository.
2. Navigate to the project directory.
3. Install the required packages using `pip install -r requirements.txt`.
4. Run `python manage.py migrate` to set up the database.
5. Create a superuser using `python manage.py createsuperuser`.
6. Start the server with `python manage.py runserver`.

## Usage

- Access the admin interface at `/admin/` to manage users and content.
- Register as a doctor or patient at `/accounts/signup/`.
- Doctors can create and manage blog posts at `/blogs/create/` and `/blogs/my-blogs/`.
- Patients can book appointments with doctors at `/appointments/book/`.

## Contributing

Feel free to submit issues or pull requests for improvements and bug fixes.

## License

This project is licensed under the MIT License.
