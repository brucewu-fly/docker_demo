DOCKER_NAMESPACE?=docker_demo
DOCKER_TAG?=latest

.PHONY: docker-image
docker-image:
	docker build -t $(DOCKER_NAMESPACE)/send_request:${DOCKER_TAG} send_request/

.PHONY: up
up:
	docker-compose -f docker-compose/docker-compose.yml up -d

.PHONY: stop
stop:
	docker-compose -f docker-compose/docker-compose.yml stop

.PHONY: rm
rm:
	docker-compose -f docker-compose/docker-compose.yml rm -f
