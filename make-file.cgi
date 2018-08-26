#!/usr/bin/perl

use strict;

my $file = './atarasi.txt';
#カレントディレクトリに存在しないファイル名を指定
open (OUT,">$file");
#上書きでopen
print OUT "NG";
#atarasi.txtに上書き（もとの文は消える）
close (OUT);

print "Content-type: text/html\n\n";
print "OK";
exit;

