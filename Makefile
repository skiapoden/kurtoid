.PHONY: run stop clean

run .image: Dockerfile
	docker build -t kurtoid .
	touch .image
	docker run -it --rm --name kurtoidapp -p 5000:5000 kurtoid

push: .image
	docker build -t kurtoid .
	docker tag kurtoid:latest paedubucher/kurtoid:latest
	docker push paedubucher/kurtoid:latest

stop:
	docker rm -f kurtoidapp

clean:
	docker rmi kurtoid
