#!/bin/bash
set -e
set -u
CONFIG=${CONFIG:-'/root/scripts/digitemp/config-serial.conf'}
SERIALDEV=${SERIALDEV:-'/dev/ttyUSB0'}
STTY=/usr/bin/stty

if [ ! -c "${SERIALDEV}" ]; then
	echo "File '${SERIALDEV}' doesn't seem to be char device. Quitting."
	exit 1;
fi

if [ ! -e "${CONFIG}" ]; then
	echo "Config '${CONFIG}' doesn't seem to exist. Quitting."
	exit 1;
fi

if [ ! -x "${STTY}" ]; then
	echo "'${STTY}' doesn't exist nor executable."
	exit 1;
fi

for PARAM in $(cat "${CONFIG}" | sed -e 's# #_#g'); do
	 $STTY -F ${SERIALDEV} $(echo ${PARAM} | sed -e  's#_# #g');
done
