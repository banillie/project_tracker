run-dev:
	python manage.py runserver --settings=project_tracker.settings_local

dev-shell:
	python manage.py shell --settings=project_tracker.settings_local

dev-super:
	python manage.py createsuperuser --settings=project_tracker.settings_local

dev-makemigrations:
	python manage.py makemigrations --settings=project_tracker.settings_local

dev-migrate:
	python manage.py migrate --settings=project_tracker.settings_local

start-sql-proxy:
	./cloud_sql_proxy -instances="dft-ppd-prt-projectengtracker:europe-west1:tracker"=tcp:5432

open-sql-proxy:
	export GOOGLE_CLOUD_PROJECT=dft-ppd-prt-projectengtracker
	export USE_CLOUD_SQL_AUTH_PROXY=true
	python manage.py runserver

