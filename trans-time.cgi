#!/usr/bin/perl

use strict;

my $time = time;
my $localtime = localtime($time);
#これでローカルの時間に変換するみたい
#一度変数に入れる

print "Content-type:text/html\n\n";
print $time,"<br>\n";
print $localtime,"<br>\n";
#「Mon Aug 27 13:38:32 2018」って表示された

exit;
