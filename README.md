# Digitemp - init, RRD logging, graphing

Inspiration: http://martybugs.net/electronics/tempsensor/

Reason for all of this is digitemp and USB-RS232 somehow don't work without
init first. Therefore, this might be useful to somebody, or not. I've also
rewritten Marty's grapher. I don't remember why, but either there were some
things I didn't like or just didn't work with ``use strict`` in Perl.

CGI also supports remote query for temp, therefore you can embed temperatures
from remote servers at your website or wherever.

## Directory structure

```
|
|-README.md - this readme
|-cgi-bin/ - CGI scripts
`shell/ - shell scripts
```
