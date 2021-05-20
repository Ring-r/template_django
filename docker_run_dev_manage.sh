#!/bin/bash

set -euo pipefail

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
IMAGE_NAME=$( basename "$DIR")

docker run --rm --entrypoint="" -v $DIR/:/home/appuser/$IMAGE_NAME/ $IMAGE_NAME python template_django/manage.py $1
