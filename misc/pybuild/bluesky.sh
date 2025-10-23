src="$(src_pypi "$pkg")"
if [ "$sysver" = 7 ]; then
	patches="$pkg-1.6.7-common.patch $pkg-1.6.7-numpy.patch"
else
	patches="$pkg-1.6.7-common.patch $pkg-1.8.3-numpy.patch"
fi

