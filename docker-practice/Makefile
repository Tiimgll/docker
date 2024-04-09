mongo:
	docker run -p 27017:27017 \
		-d \
		--rm \
		--name mongodb \
		--network notes-net \
		-v mongo-data:/data/db \
		--env-file .\config\development.env \
		mongo

backend:
#	docker build -t notes-server ./server
	docker run -p 5000:5000 \
		-d \
		--rm \
		--name notes-backend \
		--network notes-net \
		--env-file .\config\development.env \
		notes-server

frontend:
#	docker  build -t notes-client ./client
	docker run -p 3000:3000 \
	-d \
	--rm \
	--name notes-frontend \
	--network notes-net \
	notes-client

stop:
	docker stop  $(shell docker ps -a -q)

start:
	docker-compose -f docker-compose.yaml up -d

## режим разработки (в dockerfile server поменять CMD)

backend-dev:
#	docker build -t notes-server ./server
	docker run -p 5000:5000 \
		-d \
		--rm \
		--name notes-backend \
		--network notes-net \
		-v ./server:/app \
		-v /app/node_modules \
		--env-file .\config\development.env \
		notes-server

frontend-dev:
#	docker  build -t notes-client ./client
	docker run -p 3000:3000 \
	-d \
	--rm \
	--name notes-frontend \
	--network notes-net \
	-v ./client/src:/app/src \
	notes-client

dev: 
	docker-compose -f docker-compose-dev.yaml up -d