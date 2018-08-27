#!/usr/bin/perl

use strict;

my $string = 'Perl/CGI';
my $ref_string = \$string;

print "Content-type:text/html\n\n";
print ${ref_string};
exit;
