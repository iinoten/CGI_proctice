#!/usr/bin/perl

# 掲示板 その１

require "cgi-lib.pl";

print "Content-type: text/html; charset=Shift_JIS\n\n";

# フォーム部分を表示する
print <<EOL;
<html>
<body>
<h2>一行掲示板</h2>
<form method="post" action="bbs1.cgi">
メッセージ：<input type="text" name="message" size="60">
<input type="submit" value="送信">
</form>
<hr>
EOL

&ReadParse(*form);

# フォームの値を取得
$message = $form{"message"};

# ログファイル読み込み
open(IN, "bbs1.txt");
@log = <IN>;
close(IN);

# メッセージが入力されているときは書き込み処理を行なう
if ($message ne "") {
  # ログ先頭にメッセージを格納
  unshift @log, "$message\n";

  # ログファイルに書き込み
  open(OUT, "> bbs1.txt");
  print OUT @log;
  close(OUT);
}

# ログ表示
foreach $data (@log) {
  chop $data;
  print "$data<br>\n";
}

print "</body>\n</html>\n";
