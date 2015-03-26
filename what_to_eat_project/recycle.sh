rm db.sqlite3
rm whatToEat/migrations/00*
python manage.py makemigrations
echo
echo
python manage.py migrate
echo
echo DB teardown and migration completed
echo
echo Adding Watson..
echo
python manage.py buildwatson
python manage.py installwatson
echo
echo Watson added
echo
echo Attempting population...
echo
python populate_whatToEat.py
