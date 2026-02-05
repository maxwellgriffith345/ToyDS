## Last Update 2/3
- Created weather container with a postgre database
- started a compose file to use to build the container
- open psql terminal with in the contrainer to work with the database

## Last Update 2/4
- tied the schema.sql file to the init-db for the container so it builds the db on start up
- trying to get the bash script to work for loading the data, running into an issue where the db is not ready to accept input before calling the load command?

## NEXT STEP
- load in the weather events data using bash script

## NEXT NEXT STEP
- figure out how to automate it all
  - compose for the docker file
  - bash file for all the other commands?
