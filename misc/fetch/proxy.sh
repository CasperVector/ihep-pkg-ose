#!/bin/sh -e

[ -f misc/fetch/proxy-conf.sh ] && . ./misc/fetch/proxy-conf.sh
exec ./misc/fetch/default.sh "$@"

