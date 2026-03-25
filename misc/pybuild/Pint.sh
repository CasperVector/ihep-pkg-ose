src="$(src_pypi "$pkg")"
patches="$pkg-0.23.patch"
do_compile() {
	pip3 install --user setuptools_scm
	python3 -m build --no-isolation --wheel
}

