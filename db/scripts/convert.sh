#!/bin/bash
if [ "x$1" == "x" ]; then
  echo "Usage: $0 <dumpname>"
  exit
fi

cat $1 |
grep -v ' KEY "' |
grep -v ' UNIQUE KEY "' |
grep -v ' PRIMARY KEY ' |
sed '/^SET/d' |
sed 's/UNLOCK TABLES;/ /g' |
sed 's/LOCK TABLES.*;/ /g' |
sed 's/ ENGINE=.*;/;/g' |
sed 's/ COMMENT.*,/,/g' |
sed 's/ unsigned / /g' |
sed 's/ auto_increment/ primary key autoincrement/g' |
sed 's/ NOT NULL AUTO_INCREMENT/ primary key autoincrement/g' |
sed 's/ UNIQUE KEY.*(/ UNIQUE(/g' |
sed 's/ KEY.*/ /g' |
sed 's/ mediumint([0-9]*) / integer /g' |
sed 's/ smallint([0-9]*) / integer /g' |
sed 's/ tinyint([0-9]*) / integer /g' |
sed 's/ int([0-9]*) / integer /g' |
sed 's/ character set [^ ]* / /g' |
sed 's/ enum([^)]*) / varchar(255) /g' |
sed 's/ on update [^,]*//g' |
sed 's/\\r\\n/\\n/g' |
sed "s/\\\\'/''/g" |
sed 's/\\"/"/g' |
perl -e 'local $/;$_=<>;s/,\n\)/\n\)/gs;print "begin;\n";print;print "commit;\n"' |
perl -pe '
if (/^(INSERT.+?)\(/) {
  $a=$1;
  s/\\'\''/'\'\''/g;
  s/\\n/\n/g;
  s/\),\(/\);\n$a\(/g;
}
' > $1.sql
cat $1.sql > $1.err
ERRORS=`cat $1.err | wc -l`
if [ $ERRORS == 0 ]; then
  echo "Conversion completed without error. Output file: $1.db"
  rm $1.sql
  rm $1.err
else
  echo "There were errors during conversion.  Please review $1.err and $1.sql for details."
fi
