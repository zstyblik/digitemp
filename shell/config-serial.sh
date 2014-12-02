#!/bin/bash
# Desc: Setup given serial device according to params specified in given config
set -e
set -u

SERIALDEV=${1:-''}
CONFIG=${2:-''}
if [ -z "${SERIALDEV}" ] || [ -z "${CONFIG}" ]; then
	printf -- "Usage: %s <serial_dev> <serial_config>" "${0}" 1>&2
	exit 1
fi

IFS='
'
for PARAM in $(cat -- "${CONFIG}"); do
	/usr/bin/stty -F "${SERIALDEV}" ${PARAM}
done
