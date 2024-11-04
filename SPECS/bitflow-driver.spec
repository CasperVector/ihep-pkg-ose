%{eval arch}

Name:           bitflow-driver
Version:        9.08
Release:        1.el%{rhel}
Summary:        Driver for BitFlow frame grabbers

License:        Proprietary
URL:            https://bitflow.com/
Source0:        %{dist_srv}/andor-sdk3-3.15.30092.2.tgz
Patch0:         %{name}-9.08-pkg.patch

BuildRequires:  gcc
Requires:       kernel-devel
%if %{rhel} == 8
Requires:       gcc, make, elfutils-libelf-devel
%endif

%description

%prep
%autosetup -p 1 -n andor

%build

%install
. %{_specdir}/fn-build.sh
cd %{buildroot}; mkdir -p var/bitflow/module opt/bitflow \
	.%{_bindir} .%{_includedir} .%{_libdir}; cd -
install -m 0644 bitflow/inc/* %{buildroot}%{_includedir}
install -m 0755 bitflow-module-* %{buildroot}%{_bindir}
cp -r bitflow/src %{buildroot}/opt/bitflow/examples
cp -r bitflow/camf bitflow/config bitflow/fshf %{buildroot}/opt/bitflow
install -m 0644 bitflow/drv/* bitflow/%{_bits}b/lib/*.o_shipped \
	%{buildroot}/var/bitflow/module
mv %{buildroot}/var/bitflow/module/Makefile_%{_bits}b \
	%{buildroot}/var/bitflow/module/Makefile
rm %{buildroot}/var/bitflow/module/Makefile_*b
mkdir tmp
cp bitflow/%{_bits}b/lib/libBFciLib.a bitflow/src/BFciDefault.* tmp
soname=$(cd bitflow/%{_bits}b/lib; echo libBFSOciLib.*.so)
cd tmp
ar -x libBFciLib.a
gcc -fPIC -c -D BF_DEFAULT_DIR_LIST='"/opt/bitflow"' BFciDefault.c
ar -cr libBFciLib.a *.o; ranlib libBFciLib.a
gcc -shared -Wl,-soname,"$soname" *.o -o "$soname"
cd -
install -m 0644 tmp/libBFciLib.a %{buildroot}%{_libdir}
install -m 0755 tmp/"$soname" %{buildroot}%{_libdir}
%_file_list /opt /usr /var > all.lst

%files -f all.lst
%doc bitflow/README_dist

%preun
bitflow-module-make clean || true

