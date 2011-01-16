====== Digitemp - init, RRD logging, graphing ======
Inspiration: http://martybugs.net/electronics/tempsensor/

Reason for all of this is digitemp and USB-RS232 somehow doesn't work without
init first. Thus this might get useful to somebody, or not. I've also rewritten
Marty's grapher. I don't remember, but there were some things I didn't like or
didn't go with using strict in Perl.

It also supports remote temp query, so you can place temperatures from remote
servers at your eg. homepage.

===== Files =====
.:
README.TXT ~ this readme
cgi-bin/ ~ CGI scripts
shell/ ~ shell scripts

./cgi-bin:
thermometer-last.cgi* ~ returns value of the last measured temperature
thermometer.cgi* ~ prints out graphs; day, week, month, year

./shell:
.digitemprc ~ digitemp config
config-serial.conf ~ serial interface parameters
config-serial.sh* ~ sets up serial interface
get_remote_temps.sh* ~ gets the last measured temperature from remote server
rrd-log-temp.sh* ~ logs temperature from sensor into RRD file
