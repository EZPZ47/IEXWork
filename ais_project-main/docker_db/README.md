# AIS
Dockerized pre-configured PostGIS database with AIS data from Danish Maritime Authority downloaded here: https://web.ais.dk/aisdata/


## Getting started

Install Docker Desktop locally

To deploy container:
```
docker-compose up -d
```
## pgAdmin
pgAdmin should be running now at http://localhost:5050/browser/
pg Admin login info:
- admin@admin.com
- supersecret

## PostGIS database login:
PostGIS should be running now at http://localhost:5432
- aisuser
- aispass

## Table:
Servers/ais_project/Databases/mydatabase/Schemas/public/Tables/ais_raw

(Disregard other tables, they are for PostGIS extension)
