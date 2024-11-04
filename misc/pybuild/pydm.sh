src="$(src_pypi "$pkg")"
if [ "$sysver" = 7 ]; then
	patches="$pkg-1.13.0.patch"
else
	patches="$pkg-1.20.1.patch"
fi

