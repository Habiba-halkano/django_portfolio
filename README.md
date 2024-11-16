## Django Portfolio Project
A responsive and professional portfolio website built with Django, showcasing skills, projects, and professional background, complete with a functional contact form.

### Features
## About Page:

Includes a personal introduction with a professional photo.
Lists skills and hobbies.
Fully responsive layout with side-by-side content for larger screens.

## Projects Page:

Dynamically displays a list of projects with details such as titles, descriptions, and links to demos or repositories.
Data is stored in a database, allowing easy updates.

## Contact Page:

Functional contact form with fields for name, email, phone, and message.
Validations ensure proper input (e.g., valid email, minimum message length, and formatted phone numbers).
Submissions are saved in a database.

## Consistent Design:

Unified color scheme across all pages.
Stylish navbar and footer.
Hover effects for interactive elements.
## Responsive Design:

Optimized for mobile, tablet, and desktop devices.
Clean layout using Flexbox and Grid.

## Technology Stack
Backend: Django Framework <br> 
Frontend: HTML5, CSS (with Flexbox & Grid) <br>
Database: SQLite (default Django database)

## Setup Instructions
1. Clone the Repository
bash
Copy code
git clone https://github.com/Habiba-halkano/django-portfolio.git
cd django-portfolio
2. Create and Activate a Virtual Environment
bash
Copy code
python -m venv venv
source venv/bin/activate  # On Windows, use venv\Scripts\activate
3. Install Dependencies
bash
Copy code
pip install -r requirements.txt
4. Run Migrations
bash
Copy code
python manage.py makemigrations
python manage.py migrate
5. Start the Development Server
bash
Copy code
python manage.py runserver
6. Access the Website
Visit http://127.0.0.1:8000 in your browser.


### Key Highlights
## Database Models:

1. Contact: Stores contact form submissions.
2. Projects: Stores dynamic project details.
3. Django Forms: Validates user input for the contact form.
4. Styling: Unified and responsive design using a single style.css file.
            Professional and clean look with a consistent color scheme.

### Future Improvements
Add user authentication for managing projects and contact submissions.
Integrate a real email service for the contact form.
Enhance animations and transitions for improved user experience.

### Contact
For questions or collaborations, feel free to reach out:

Name: Habiba Halkano <br> 
Email: halkanohabiba8@gmail.com <br>
GitHub: https://github.com/Habiba-halkano
