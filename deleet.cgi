#!/usr/bin/perl

use strict;

my $file = './log.txt';
#$fileにカレントディレクトリのlog.txtを指定
unlink $file;
#unlink関数でlog.txtを消去

print "Content-type:text/html\n\n";
print "delete,OK";

exit;
