#!/bin/sh

set -e

envsubst </etc/nginx/default.conf.tpl >/etc/nginx/conf.d/default.conf # Substituting ${} syntax with env variables
nginx -g 'daemon off;'                                                # Nginx stays in the foreground: one container = one process
