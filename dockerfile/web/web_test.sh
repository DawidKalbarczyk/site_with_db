#!/bin/sh
set -eu

envsubst '${WEB_TEST} ${ENV_NAME}' < /usr/share/nginx/html/index.html.template \
    > /usr/share/nginx/html/index.html

exec nginx -g 'daemon off;'