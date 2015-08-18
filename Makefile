usage: # Print Targets
	@grep '^[^#[:space:]].*:' Makefile

docs:
	doxygen docs/Doxyfile
	cd docs && mkdocs build

clean:
	git clean -fdX

.PHONY: docs clean
