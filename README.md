# PROJECT_GROUP

¿Qué es fragmentación?
Sharding es un método para distribuir datos entre varias máquinas. MongoDB usa fragmentación para admitir implementaciones con conjuntos de datos muy grandes y operaciones de alto rendimiento.

Los sistemas de bases de datos con grandes conjuntos de datos o aplicaciones de alto rendimiento pueden desafiar la capacidad de un solo servidor. Por ejemplo, las altas tasas de consultas pueden agotar la capacidad de la CPU del servidor. Los tamaños de conjuntos de trabajo más grandes que la RAM del sistema hacen hincapié en la capacidad de E/S de las unidades de disco.

Hay dos métodos para abordar el crecimiento del sistema: escalado vertical y horizontal. MongoDB admite el escalado horizontal a través de Sharding.

Clúster fragmentado
Un clúster fragmentado de MongoDB consta de los siguientes componentes:

fragmento: cada fragmento contiene un subconjunto de los datos fragmentados. Cada fragmento se puede implementar como un conjunto de réplicas.
mongos: los mongos actúan como un enrutador de consultas, proporcionando una interfaz entre las aplicaciones cliente y el clúster fragmentado.
Servidores de configuración: los servidores de configuración almacenan metadatos y ajustes de configuración para el clúster.

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

Cómo utilizar
El proceso de configuración del espacio de trabajo de desarrollo es más simple que nunca con los siguientes pasos:

Install python3.
Install Docker for Desktop.
Clone este proyecto en su máquina local.
Abra la terminal y asegúrese de estar en el directorio raíz de este proyecto, ejecute el comando docker-compose up (esto hará que MongoDB Sharded Cluster funcione automáticamente). Eso es todo.
Ejecutar la aplicación

![image](https://github.com/Amy-Sanchez/PROJECT_GROUP/assets/65546803/97354d37-4002-422a-8602-3899461318d2)
