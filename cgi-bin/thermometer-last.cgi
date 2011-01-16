#!/bin/sh
set -e
set -u

echo "Content-type: text/plain; charset=utf-8"
echo

RRDFILE='/var/lib/temperatures/temp_0.rrd'
LOCATION='Výšinka'

if [ ! -e "${RRDFILE}" ]; then
	echo "<li><strong>${LOCATION}:</strong> -255 &#176;C</li>"
	exit 1
fi

RRDOUT=$(/usr/bin/rrdtool lastupdate "${RRDFILE}" | \
tr '\n' ':' | tr -s ':' | tr -d ' ')

#TIMEUNIX=$(echo "${RRDOUT}" | cut -d ':' -f 2)
#TIMELAST=$(echo "${TIMEUNIX}" | awk '{ print strftime("%c", $1) }')
TEMP=$(echo "${RRDOUT}" | cut -d ':' -f 3)

echo "<li><strong>${LOCATION}:</strong> ${TEMP} &#176;C</li>"

