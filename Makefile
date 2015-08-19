

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
	#Django tests
	cd ofdat && python manage.py test
	#Documentation tests
	nosetests --with-doctest --doctest-extension=md -w docs/docs/

.PHONY: docs clean test runserver
