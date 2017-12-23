# Feedbacks



### Installations

Clone project from git repository
* `git clone git@github.com:BakitD/Feedbacks.git`

Next commands were executed on Linux (Debian). <br/>
Some of them could differ depending on system you are working on. <br/>

* `virtualenv -p PATH_TO_PYTHON3  venv` or
* `virtualenv --python=PATH_TO_PYTHON3 venv`

where PATH_TO_PYTHON3 is path to python3. <br/>
Usually this path is `/usr/bin/python3` for Linux (Ubuntu, Debian).


* `source venv/bin/activate`
* `pip install -r requirements.txt`
* `python manage.py db init`
* `python manage.py db migrate`
* `python manage.py db upgrade`


to deactivate venv use `deactivate`

### Run server
* `python manage.py runserver`
* Open browser with address `localhost:5000` or `127.0.0.1:5000` 
