#!/usr/bin/perl --

# フォームの内容を表示する

require "cgi-lib.pl";    # cgi-libを使用する

print "Content-type: text/html; charset=Shift_JIS\n\n";

&ReadParse(*form);

print <<EOL;
<html>
<body>
<p>
コンニチハ、 $form{"namae"} サン。
</p>
</body>
</html>
EOL
