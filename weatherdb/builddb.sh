#! /usr/local/bin/bash

echo "Building Weather Database"

# build the container
docker compose up -d

# access the database
# docker exec -it container_name psql -U username dbname
# docker exec: runs a command inside a container
# -i interactive: -t opens a terminal
# docker exec -it weathercnt psql -U myuser weatherdb 
