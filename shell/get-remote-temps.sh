#!/bin/bash
# 2010/Nov/12 @ Zdenek Styblik
set -e
set -u

SERVER=${1:-''}
TMPDIR='/mnt/tmp/temperatures/'

if [ -z "${SERVER}" ]; then
	echo "Huh? I don't know where to download from"
	exit 255
fi

if [ ! -d "${TMPDIR}" ]; then
	mkdir "${TMPDIR}"
	chown apache "${TMPDIR}"
fi

wget --quiet "http://${SERVER}/cgi-bin/thermometer/thermometer-last.cgi" \
-O "${TMPDIR}/${SERVER}.htm" > /dev/null || \
{
	echo '<li><strong>Chyba:</strong> -254 &#176;C</li>' > "${TMPDIR}/${SERVER}.htm"
}

chown apache "${TMPDIR}/${SERVER}.htm"

