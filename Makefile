DOCKER_NAMESPACE?=docker_demo
DOCKER_TAG?=latest

.PHONY: docker-image
docker-image:
	docker build -t $(DOCKER_NAMESPACE)/send_request:${DOCKER_TAG} send_request/

.PHONY: docker-run
docker-run:
	docker run -it --rm $(DOCKER_NAMESPACE)/send_request:${DOCKER_TAG}
