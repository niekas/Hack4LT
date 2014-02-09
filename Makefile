.PHONY: install run static tags

all: install collect_static

install:
	python bootstrap.py
	bin/buildout
	bin/django migrate hack4lt
	bin/django compilemessages

run:
	bin/django runserver

collect_static:
	bin/django collectstatic --noinput

change_db:
	bin/django schemamigration hack4lt --auto
	bin/django migrate hack4lt

test:
	bin/django test hack4lt

start_database:
	mkdir var || touch var/db
	bin/django syncdb --noinput
	bin/django migrate hack4lt
	# bin/django loaddata initial.json

tags:
	bin/ctags -v
