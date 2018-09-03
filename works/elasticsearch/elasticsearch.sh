#!/bin/bash

check_non_empty() {
  # $1 is the content of the variable in quotes e.g. "$FROM_EMAIL"
  # $2 is the error message
  if [[ "$1" == "" ]]; then
    echo "ERROR: specify $2"
    exit -1
  fi
}

check_exec_success() {
  # $1 is the content of the variable in quotes e.g. "$FROM_EMAIL"
  # $2 is the error message
  if [[ "$1" != "0" ]]; then
    echo "ERROR: $2 failed"
    echo "$3"
    exit -1
  fi
}

CurDir="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# get host ip
HostIP="$(ip route get 1 | awk '{print $NF;exit}')"

# set data dir
ESData=/data/elasticsearch/data
ESLog=/data/elasticsearch/logs

update_images() {
  # pull elasticsearch docker image
  docker pull docker.elastic.co/elasticsearch/elasticsearch:5.0.2

  check_exec_success "$?" "pulling 'elasticsearch' image"
}

start() {

  update_images

  docker kill elasticsearch 2>/dev/null
  docker rm -v elasticsearch 2>/dev/null
#     -v ${ESData}:/usr/share/elasticsearch/data \
#     -v ${ESLog}:/usr/share/elasticsearch/logs \

  docker run -d --name elasticsearch \
    -p 9200:9200 \
    -e "http.host=0.0.0.0" \
    -e "transport.host=127.0.0.1" \
    docker.elastic.co/elasticsearch/elasticsearch:5.0.2

  check_exec_success "$?" "start elasticsearch container"

  curl -XPOST http://${HostIP}:8500/v1/agent/service/register -d "{
      \"Name\": \"elasticsearch\",
      \"Port\": 9200,
      \"Check\": {\"HTTP\": \"http://${HostIP}:9200\", \"Interval\": \"30s\"}
    }"

}

stop() {
  curl http://${HostIP}:8500/v1/agent/service/deregister/elasticsearch
  docker stop elasticsearch 2>/dev/null
  docker rm -v elasticsearch 2>/dev/null
}

destroy() {
  stop
  rm -rf ${ESData}
  rm -rf ${ESLog}
}


##################
# Start of script
##################

case "$1" in
  start) start ;;
  stop) stop ;;
  restart)
    stop
    start
    ;;
  destroy) destroy ;;
  *)
    echo "Usage:"
    echo "./elasticsearch.sh start|stop|restart"
    echo "./elasticsearch.sh destroy"
    exit 1
    ;;
esac

exit 0
