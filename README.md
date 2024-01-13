# travel_helper
### Clone the Repository
# git clone https://github.com/shahriarmohim-bs23/travel_helper.git
cd travel_helper
### Create Virtual Environment
pip3 install virtualenv
virtualenv venv
source venv/bin/activate
### Create .env File
# Database configuration
```
POSTGRES_DB=postgres(example) 
POSTGRES_USER=postgres(example) 
POSTGRES_PASSWORD=postgres(example) 
POSTGRES_HOST=localhost 
POSTGRES_PORT=5432
# Secret key for Django (replace with a strong, random value)
SECRET_KEY=mysecretkey

# Other configuration variables
DEBUG=True
### Install Dependencies
pip3 install -r requirements.txt
### Create a Superuser
python3 manage.py createsuperuser
### Run the Project
python3 manage.py runserver



