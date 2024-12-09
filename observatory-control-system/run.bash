#!/bin/bash
set -eu -o pipefail

[[ -f tls/client.cert.pem ]] || ( cd tls && ./make-certs.bash )

docker_compose=(docker compose -f docker-compose.yml)
docker_compose+=(-f docker-compose.dev.override.yml)

${docker_compose[@]} down
${docker_compose[@]} build
${docker_compose[@]} up

