src="$(src_pypi "$pkg")"
if [ "$sysver" = 7 ]; then
	patches="$pkg-0.11.1.patch"
else
	patches="$pkg-0.13.7.patch"
fi

