export DOCKER_NETWORK=docker-network
export DEV_HOME=$(pwd)
docker-compose -f docker-compose.tango_gui.yaml down --remove-orphans
docker-compose -f docker-compose.tangobase.yaml down --remove-orphans
docker stop dev
docker network remove docker-network