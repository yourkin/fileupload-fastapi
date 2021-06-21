## Instructions for use

### Create a .env file in the source folder
####
Set the necessary environment variables in .env, for instance:

FILESTORE_DIR=/data/filestore\
PG_USER=postgres\
PG_PASSWORD=postgres\
PG_DB=web_dev\
PG_DB_TEST=web_test\
ENVIRONMENT=dev\
TESTING=True

### Bring up the stack
`docker-compose up --build -d`

### Run the unit tests 

`docker-compose exec web python -m pytest`

### Check the OpenAPI docs 

In development mode, OpenAPI documentation is available at

http://localhost:8004/docs