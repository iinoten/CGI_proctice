#!/usr/bin/perl

# 掲示板 その２

require "cgi-lib.pl";

print "Content-type: text/html; charset=Shift_JIS\n\n";

# フォーム部分を表示する
print <<EOL;
<html>
<body>
<h2>一行掲示板</h2>
<form method="post" action="bbs2.cgi">
名前：<input type="text" name="namae" size="20">&nbsp;
メッセージ：<input type="text" name="message" size="60">
<input type="submit" value="送信">
</form>
<hr>
EOL

&ReadParse(*form);

# フォームの値を取得
$namae = $form{"namae"};
$message = $form{"message"};

# ログファイル読み込み
open(IN, "bbs2.txt");
@log = <IN>;
close(IN);

# メッセージが入力されているときは書き込み処理を行なう
if ($message ne "") {
  # タグの無効化
  $namae =~ s/</&lt;/g;
  $namae =~ s/>/&gt;/g;
  $message =~ s/</&lt;/g;
  $message =~ s/>/&gt;/g;
#フォームから送られてきたタグの<と>を右のに変える

  # ログ先頭に名前とメッセージを格納
  unshift @log, "$namae\t$message\n";

  # ログファイルにロックをかけて書き込み
  open(OUT, "+< bbs2.txt"); #+<で読み書きどちらものモードでオープンできる
  flock(OUT, 2);  #ファイルロック
  truncate(OUT, 0);
  seek(OUT, 0, 0);
#ファイルのサイズを０にする？？？？？？？？？？？ロックするときに必要な工程らしい
  print OUT @log;
  close(OUT);
}

# ログ表示
foreach $data (@log) {
  chop $data;
  ($namae, $message) = split(/\t/, $data);
  print "[$namae] $message<br>\n";
}

print "</body>\n</html>\n";
