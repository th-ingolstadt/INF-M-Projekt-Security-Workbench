#!/bin/bash

CONTAINER_NAME=arpcontainer
IMAGE_NAME=arpimage
PATH_TO_DOCKERFILE=$(dirname $(realpath "$0"))
DOCKER_FILE_NAME_RASPBERRY=Dockerfile_Raspberry_Pi
DOCKER_FILE_NAME_x86=Dockerfile_x86
WEB_SERVER_DST_PATH=/var/www/html/


# ussge function
function usage {
	echo "usage: $0 [start|stop|status]"
	echo "env: ARP_WEB_RES_PATH has to be set and point to the location of the web application resources. This directory will be copied to the root folder of the web server."
	exit 1
}

# Check if environment variable ARP_WEB_RES_PATH is set
if [ -z "$ARP_WEB_RES_PATH" ]; then
	echo "Environment variable ARP_WEB_RES_PATH not set!"
	usage
	exit 1
else
	if [ -d "$ARP_WEB_RES_PATH" ]; then
		ARP_WEB_RES_ABSOLUTE_PATH=$(realpath $ARP_WEB_RES_PATH)
		status=$?
		if [ $status -ne 0 ]; then
			echo "Absolute path to environment variable value ARP_WEB_RES_PATH=$WEB_RES_PATH could not be created!"
			exit 1
		fi
	else
		echo "The path of the environment variable ARP_WEB_RES_PATH=$ARP_WEB_RES_PATH could not be found!"
		exit 1
	fi
fi

# One argument has to be supplied
if [ $# -ne 1 ]; then
	echo "There has to be exacatly one argument!"
	usage
	exit 1
fi

# Check architecture then choose the right Dockerfile
architecture=$(uname -m)
if [ "$architecture" == "x86_64" ] || [ "$architecture" ==  "i686" ]; then
	DOCKER_FILE_NAME=$DOCKER_FILE_NAME_x86
elif [ "$architecture" == "armv7l" ]; then
	DOCKER_FILE_NAME=$DOCKER_FILE_NAME_RASPBERRY
else
	echo "Architecture not recognized!"
	echo "No Dockerfile for this architecture available!"
	exit 1
fi

# Check if the image exists
image_exists="$(docker images | grep $IMAGE_NAME)"

if [ -z "$image_exists" ]; then
	echo "The image $IMAGE_NAME will be created"
	echo "This will take some time..."
	docker build -t $IMAGE_NAME -f $PATH_TO_DOCKERFILE/$DOCKER_FILE_NAME $PATH_TO_DOCKERFILE
	build_status=$?

	if [ $build_status -ne 0 ]; then
		echo "Build of image $IMAGE_NAME failed!"
		echo "Please check the Dockerfile $DOCKER_FILE_NAME in the directory $PATH_TO_DOCKERFILE"
		exit 1
	else
		echo "Docker image $IMAGE_NAME successfully created."
	fi
fi

# Check if the container exists
container_exists="$(docker ps -aq -f name=$CONTAINER_NAME)"

if [ ! -z "$container_exists" ]; then
	# Check if container is already running, "true" or "false" will be stored in the variable
	is_running="$(docker inspect -f {{.State.Running}} $CONTAINER_NAME)"
else
	is_running="false"
fi

if [ "$1" == "start" ]; then
	# remove existing container
	if [ ! -z "$container_exists" ]; then
		# stop if container is running
		if [ "$is_running" == "true" ]; then
			echo "Stopping running container $CONTAINER_NAME ..."
			docker stop $CONTAINER_NAME
			echo "Stopped $CONTAINER_NAME"
		fi
		# remove container
		echo "Removing existing container $CONTAINER_NAME ..."
		docker rm $CONTAINER_NAME
		echo "Removed $CONTAINER_NAME"
	fi
	
	echo "Starting apache docker container ..."
	
	docker run \
		-v $ARP_WEB_RES_ABSOLUTE_PATH:$WEB_SERVER_DST_PATH \
		-p 80:80 \
		--name $CONTAINER_NAME \
		-d $IMAGE_NAME
	status=$?

	if [ $status -ne 0 ]; then
		echo "Error: Could not start docker container: $status"
		echo "Check if the image $IMAGE_NAME exists"
		exit 1
	fi
	
	echo "... apache docker container started successfully."

elif [ "$1" == "stop" ]; then
	if [ ! -z "$container_exists" ]; then
		echo "Stopping container $CONTAINER_NAME ..."
		docker stop $CONTAINER_NAME
	fi

	echo "Container $CONTAINER_NAME is stopped."

elif [ "$1" == "status" ]; then
	container_status="unknown"
	if [ "$is_running" == "true" ]; then
		container_status="running"
	else
		container_status="stopped"
	fi
	
	echo "Status of the docker container $CONTAINER_NAME: $container_status"

else
	usage
	exit 1
fi	

