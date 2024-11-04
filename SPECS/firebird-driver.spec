%define dcamver 24.4.6764

Name:           firebird-driver
Version:        3.2.1
Release:        1.el%{rhel}
ExclusiveArch:  x86_64
Summary:        Driver for FireBird frame grabbers from Active Silicon

License:        Proprietary
URL:            https://www.activesilicon.com/
# See hamamatsu-sdk.
Source0:        %{dist_srv}/DCAM-API_Lite_for_Linux_v%{dcamver}.tar.gz
Patch0:         %{name}-3.2.1-pkg.patch

Requires:       gcc, make, kernel-devel
%if %{rhel} == 8
Requires:       elfutils-libelf-devel
%endif

%description

%prep
%setup -n DCAM-API_Lite_for_Linux_v%{dcamver}
tar xpf api/driver/firebird/HAM-Installer-*.tgz
rpm2cpio %{_arch}/as-fbd-linux-ham-%{version}-1.%{_arch}.rpm | cpio -id
mv usr/local/activesilicon .
cd activesilicon/source/driver/mdadrv/linux
	mv aslenum/system/*.rules "$OLDPWD"/89-activesilicon.rules
	rm -rf aslenum/system Makefile; cd -
rm -rf usr %{_arch}; patch -p1 < %{P:0}
sed -i 's/MODE="0666"/GROUP="video", MODE="0660"/; /udev_start/ d' *.rules
cd activesilicon/source/driver/mdadrv/linux
	sed -ri '/^(all|\$\(MODULE\)):$/ s/^/ccflags-y := $(ASLENUM_CFLAGS)\n/' \
		*/Makefile
	sed -ri -e '/^(all|\$\(MODULE\)):$/,$ d' -e '/^(KREL|PWD)/,/^$/ d' \
		-e '/^MDASRC_PATH/ s@:=.*@:= /var/firebird/module@' */Makefile
cd -

%build

%install
. %{_specdir}/fn-build.sh
cd %{buildroot}; mkdir -p .%{_bindir} etc/ld.so.conf.d \
	etc/udev/rules.d var/firebird usr/local/activesilicon/lib64; cd -
install -m 0755 activesilicon/lib64/*.so \
	%{buildroot}/usr/local/activesilicon/lib64
install -m 0644 aslphxapi.conf %{buildroot}/etc/ld.so.conf.d
install -m 0755 activesilicon/bin64/* \
	firebird-module-* %{buildroot}%{_bindir}
install -m 0644 *.rules %{buildroot}/etc/udev/rules.d
cp -r activesilicon/source/driver %{buildroot}/var/firebird/module
%_file_list /usr /var > noetc.lst

%files -f noetc.lst
%config(noreplace) /etc/ld.so.conf.d/*.conf
%config(noreplace) /etc/udev/rules.d/*.rules

%preun
firebird-module-make clean || true

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

