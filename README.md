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

# Mini Project 1
MVP: Pull data from web and store it in a dockerized PostgreSQL DB
- Setup Repo
- Python scripts to scrap csv files
- SQL scripts to create schema and load data
- write at least one test
- Python + SQL script to read data back into project
- tidy github repo

