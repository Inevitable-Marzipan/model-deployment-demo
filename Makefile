SHELL := $(shell type bash | cut -d ' ' -f 3)

build-app:
	docker build -f Dockerfile.inference -t demo-app . 

run-app:
	docker run -d -p 8080:8080 demo-app
