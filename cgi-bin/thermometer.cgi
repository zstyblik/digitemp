#!/usr/bin/perl -w -T
# 2010/Nov/12 @ Zdenek Styblik
# 
# Inspiration: 
# ---
# http://martybugs.net/electronics/tempsensor/

use strict;
use warnings;

use RRDs;

# define location of rrdtool databases
my $rrd = '/var/lib/temperatures/';
# define location of images
my $img = '/var/mrtg/temperatures/';

my $lastUnix = 0;

sub CreateGraph
{
	my $ERROR;
# creates graph
# inputs: $_[0]: n/a
#         $_[1]: interval (ie, day, week, month, year)
#         $_[2]: graph description
#		"DEF:temp1=$rrd/temp1.rrd:temp:AVERAGE",
#		"DEF:temp2=$rrd/temp2.rrd:temp:AVERAGE",
# 
#		"LINE2:temp1#990000:sensor 2\\:         ",
#		"GPRINT:temp1:MIN:    Min\\: %5.2lf",
#		"GPRINT:temp1:MAX:   Max\\: %5.2lf",
#		"GPRINT:temp1:AVERAGE:   Average\\: %5.2lf",
#		"GPRINT:temp1:LAST:   Current\\: %5.2lf degrees Celsius\\n",
#		"LINE2:temp2#00FF00:sensor 3\\:         ",
#		"GPRINT:temp2:MIN:    Min\\: %5.2lf",
#		"GPRINT:temp2:MAX:   Max\\: %5.2lf",
#		"GPRINT:temp2:AVERAGE:   Average\\: %5.2lf",
#		"GPRINT:temp2:LAST:   Current\\: %5.2lf degrees Celsius\\n";

	$lastUnix = RRDs::last "$rrd/temp_0.rrd";

	RRDs::graph "$img/temp_$_[1].png",
		"-s -1$_[1]",
		"-t DS18S20 temperature sensor :: last $_[1] (1 minute samples)",
		"--lazy",
		"-h", "200", "-w", "800",
		"-l", "0",
		"-a", "PNG",
		"-v degrees Celsius",
		"--slope-mode",
		"--color", "SHADEA#eeeeee",
		"--color", "SHADEB#eeeeee",
		"--color", "BACK#ffffff",
		"--color", "CANVAS#ffffff",
		"DEF:temp0=$rrd/temp_0.rrd:temp:AVERAGE",
		"LINE2:temp0#33CC00:sensor 1\\:         ",
		"GPRINT:temp0:MIN:    Min\\: %5.2lf",
		"GPRINT:temp0:MAX:   Max\\: %5.2lf",
		"GPRINT:temp0:AVERAGE:   Average\\: %5.2lf",
		"GPRINT:temp0:LAST:   Current\\: %5.2lf degrees Celsius\\n";
	if ($ERROR = RRDs::error) { 
		#print "$0: unable to generate sensor $_[0] $_[1] graph: $ERROR\n"; 
		#printf("Unable to generate sensor graph. Error: '%s'\n", $ERROR);
		return 1;
	}
	return 0;
}

print "Content-type: text/html; charset=utf-8\n\n";

&CreateGraph($_[0], "day", $_[1]);
&CreateGraph($_[0], "week", $_[1]);
&CreateGraph($_[0], "month", $_[1]);
&CreateGraph($_[0], "year", $_[1]);

my $lastTime = localtime($lastUnix);

print << "HTML";
<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.01//EN"
"http://www.w3.org/TR/html4/strict.dtd">
<html>
	<head>
		<meta name="description" content="Temperature measurements using 1-wire sensors">
		<meta name="keywords" content="1-wire,temperature,sensor,thermometer">
		<meta name="author" content="multiple authors">
		<meta http-equiv="Content-Type" content="text/html;charset=UTF-8">
		<meta http-equiv="refresh" content="300">
		<title>DS18S20 temperature sensors</title>
		<style type="text/stylesheet">
			div {
				margin-left: 20px;
			}
			#footer {
				font-size: small;
			}
		</style>
	</head>
	<body>
		<h1>DS18S20 temperature sensor(s)</h1>
		<p>
			<strong>Last update:</strong> $lastTime
		</p>
		<hr>
		<h2>Daily</h2>
		<div>
			<img src="temp_day.png" alt="Temps daily">
		</div>
		<hr>
		<h2>Weekly</h2>
		<div>
			<img src="temp_week.png" alt="Temps weekly">
		</div>
		<hr>
		<h2>Monthly</h2>
		<div>
			<img src="temp_month.png" alt="Temps monthly">
		</div>
		<hr>
		<h2>Yearly</h2>
		<div>
			<img src="temp_year.png" alt="Temps yearly">
		</div>
		<hr>
		<h6>Inspiration</h6>
		<div id="footer">
			<a href="http://martybugs.net/electronics/tempsensor/" title="tempsensor">
				Martin Pot's tempsensor
			</a>
		</div>
	</body>
</html>
HTML
