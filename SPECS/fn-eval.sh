#!/bin/sh -

(
	printf 'Name: test\nVersion: 0\nRelease: 0\nSummary: test\n'
	printf 'License: test\n\n%%description\n\n'
	echo $* | xargs | tr ' ' '\n' |
		sed 's@^@SPECS/classes/eval.@; s@$@.spec@' | xargs cat
) | rpmspec --define "_topdir $PWD" -P /dev/stdin |
	sed -n '/%description/,$ p' | tail -n +2

