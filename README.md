# PROJECT_GROUP
PROJECT_GROUP
#ejecutar  docker-compose_mongo_container.yml ya teniendo creados los archivos rs-init.sh y init.js
docker-compose --file docker-compose_mongo_container.yml --project-name datawarehouse-mongodb-replic
#Ejecutar rs-init.sh dentro de mongo1
docker exec mongo1 sh /scripts/rs-init.sh
#ejecutar configserver-init.js
docker exec mongo1 sh -c "mongosh < /scripts/init.js"


![image](https://github.com/Amy-Sanchez/PROJECT_GROUP/assets/65546803/e237cfba-5b4d-4805-9f3b-a2144cbcb056)
