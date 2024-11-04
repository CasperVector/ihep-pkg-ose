#!/bin/sh -e

sed -r 's@^fetch://([^/]+)/([^/]+)/([^/]+)/archive/([^/]+)/([^/]+)@\1 \2 \3 \4 \5@' < "$1" |
	while read host owner repo commit file; do
		[ -f SOURCES/"$file" ] || wget -O SOURCES/"$file" \
			"https://$host/$owner/$repo/archive/$commit.tar.gz"; done

