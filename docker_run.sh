#!/bin/bash

set -euo pipefail

DIR=$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )
IMAGE_NAME=$( basename "$DIR")

docker run --rm --network="host" $IMAGE_NAME
