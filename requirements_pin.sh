#!/bin/bash

set -euo pipefail

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" &> /dev/null && pwd )"

docker run \
	--entrypoint=bash \
	--rm \
	-v "$DIR/requirements.in":/requirements.in \
	-v "$DIR/requirements.txt":/requirements.txt \
	python -c "pip install pip-tools && python -m piptools compile --generate-hashes --no-header --output-file=- requirements.in > requirements.txt"
