SHELL := $(shell type bash | cut -d ' ' -f 3)

build-app:
	docker build -f Dockerfile.inference -t demo-app:latest . 

run-app:
	docker run -d -p 8080:8080 demo-app\:latest

login-docker:
	aws ecr get-login-password --region eu-west-2 | docker login --username AWS --password-stdin ${ECR_REPO}

push-image-ecr:
	docker tag demo-app:latest ${ECR_REPO}:latest
	docker push ${ECR_REPO}:latest
