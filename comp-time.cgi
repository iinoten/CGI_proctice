#!/usr/bin/perl

use strict;

my $time = time;
my @localtime = localtime($time);

print "Content-type:text/html\n\n";
print $time,"<br>\n";

for (my $i= 0;$i<=$#localtime;$i++){  #$#で配列内の最大の添字を取得できる
    print $i," : ",$localtime[$i], "<br>\n";
  }

exit;
