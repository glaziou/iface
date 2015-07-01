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

my $level=$q->param("level");
my $or=$q->param("or");
my $exp=$q->param("exp");
my $power=$q->param("power");
my $alpha=$q->param("alpha");
my $c=$q->param("c");
my $onesided=$q->param("onesided");
my $n=$q->param("n");
my $matched=$q->param("matched");
my $minimum=$q->param("minimum");
my $err = 0;


## handles some data entry errors
if ($level < 0 or $level > 100) {$err++
} elsif ($or < 0) {$err++
}


if ($err) {print "ERROR: click on the -back- button and check the values";
} elsif ($minimum and $or > 0) {print "ERROR: enter an odds-ratio or click the checkbox minimum OR, but not both";
} elsif ($minimum and $matched) {print "ERROR: matched option not supported with minimum OR computation";
} elsif ($minimum and $c>1) {print "minimum/maximum detectable odds-ratio only available with a ratio of cases/controls = 1";
} elsif ($n > 0 and $minimum and !$onesided) {system("$prog", "-n", "$n", "-exp", "$exp", "-c", "$c");
} elsif ($n > 0 and $minimum and $onesided) {system("$prog", "-n", "$n", "-exp", "$exp", "-c", "$c", "-onesided");
} elsif ($n > 0 and !$onesided and !$matched) {system("$prog", "-n", "$n", "-exp", "$exp", "-or", "$or", "-c", "$c");
} elsif ($n > 0 and $onesided and $matched) {system("$prog", "-n", "$n", "-exp", "$exp", "-or", "$or", "-c", "$c", "-onesided", "-matched");
} elsif ($n > 0 and !$onesided and $matched) {system("$prog", "-n", "$n", "-exp", "$exp", "-or", "$or", "-c", "$c", "-matched");
} elsif ($n > 0 and $onesided and !$matched) {system("$prog", "-n", "$n", "-exp", "$exp", "-or", "$or", "-c", "$c", "-onesided");
} elsif ($or > 0 and !$onesided and !$matched) {system("$prog", "-or", "$or", "-exp", "$exp", "-power", "$power", "-c", "$c");
} elsif ($or > 0 and $onesided and !$matched) {system("$prog", "-or", "$or", "-exp", "$exp", "-power", "$power", "-c", "$c", "-onesided");
} elsif ($or > 0 and !$onesided and $matched) {system("$prog", "-or", "$or", "-exp", "$exp", "-power", "$power", "-c", "$c", "-matched");
} elsif ($or > 0 and $onesided and $matched) {system("$prog", "-or", "$or", "-exp", "$exp", "-power", "$power", "-c", "$c", "-onesided", "-matched");
} else {print "ERROR: click on the -back- button and check the values";}


print <<EndHTML2;
</pre>
<hr>
</body>
</html>
EndHTML2
