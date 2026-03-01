To access database while docker is running 

1) docker ps

2) docker exec -it <container_name> psql -U postgres -d fastapi_db

for example 

3) docker exec -it my_postgres_container psql -U postgres -d fastapi_db