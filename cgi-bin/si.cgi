#!/usr/bin/perl -w
#
#
# sampsize cgi interface
# Version 0.0.4
# 
# Copyright (C) Philippe Glaziou 	<glaziou@pasteur-kh.org>

$ENV{'PATH'} = '/home/groups/s/sa/sampsize/bin:/bin:/usr/bin:/usr/local/bin';

use CGI;
use strict;

my $q = new CGI;
my $prog = "sampsize";

print "Content-type:text/html\n\n";

print <<EndHTML;
<html><head><title>Sampsize results</title></head>
<body>
<h2>Sample size results</h2>
<pre>
EndHTML

my $s=$q->param("s");
my $pr=$q->param("pr");
my $pop=$q->param("pop");
my $level=$q->param("level");
my $nob=$q->param("nob");
my $power=$q->param("power");
my $alpha=$q->param("alpha");
my $onesided=$q->param("onesided");
my $bi1=$q->param("bi1");
my $bi2=$q->param("bi2");
my $onesample=$q->param("onesample");
my $err = 0;


# handles some data entry errors
if ($s < 0 or $level < 0 or $level > 100 or $pop < 0 or $pr < 0) {$err++;
}


if ($err) {print "ERROR: click on the -back- button and check the values";
} elsif ($s > 0) {system("$prog", "-e", "$s", "-pr", "$pr", "-pop", "$pop", "-level", "$level");
} elsif ($nob > 0) {system("$prog", "-nob", "$nob", "-pr", "$pr", "-level", "$level");
} elsif ($bi1 > 0) {system("$prog", "-bi", "$bi1", "$bi2", "-level", "$level");
} else {print "ERROR: click on the -back- button and check the values";}

print <<EndHTML2;
</pre>
<hr>
</body>
</html>
EndHTML2
