#!/bin/sh -e

handles=default
filter() {
	grep -E "$2" < /tmp/fetch/default.lst > /tmp/fetch/"$1".lst || true
	grep -vE "$2" < /tmp/fetch/default.lst > /tmp/fetch/default.tmp || true
	mv -f /tmp/fetch/default.tmp /tmp/fetch/default.lst
	handles="$1 $handles"
}

mkdir /tmp/fetch
cat "$1" > /tmp/fetch/default.lst
filter proxy '^https://example\.com/'
for name in $handles; do
	./misc/fetch/"$name".sh /tmp/fetch/"$name".lst; done
rm -rf /tmp/fetch

