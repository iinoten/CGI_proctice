#!/usr/bin/perl

use strict;

my $file = 'log.txt';
open(IN,"$file");
my @file = <IN>;
close(IN);

print "Content-type: text/html\n\n";
foreach (@file) {
print $_, "<br>\n";
}
exit;
