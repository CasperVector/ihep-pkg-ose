#!/bin/sh -e
exec xargs -r wget -nc -t 1 -P SOURCES < "$1"

