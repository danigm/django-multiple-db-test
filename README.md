https://docs.djangoproject.com/en/1.9/topics/db/multi-db/

This project is a test for django multiple database functionality. There're
two django apps, main and disp, and a DatabaseRouter to select a diferent
db for all models in disp. Other models goes to main.

## How to use?

```
$ python manage.py migrate
$ python manage.py migrate --database=disp
```

This will create db.sqlite3 with all django tables and db2.sqlite3 with
disp tables.

```
$ python manage.py shell
>>> from main.models import Main
>>> from disp.models import Disp
>>> for i in range(10):
>>>   Main().save()
>>>   Disp().save()
```

This will create 10 rows in main\_main table in db.sqlite3 and 10 rows in
disp\_disp in db2.sqlite3

## Important files

 * disp/db.py
 * testdb/settings.py
    - DATABASES
    - DATABASE\_ROUTES
