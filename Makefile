

usage: # Print Targets
	@grep '^[^#[:space:]].*:' Makefile

runserver:
	cd ofdat && python manage.py runserver

docs:
	doxygen docs/Doxyfile
	cd docs && mkdocs build

clean:
	git clean -fdX
	cd ofdat && python manage.py migrate

test:
	cd ofdat && python manage.py test

.PHONY: docs clean test runserver
