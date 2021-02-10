test_default_package:
	rm -rf git_workshop_testing
	cookiecutter --no-input --directory $(shell pwd) git_workshop_testing
	# needs to be in one line otherwise the working directory does not change
	cd git_workshop_testing; pip install -e . ; tox --recreate
