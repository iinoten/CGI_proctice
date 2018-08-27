#!/usr/bin/perl

use strict;

my $time = time;
#多分これはグリニッジ標準時

print "Content-type:text/html\n\n";
print $time,"<br>\n";
print localtime($time),"<br>\n";
#「秒、分、時、日、月、年、曜日、経過日数(多分一年のうちの)、サマータイムなんちゃら」のやつが数字で表示される

exit;
