create extension postgis;

COPY /dockerfile/postgres/init-scripts/ /docker-entrypoint-initdb.d/