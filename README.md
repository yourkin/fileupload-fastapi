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
TESTING=True\
BACKEND_CORS_ORIGINS=["http://localhost:8004", "https://uploads.example.com"]

### Bring up the stack
`docker-compose up --build -d`

### Run the unit tests 

`docker-compose exec web python -m pytest`

### Check the OpenAPI docs 

In development mode, OpenAPI documentation is available at

http://localhost:8004/docs

### Alternatives

An alternative implementation would be to use the tus resumable upload protocol
https://github.com/tus/tus-resumable-upload-protocol

#### Varnish HTTP Cache

It is also possible to use a tus module for the Varnish HTTP Cache

https://code.uplex.de/uplex-varnish/libvmod-tus