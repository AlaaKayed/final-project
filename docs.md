# Bazar Store



## Overview

in this part of the project we are asked to build and rearchitecting ***Bazar online store*** we built in Lab 1 to handle a higher workload.

## System Design and Replication
- - -
We created two replicas of the ***catalog server*** and two replicas of the ***order server***, and one replica for the ***front-end server*** and one replica for the ***cache server (memcached server)*** as shown in the image below : 

![alt text](https://i.ibb.co/m41vpNG/bazar-store.png "Title")

every replica is running in a diffrent docker container and communicate with each other using REST API calls.

#####Note : Docker images is uploaded to Docker Hub and we can access them using the following links : 

[Catalog Primary Server](https://hub.docker.com/repository/docker/95367920/bazar-catalog-primary-server )

[Catalog Normal Server](https://hub.docker.com/repository/docker/95367920/bazar-catalog-normal-server)

[Order Server](https://hub.docker.com/repository/docker/95367920/bazar-order-server)

[Front-end Server](https://hub.docker.com/repository/docker/95367920/bazar-front-end-server)

and we can download ***memcached server*** docker image using the following link :

[Memcached Server ](https://hub.docker.com/_/memcached)


## How to Run
- - -
1. **Catalog Primary Server:**
> sudo docker run --rm --name  catalog-instance1 --network bazar-store-network -d -it 95367920/bazar-catalog-primary-server

2. **Catalog Normal Server:**
> sudo docker run --rm --name  catalog-instance2 --network bazar-store-network -d -it 95367920/bazar-catalog-normal-server

3. **Order server**:
> sudo docker run --rm --name  order-instance1 --network bazar-store-network -d -it 95367920/bazar-order-server

4. **Front-end Server:**
> sudo docker run --publish 4200:4200 --rm --name  fcache --network bazar-store-network -d -it 95367920/bazar-front-end-server

5. **Memcached server:**
> sudo docker run --publish 11211:11211 --network bazar-store-network --name my-memcache memcached


## Consistancy 
- - -
to ensure the consistancy across replicas we use internal protocol ***(Remote-Write Protocol)*** and we considered the ***catalog-instance1 as a primary server*** and other replicas such as ***catalog-instance2 as a normal server*** , so if any write requests comes to catalog-instance2 it forwards it to the primary server
and the primary server tell other replicas to update their data, but if the write request comes to catalog-instance1 which is the primary server it updated the data on its database and then tell other replicas to update their data.

## Cache Consistancy
---
we ensure cache consistancy by using **Push Approach**, when any write request occurs we check if the value we written in is cached or not , if the value is cached send invalidate request to the Memcached server to remove it from the cache. 


## Load Balancing

for the load balancing in the front-end server we used Round Robin approach , and because all the servers have the same capabilites we balanced the requests to 50% for each server.


## Performance Measurements
