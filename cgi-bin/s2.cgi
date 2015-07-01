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
my $m1=$q->param("m1");
my $m2=$q->param("m2");
my $sd1=$q->param("sd1");
my $sd2=$q->param("sd2");
my $onesample=$q->param("onesample");
my $n=$q->param("n");
my $matched=$q->param("matched");
my $numclus=$q->param("numclus");
my $obsclus=$q->param("obsclus");
my $rho=$q->param("rho");
my $cluster=$q->param("cluster");
my $err = 0;


## handles some data entry errors
if ($level < 0 or $level > 100) {$err++
} elsif ($cluster and $numclus > 0 and $obsclus > 0) {$err++
}


if ($err) {print "ERROR: click on the -back- button and check the values";
} elsif ($n > 0 and $sd1 > 0 and $onesided and !$onesample) {system("$prog", "-means", "$m1", "$m2", "$sd1", "$sd2", "-alpha", "$alpha", "-c", "$c", "-onesided", "-n", "$n");
} elsif ($n > 0 and $sd1 > 0 and !$onesided and $onesample) {system("$prog", "-means", "$m1", "$m2", "$sd1", "-alpha", "$alpha", "-c", "$c", "-onesample", "-n", "$n");
} elsif ($n > 0 and $sd1 > 0 and $onesided and $onesample) {system("$prog", "-means", "$m1", "$m2", "$sd1", "-alpha", "$alpha", "-c", "$c", "-onesample", "-onesided", "-n", "$n");
} elsif ($n > 0 and $sd1 > 0 and !$onesided and !$onesample and !$cluster) {system("$prog", "-means", "$m1", "$m2", "$sd1", "$sd2", "-alpha", "$alpha", "-c", "$c", "-n", "$n");} elsif ($sd1 > 0 and $onesided and !$onesample and !$cluster) {system("$prog", "-means", "$m1", "$m2", "$sd1", "$sd2", "-power", "$power", "-alpha", "$alpha", "-c", "$c", "-onesided");
} elsif ($sd1 > 0 and !$onesided and $onesample and !$cluster) {system("$prog", "-means", "$m1", "$m2", "$sd1", "-power", "$power", "-alpha", "$alpha", "-c", "$c", "-onesample");
} elsif ($sd1 > 0 and $onesided and $onesample and !$cluster) {system("$prog", "-means", "$m1", "$m2", "$sd1", "-power", "$power", "-alpha", "$alpha", "-c", "$c", "-onesample", "-onesided");
} elsif ($sd1 > 0 and !$onesided and !$onesample and !$cluster) {system("$prog", "-means", "$m1", "$m2", "$sd1", "$sd2", "-power", "$power", "-alpha", "$alpha", "-c", "$c");



} elsif ($sd1 > 0 and $onesided and !$onesample and $cluster and $numclus > 0) {system("$prog", "-means", "$m1", "$m2", "$sd1", "$sd2", "-power", "$power", "-alpha", "$alpha", "-c", "$c", "-onesided", "-rho", "$rho", "-numclus", "$numclus");
} elsif ($sd1 > 0 and !$onesided and $onesample and $cluster and $numclus > 0) {system("$prog", "-means", "$m1", "$m2", "$sd1", "-power", "$power", "-alpha", "$alpha", "-c", "$c", "-onesample", "-rho", "$rho", "-numclus", "$numclus");
} elsif ($sd1 > 0 and $onesided and $onesample and $cluster and $numclus > 0) {system("$prog", "-means", "$m1", "$m2", "$sd1", "-power", "$power", "-alpha", "$alpha", "-c", "$c", "-onesample", "-onesided", "-rho", "$rho", "-numclus", "$numclus");
} elsif ($sd1 > 0 and !$onesided and !$onesample and $cluster and $numclus > 0) {system("$prog", "-means", "$m1", "$m2", "$sd1", "$sd2", "-power", "$power", "-alpha", "$alpha", "-c", "$c", "-rho", "$rho", "-numclus", "$numclus");

} elsif ($sd1 > 0 and $onesided and !$onesample and $cluster and $obsclus > 0) {system("$prog", "-means", "$m1", "$m2", "$sd1", "$sd2", "-power", "$power", "-alpha", "$alpha", "-c", "$c", "-onesided", "-obsclus", "$obsclus");
} elsif ($sd1 > 0 and !$onesided and $onesample and $cluster and $obsclus > 0) {system("$prog", "-means", "$m1", "$m2", "$sd1", "-power", "$power", "-alpha", "$alpha", "-c", "$c", "-onesample", "-obsclus", "$obsclus");
} elsif ($sd1 > 0 and $onesided and $onesample and $cluster and $obsclus > 0) {system("$prog", "-means", "$m1", "$m2", "$sd1", "-power", "$power", "-alpha", "$alpha", "-c", "$c", "-onesample", "-onesided", "-obsclus", "$obsclus");
} elsif ($sd1 > 0 and !$onesided and !$onesample and $cluster and $obsclus > 0) {system("$prog", "-means", "$m1", "$m2", "$sd1", "$sd2", "-power", "$power", "-alpha", "$alpha", "-c", "$c", "-obsclus", "$obsclus");
} else {print "ERROR: click on the -back- button and check the values";}

print <<EndHTML2;
</pre>
<hr>
</body>
</html>
EndHTML2
