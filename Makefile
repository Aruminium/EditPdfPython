u:
	docker compose up -d

b: docker-compose.yml
	docker compose build

d:
	docker compose down
e:
	sh docker-exec.sh