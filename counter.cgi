#!/usr/bin/perl
# アクセスカウンタ

print "Content-type: text/html; charset=Shift_JIS\n\n";

# カウントファイルから読み込み
open(IN, "counter.txt");
#大文字のINはファイルハンソル、なんでもいい。INにcounter.txtすべてを収納
$count = <IN>;
#変数$countにファイルハンドルINを収納
close(IN);  #openしたあとは閉じなければいけない
#closeしたあとはファイルハンドルINに触ることはできない

# カウント増加
$count++;

# カウントファイルに書き込み
open(OUT, "> counter.txt");
#openと>を併用することで書き込み専用でopenできる
print OUT $count;
#OUTに$countの値を収納、これによってcounter.txtの中身が$countの値になる
close(OUT);#閉じる

print <<EOL;
<html>
<body>
<p>you are $count nunbers</p>
</body>
</html>
EOL
