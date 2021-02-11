test_default_package:
	rm -rf git_workshop_testing
	cookiecutter --no-input --directory $(shell pwd) git_workshop_testing
	# needs to be in one line otherwise the working directory does not change
	cd git_workshop_testing; pip install -e . ; tox --recreate


start_gitlab_runner:
	# create the config for the container
	docker volume create gitlab-runner-workshop-config
	# start the docker container
	docker run -d --name gitlab-runner-workshop --restart always \
     -v /var/run/docker.sock:/var/run/docker.sock \
     -v gitlab-runner-workshop-config:/etc/gitlab-runner \
     gitlab/gitlab-runner:latest
