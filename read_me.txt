This is a simple Django REST API for creating and updating blog posts. The API allows you to create a new blog post, update an existing blog post, list all blog posts, and delete a blog post by ID.
Installation
To install and run this project below are steps-

1)-Clone the repository:

git clone https://github.com/your-username/django-blog-api.git
Navigate into the project directory:

cd django-blog-api
Create a virtual environment:
python -m venv env
Activate the virtual environment:
On Windows:
env\Scripts\activate


2)- reqirements.txt work-
pip install -r requirements.txt
run this command after activating your virtual environment.

3)-run your local server
python manage.py runserver
API Endpoints

4)-The following API endpoints are available:
POST /create/: Creates a new blog post. 
PUT /update/id>/ for updating
GET /all/: Lists all blog posts. 
DELETE /delete/id>/ Deletes a blog post with the given ID.

5)-Packages Used
The following packages were used in this project:
Django
djangorestframework
python-dotenv
sqlite3
Requirements.txt
