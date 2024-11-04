Name:           pco-sdk
Version:        1.31.0
Release:        1.el%{rhel}
Summary:        SDK for PCO cameras
ExclusiveArch:  x86_64

License:        Proprietary
URL:            https://www.excelitas.com/product/pco-software-development-kits
Source0:        %{dist_srv}/pco_sdk_%(echo %{version} | tr . _)_Linux_AMD64.zip
Patch0:         %{name}-1.31.0-pkg.patch
Requires:       libusbx

%description

%prep
%autosetup -c -n %{name}
ar x pco.sdk_%{version}_amd64.deb
tar xpf data.tar.xz
mv opt/pco/pco.sdk pco
mv usr/share/doc/pco.sdk/* pco
gzip -d pco/changelog.gz
sed -i 's/MODE="0666"/MODE="0664"/g' pco/*.rules
mkdir -p pco/skel/.config pco/skel/.pco/pco_logging
mv pco/inifiles pco/skel/.config/pco
for name in pco_recorder pco_sc2cam pco_usb pco_usb3 pco_gige \
	pco_devicemgr pco_cl_me4 pco_clhs_me5 pco_clhs_kaya; \
	do touch pco/skel/.pco/pco_logging/"$name".txt; done

%build

%install
. %{_specdir}/fn-build.sh
cd %{buildroot}; mkdir -p opt/pco/lib etc/ld.so.conf.d etc/udev/rules.d \
	.%{_bindir} .%{_includedir} .%{_libdir}/genicam; cd -
install -m 0755 pco/lib/*.so.*.* %{buildroot}%{_libdir}
install -m 0755 pco/lib/genicam/*.so %{buildroot}/opt/pco/lib
mv %{buildroot}%{_libdir}/libOpenCL.so* %{buildroot}/opt/pco/lib
_link_so %{buildroot}%{_libdir}/*.so.*.*
install -m 0644 pco.conf %{buildroot}/etc/ld.so.conf.d
install -m 0644 pco/include/*.h %{buildroot}%{_includedir}
install -m 0755 pco-user-init pco/bin/* %{buildroot}%{_bindir}
install -m 0644 pco/*.rules %{buildroot}/etc/udev/rules.d/99-pco_usb.rules
cp -r pco/samples pco/skel %{buildroot}/opt/pco
%_file_list /opt /usr > noetc.lst

%files -f noetc.lst
%config(noreplace) /etc/ld.so.conf.d/*.conf
%config(noreplace) /etc/udev/rules.d/*.rules
%doc pco/*.pdf pco/changelog pco/copyright

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

