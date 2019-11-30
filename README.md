# anyway-backend


------
### Docker

There are 2 Dockerfiles in this project :
1) The PostgreSQL DB docker at the "db_docker" folder
2) The actual application docker at the "application_docker"



#### ReBuild & ReRun
If you change the docker files and want to re-run the docker-compose you need to:
`docker-compose build`
adn then:
`docker-compose up`


docker-postgis - Dockerfile, initdb-postgis.sh and update-postgis.sh where taken from here:
`https://github.com/appropriate/docker-postgis/tree/f6d28e4a1871b1f72e1c893ff103f10b6d7cb6e1/10-2.4`


