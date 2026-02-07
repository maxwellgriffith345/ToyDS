## Last Update 2/3
- Created weather container with a postgre database
- started a compose file to use to build the container
- open psql terminal with in the contrainer to work with the database

## Last Update 2/5
- tied the schema.sql file to the init-db for the container so it builds the db on start up
- command to load data from csv file works
- trying to get the bash script to work for loading the data, running into an issue where the db is not ready to accept input before calling the load command?

## Last Update 2/7
- used pg_ready to check the status of the connection before loading db
- I think there is an issue with the db restarting
- the bash script works to atuomate building the contrainer and the data Database
- CALLING IT DONE: Minimual vialbe product


## NEXT STEP
- load in the weather events data using bash script
