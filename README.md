# PROJECT_GROUP

El sistema invocará un clúster compuesto por:

3 nodos de fragmentación (mongorshard1node1, mongorshard1node2, mongorshard1node3)
3 nodos de configuración (mongoConfNode1, mongoConfNode2, mongoConfNode3)
2 nodos Mongos (mongosNode1, mongosNode2)
Los contenedores almacenarán datos relevantes (como bases de datos) en la carpeta raíz del host. En detalle:

Sharding notado almacenará datos en:
./mongoData/fragmento1/nodo1
./mongoData/fragmento1/nodo2
./mongoData/fragmento1/nodo3
Los nodos de configuración almacenarán datos en:
./mongoData/shard1/config1
./mongoData/shard1/config2
./mongoData/shard1/config3

PROJECT_GROUP
#ejecutar  docker-compose_mongo_container.yml ya teniendo creados los archivos rs-init.sh y init.js

docker-compose --file docker-compose_mongo_container.yml --project-name datawarehouse-mongodb-replic

#Ejecutar rs-init.sh dentro de mongo1

docker exec mongo1 sh /scripts/rs-init.sh

#ejecutar configserver-init.js

docker exec mongo1 sh -c "mongosh < /scripts/init.js"


![image](https://github.com/Amy-Sanchez/PROJECT_GROUP/assets/65546803/e237cfba-5b4d-4805-9f3b-a2144cbcb056)



![image](https://github.com/Amy-Sanchez/PROJECT_GROUP/assets/65546803/97354d37-4002-422a-8602-3899461318d2)
