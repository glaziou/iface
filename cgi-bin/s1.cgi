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
my $power=$q->param("power");
my $alpha=$q->param("alpha");
my $c=$q->param("c");
my $onesided=$q->param("onesided");
my $p1=$q->param("p1");
my $p2=$q->param("p2");
my $onesample=$q->param("onesample");
my $n=$q->param("n");
my $numclus=$q->param("numclus");
my $obsclus=$q->param("obsclus");
my $rho=$q->param("rho");
my $cluster=$q->param("cluster");
my $err = 0;


## handles some data entry errors
if ($level < 0 or $level > 100) {$err++
} elsif ($p1 < 0 or $p1 > 100 or $p2 < 0 or $p2 > 100) {$err++
} elsif ($cluster and $numclus > 0 and $obsclus > 0) {$err++
}


if ($err) {print "ERROR: click on the -back- button and check the values";
} elsif ($numclus > 0 and $obsclus > 0) {print "ERROR: must choose number of clusters or number of observations per cluster, but not both";
} elsif ($n > 0 and !$onesample and !$onesided) {system("$prog", "-cp", "$p1", "$p2", "-alpha", "$alpha", "-c", "$c", "-n", "$n");
} elsif ($n > 0 and !$onesample and $onesided) {system("$prog", "-cp", "$p1", "$p2", "-alpha", "$alpha", "-c", "$c", "-onesided", "-n", "$n");
} elsif ($n > 0 and $onesample and !$onesided) {system("$prog", "-cp", "$p1", "$p2", "-alpha", "$alpha", "-c", "$c", "-onesample", "-n", "$n");
} elsif ($n > 0 and $onesample and $onesided) {system("$prog", "-cp", "$p1", "$p2", "-alpha", "$alpha", "-c", "$c", "-onesample", "-onesided", "-n", "$n");
} elsif (!$onesample and !$onesided and !$cluster) {system("$prog", "-cp", "$p1", "$p2", "-alpha", "$alpha", "-c", "$c", "-power", "$power");
} elsif (!$onesample and $onesided and !$cluster) {system("$prog", "-cp", "$p1", "$p2", "-alpha", "$alpha", "-c", "$c", "-power", "$power", "-onesided");
} elsif ($onesample and !$onesided and !$cluster) {system("$prog", "-cp", "$p1", "$p2", "-alpha", "$alpha", "-c", "$c", "-power", "$power", "-onesample");
} elsif ($onesample and $onesided and !$cluster) {system("$prog", "-cp", "$p1", "$p2", "-alpha", "$alpha", "-c", "$c", "-power", "$power", "-onesample", "-onesided");
} elsif (!$onesample and !$onesided and $cluster and $numclus > 0) {system("$prog", "-cp", "$p1", "$p2", "-alpha", "$alpha", "-c", "$c", "-power", "$power", "-rho", "$rho", "-numclus", "$numclus");
} elsif (!$onesample and $onesided and $cluster and $numclus > 0) {system("$prog", "-cp", "$p1", "$p2", "-alpha", "$alpha", "-c", "$c", "-power", "$power", "-onesided", "-rho", "$rho", "-numclus", "$numclus");
} elsif ($onesample and !$onesided and $cluster and $numclus > 0) {system("$prog", "-cp", "$p1", "$p2", "-alpha", "$alpha", "-c", "$c", "-power", "$power", "-onesample", "-rho", "$rho", "-numclus", "$numclus");
} elsif ($onesample and $onesided and $cluster and $numclus > 0) {system("$prog", "-cp", "$p1", "$p2", "-alpha", "$alpha", "-c", "$c", "-power", "$power", "-onesample", "-onesided", "-rho", "$rho", "-numclus", "$numclus");
} elsif (!$onesample and !$onesided and $cluster and $obsclus > 0) {system("$prog", "-cp", "$p1", "$p2", "-alpha", "$alpha", "-c", "$c", "-power", "$power", "-rho", "$rho", "-obsclus", "$obsclus");
} elsif (!$onesample and $onesided and $cluster and $obsclus > 0) {system("$prog", "-cp", "$p1", "$p2", "-alpha", "$alpha", "-c", "$c", "-power", "$power", "-onesided", "-rho", "$rho", "-obsclus", "$obsclus");
} elsif ($onesample and !$onesided and $cluster and $obsclus > 0) {system("$prog", "-cp", "$p1", "$p2", "-alpha", "$alpha", "-c", "$c", "-power", "$power", "-onesample", "-rho", "$rho", "-obsclus", "$obsclus");
} elsif ($onesample and $onesided and $cluster and $obsclus > 0) {system("$prog", "-cp", "$p1", "$p2", "-alpha", "$alpha", "-c", "$c", "-power", "$power", "-onesample", "-onesided", "-rho", "$rho", "-obsclus", "$obsclus");
} else {print "ERROR: click on the -back- button and check the values";}

print <<EndHTML2;
</pre>
<hr>
</body>
</html>
EndHTML2
