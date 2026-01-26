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
- The exact location of files matters less than the motivation for grouping similar files
- For a Project called "My_Project" the structure could be:
  - My_Project
    - my_project(aka src): all the main .py files are stored
    - data: all the data files .csv .xlsx, subdir for raw and processed
    - db: sql scripts to create and load db. schema.sql, load_data.sql
    - tests: all .py files to run tests
    - notebooks: juypter notebooks
    - docs:
    - ReadMe.md, LICENSE, gitignore  


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

