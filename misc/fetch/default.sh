#!/bin/sh -e
exec xargs -r wget -nc -P SOURCES < "$1"

