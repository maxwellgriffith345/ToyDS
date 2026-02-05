#! /usr/local/bin/bash

echo "Building Weather Database"

# build the container
docker compose up -d

# access the database
# docker exec -it container_name psql -U username dbname
# docker exec: runs a command inside a container
# -i interactive: -t opens a terminal
# docker exec -it weathercnt psql -U myuser weatherdb

# get logs for the container
# docker logs -f container_name

# need to use wait for sleep here to wait until db is fully built

echo "Data base Built"
echo "Loading Data"

# load the csv file into the db
docker exec -i weathercnt \
    psql -U myuser -d weatherdb \
    -c "\copy weather_events FROM STDIN WITH (FORMAT csv, HEADER true)" \
    < ./rawdata/stormevents.csv


echo "Data load finished"
