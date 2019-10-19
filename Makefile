.PHONY: run stop clean

run: Dockerfile
	docker build -t kurtoid .
	docker run -it --rm --name kurtoidapp -p 8000:8000 kurtoid

stop:
	docker rm -f kurtoidapp

clean:
	docker rmi kurtoid
