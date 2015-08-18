usage: # Print Targets
	@grep '^[^#[:space:]].*:' Makefile

docs:
	doxygen docs/Doxyfile

clean:
	git clean -fdX

.PHONY: docs clean
