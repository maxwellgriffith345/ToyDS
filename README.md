# ToyDS
Toy DS project to learn end to end flow

# Step 1: Understand DS Project Setup and Create Github repo
- Develope production ready code
- Main Areas
  - Project Structure
  - Advanced Pandas
  - Testing (and typing)
  - Reproducable workflows

- Resources
  - Real Python Project Layouts
  - pytest docs (basics only)

- Knowledge Application
  - GitHub repo with:
    - /src
    - /tests
    - /data
    - /notebooks
  - Unit Tests for Feature Functions

## Notes: Project Structure
- [RP Application Layouts](https://realpython.com/python-application-layouts/)
- [Cookiecutter Data Sci Template](https://cookiecutter-data-science.drivendata.org/)
- [Structuring Python Project](https://trevoramestoy.com/posts/2022/PythonProjects/)
- [Hitchhiker's Guide To Python](https://docs.python-guide.org/)
- The exact location of files matters less than the motivation for grouping similar files
- For a Project called "My_Project" the structure could be:
  - My_Project
    - **my_project(aka src)**: all the main .py files are stored
      - dataset.py: scripts to download or generate data
      - feature.py: code to create features for modeling
      - modeling: train/predict
      - plots.py: code to create visualizations
    - **data**: all the data files .csv .xlsx, subdir for raw and processed
    - **db**: sql scripts to create and load db. schema.sql, load_data.sql
    - **models**: trained and serialized models, predications or model summaries
    - **tests**: all .py files to run tests
    - **notebooks**: juypter notebooks
    - **docs**:
    - **references**: notes, manuals etc etc
    - **reports**: finished analysis PDF or Markdown with figures
    - ReadMe.md, LICENSE, gitignore

- executable shouldn't have much code in it. just an import and a call to a main function in "runner" script
- Never edit your raw data, raw data is immmutable
- Never open raw data in excel or as a csv
- The project and analysis is a one way path without any loops so anyone can re-produce it
- DO move the raw data through a pipeline to your final analysys creating intermediate outputs
- Data should not be kept in source control
  - the data is immmutable so it doesn't change at all (or much)
  - the "data/" folder should be inlcuded in the .gitignore file
  - you have scripts that can rebuild the data if anyone wants to re-run the analysis
- Notebooks are for exploration and communication not finished modeling/reproducing analysis
  -  subdivide "notebooks/" folder inot "exploration/" and "reports/" sub folders
  -  notebooks are challenging for source control
-  Refactor re-used code into source code
  - don't re-write code to do the same task in multiple notebooks
  - pull it out into a module or into the source code
  - if it's for data preprocessing pt it in /data/make_datset.py
-  Don't forget to include the environment details: packages etc (that's where it all starts)
  - Conda has tools for exporting env details
  - virtual machine approach like Docker for more complex envs
- Don't leak your passwords
  - store your secrets in a file that is included in your .gitignore
  - this file should never get committed to the repository
  - use python-dotenv to load the access  keys as env variables


# Step 2: Data Base Set Up
- raw csv files -> Dockerized PostgreSQL

## Notes: DB setup
[Postgres Basic Data Loading](https://www.crunchydata.com/blog/data-loading-in-postgres-for-newbies)
[Using Postgres COPY](https://www.compilenrun.com/docs/database/postgresql/postgresql-data-import-export/postgresql-copy-command/)

## Notes: Docker
[Basic Docker App](https://docs.docker.com/get-started/workshop/02_our_app/)
[PostgreSQL and Docker](https://simplebackups.com/blog/run-postgresql-on-docker)
[Another PostgreSQL Tut](https://dev.to/nhannguyenuri/setting-up-postgresql-in-docker-a-step-by-step-guide-3gc4)
[Pre Seed Docker Postgres](https://docs.docker.com/guides/pre-seeding/)
- Basic Parts
  - The Container
    -  isolated shell that holds dependencies to run application, similar to env
  - The Image
    - a pre configured package used to create a container: includes all the needed files, librares and cong ie PostgreSQL for databases
  - Volumes
    - Share files created or modified in container to the host
    - Allow files created in container to be saved to the host
    - Connect filesystem paths of the container to the host machine. allowing file changes to persist across containers
    - Volume mount: docker fully manages the volume, including storage location on disk. only need to remeber the name of the volume
  - Binds
    - Share files from the host to a container

## How to Persist a DB created in a container
  - containers can create, update and delete files but those changes are lost when you remove the container
  - Docker isolates all files changes to that container
  - So we use volumes which link a filesystem path of the container back to the host machine
  - if you mount a direcoty in the container, changes in that dir are seen on the host machine
  - if you mount that direcoty across container restars, you'd see the same files
  - Need to mount the location where Postgres saves it's database files to a volume in the host machine
  - create a volume and attach it to the direcoty where the data base files are store you can persist the data
  - We use a volume mount: define which file path in the contaier you want to persist, the name of the volume and docker does the rest
  - you don't really know WHERE docker has stored the volume on your disk but you don't need to
  - Need to know the file path the Postgre uses to store the db files

## How to connect to docker DB from python
  - Mapp the containers port to a localhost port?
  - PostgreSQL default port is 5432

## Application
- Use events data from NOAA to setup postgres data base in docker
- write a bash script to automate setting everything up and loading the data


# Mini Project 1
MVP: Pull data from web and store it in a dockerized PostgreSQL DB
- Setup Repo
- Python scripts to scrap csv files
- SQL scripts to create schema and load data
- write at least one test
- Python + SQL script to read data back into project
- tidy github repo

# Step ?: Model Deployment
[Basic Explainer on Real-Time, Batch and Edge](https://towardsdatascience.com/3-ways-to-deploy-machine-learning-models-in-production-cdba15b00e/)
[Basic Real Time Example](https://machinelearningmastery.com/a-practical-guide-to-deploying-machine-learning-models/)
## Notes Deployment
- two main types: Real-Time/On Demand, and Batch
  - Real-time/On Demand uses a server to take in new data and instantly produce a result
  - Batch takes in larger amounts of data at regular intervals ie for forecasting
-  Real-Time/On Demand
  - Use a server API packaged as a web app to take in new data and return the prediction
  1. Develop and train a model: scikit learn
  2. Save the trained model: Pickle
  3. Creat app to handle prediction requests: FastAPI, pydantic (for input validation)
  4. Create a container to hold and run the app in: Docker with custome image
      - Uvicorn to run the FastAPI app
  5. Build and run contrainer with your app image
