# anyway-backend


------

# ANYWAY’s docker environment
-----------------------

Read more about DOCKER at [Offical docs](https://docs.docker.com/) or at [Github project](https://github.com/docker/docker)

There are 2 Dockerfiles in this project :
1) The PostgreSQL DB docker at the "db_docker" folder
2) The actual backend application docker is the Dockerfile


#### ReBuild & ReRun
If you change the docker files and want to re-run the docker-compose you need to:

`docker-compose build` and then: `docker-compose up`


docker-postgis - Dockerfile, initdb-postgis.sh and update-postgis.sh where inspired from here:
`https://github.com/appropriate/docker-postgis/tree/f6d28e4a1871b1f72e1c893ff103f10b6d7cb6e1/10-2.4`
