

### Requirements
1. mysql / postgresSql
2. Python 3 
3. Docker

### New Installation

1. Navigate to folder
1. `python3 -m venv venv` - [Virtual env docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/#creating-a-virtual-environment)
1. `source venv/bin/activate`
1. `pip install -r requirements.txt`
1. If the above step couldn't install psycopg2 then follow this link on macos - https://stackoverflow.com/a/56110800
1. `docker-compose up db`
1. `python manage.py migrate`

### Running the server
1. `python manage.py runserver`

### API docs

1. Run the server and open `localhost:8000/api/` to open swagger.



