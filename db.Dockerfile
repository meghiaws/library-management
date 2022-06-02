FROM postgres:13.7
COPY db_init.sql /docker-entrypoint-initdb.d/