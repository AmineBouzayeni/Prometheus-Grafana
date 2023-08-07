#!/bin/bash

datasource_id=$(curl -u admin:__ADMIN_PASSWORD__ http://__GRAFANA_IP__:__GRAFANA_PORT__/api/datasources/id/:__DS_NAME__)
datasource_id=$(echo $datasource | jq .uid | sed 's/"//g')
echo $datasource_id