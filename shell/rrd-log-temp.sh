#!/bin/bash
# 2010/Nov/11 @ Zdenek Styblik
# Inspiration: http://martybugs.net/electronics/tempsensor/
#
set -e
set -u

DIGITEMP=/opt/digitemp-3.6.0/digitemp_DS9097
DIGITEMPCONF=/etc/digitemp.conf
RRDTOOL=/usr/bin/rrdtool

SENSOR=${1:-''}
RRDFILESDIR=/var/lib/temperatures/
RRDFILE="${RRDFILESDIR}/temp_${SENSOR}.rrd"

function help()
{
	echo "Log temperatures into RRD file."
	echo "Use: ${0} <sensor No.>"
	return 0
}

if [ ! -x "${RRDTOOL}" ]; then
	echo "RRDtool is required!"
	exit 3;
fi

if [ ! -x "${DIGITEMP}" ]; then
	echo "Digitemp is required!"
	exit 3;
fi

# TODO - only [0-9] is acceptable
if [ -z "${SENSOR}" ]; then
	help
	exit 2;
fi

if [ ! -e "${RRDFILE}" ]; then
	echo "File '${RRDFILE}' doesn't exist yet."
	echo -n "Trying to create..."
	$RRDTOOL create "${RRDFILE}" \
		-s 60 \
		DS:temp:GAUGE:240:U:U \
		RRA:AVERAGE:0.5:1:2016 \
		RRA:AVERAGE:0.5:6:1344 \
		RRA:AVERAGE:0.5:24:2190 \
		RRA:AVERAGE:0.5:144:3650
	echo "done."
fi

TEMP=$($DIGITEMP -t ${1} -q -c ${DIGITEMPCONF} -o "%.2C")
TEMPTEST=$(printf "%.0f" "${TEMP}")

if [ ${TEMPTEST} -eq 85 ]; then
	echo "Failed to read value from sensor."
	exit 1;
fi

$RRDTOOL update "${RRDFILE}" \
	-- "N:${TEMP}"
