init:
	mkdir -p ./database/mongo
	mkdir -p ./database/mysql

start:
	docker-compose up -d

end:
	docker-compose down