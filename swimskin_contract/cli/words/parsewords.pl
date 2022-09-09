#!/usr/bin/perl

use DBI;

$dbh = DBI -> connect("dbi:Pg:dbname=ethereum;host=127.0.0.1;port=54341", "postgres", 'fanif@x3R', {Autocommit => 0, RaiseError => 1}) or die $DBI::errstr;
open(FILE, "<raw.html") || die "Error opening file";

$data = <FILE>;

close(FILE);

@list = split(/href/, $data);
print $#list;

open(FILE, ">words.dat") || die "Error opening file";

foreach (@list) {
	$_ =~ />(.*)<\/a>/;
	#print $1."\n";
	print FILE $1."\n";
	$sth = $dbh->do("insert into words (word) values ('$1')");
	$dbh->commit;
}

close(FILE);

