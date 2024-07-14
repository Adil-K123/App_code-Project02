#!/bin/bash

#create and provide necessory files and directories
mkdir -p monitoring_files/grafana_db && chmod 777 monitoring_files/grafana_db
chmod 777 monitoring_files/prometheus && chmod 777 monitoring_files/prometheus/prometheus.yml
                
#Deploy monitoring_stack
sudo docker stack deploy --with-registry-auth --detach=false -c monitoring_files/docker-compose.yaml monitoring_stack