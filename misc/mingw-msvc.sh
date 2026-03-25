#!/bin/sh -e
# ./mingw-msvc.sh \
# 'C:\Program Files (x86)\Microsoft Visual Studio\2022\VC\Auxiliary\Build\vcvars64.bat'

#env -i COMSPEC='C:\Windows\system32\cmd.exe' PATH='C:/Windows/system32' \
./mingw-msvc.bat "$1" | grep '=' |
sed 's/^/export /; s/=/="/; s/$/"/; s@\\@/@g'

