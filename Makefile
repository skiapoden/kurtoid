.PHONY: run debug stop clean

run .container: Dockerfile
	docker build -t kurtoid .
	docker run -it --rm --name kurtoidapp -p 8000:8000 kurtoid

debug: .container
	docker exec -it kurtoidapp bash

stop:
	docker rm -f kurtoidapp
	rm -f .container

clean:
	docker rmi kurtoid
	rm -f .image
