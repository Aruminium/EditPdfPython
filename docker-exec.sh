#!/bin/bash
CONTAINER_ID=`docker ps -q`
if [ -n "$CONTAINER_ID" ]; then
  docker exec -it "$CONTAINER_ID" /bin/bash
else
  echo "Containerが起動されていません"
fi