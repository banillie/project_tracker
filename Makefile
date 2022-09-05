dev-run:
	python manage.py runserver --settings=project_tracker.settings_local

dev-shell:
	python manage.py shell --settings=project_tracker.settings_local

dev-super:
	python manage.py createsuperuser --settings=project_tracker.settings_local

dev-makemigrations:
	python manage.py makemigrations --settings=project_tracker.settings_local

dev-migrate:
	python manage.py migrate --settings=project_tracker.settings_local

proxy-run:
	python manage.py runserver

proxy-sql-set:
    export GOOGLE_CLOUD_PROJECT=dft-ppd-prt-projectengtracker
	export USE_CLOUD_SQL_AUTH_PROXY=true

proxy-migrate:
	python manage.py migrate

proxy-collectstatic:
	python manage.py collectstatic






