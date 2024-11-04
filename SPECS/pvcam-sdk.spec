%if %{_arch} == x86_64
%define sdkarch x86_64
%else
%define sdkarch i686
%endif

Name:           pvcam-sdk
Version:        3.10.0.3
Release:        1.el%{rhel}
Summary:        SDK for Teledyne Photometrics cameras

License:        Proprietary
URL:            https://www.photometrics.com/
Source0:        %{dist_srv}/PVCAM-Linux-%(echo %{version} | tr . -).zip
Patch0:         %{name}-3.10.0.3-pkg.patch
Requires:       libusbx, kernel-devel
%if %{rhel} == 8
Requires:       elfutils-libelf-devel
%endif

%description

%package -n %{name}-tools
Summary:        Utility programs from %{name}
Requires:       %{name}, libtiff, wxGTK3

%description -n %{name}-tools

%prep
%autosetup -p 1 -c -n %{name}
. %{_specdir}/fn-build.sh
chmod 0755 pvcam/pvcam_%{version}.run pvcam-sdk/pvcam-sdk_%{version}-1.run
./pvcam/pvcam_%{version}.run --keep --noexec
./pvcam-sdk/pvcam-sdk_%{version}-1.run --keep --noexec
_fix_perm pvcam*
mv pvcam_%{version}/opt/pvcam/* pvcam
mv pvcam-sdk_%{version}-1/opt/pvcam/* pvcam-sdk
sed -ri -e 's/-L\$\{libdir\} //' -e '/^(prefix|libdir)=/d' \
	-e '/^includedir=/ s@=.*@=/usr/include/pvcam@g' \
	pvcam-sdk/sdk/pkgconfig/%{sdkarch}/*.pc
sed -i 's/GROUP="users"/GROUP="video"/g' pvcam/lib/udev/rules.d/*.rules
mv pvcam-sdk/sdk/helpers/*/bin/linux-%{sdkarch}/release/* \
	pvcam/library/%{sdkarch}
mv pvcam-sdk/sdk/helpers/*/inc/* pvcam-sdk/sdk/include
mv pvcam-sdk/sdk/helpers/*/doc/*.pdf pvcam/doc
cd pvcam/bin/VersionInformation/%{sdkarch}
mv VersionInformation* PVCamVersion
cd -; cd pvcam/bin/PVCamTest/%{sdkarch}
rm PVCamTest PVCamTest.gtk2 *.so*; mv PVCamTest.gtk3 PVCamTest
cd -; cd pvcam-sdk/sdk/examples
for name in *; do mv "$name"/src/* "$name"; rmdir "$name"/src; done
rm -rf PVCamTest/bin; mkdir bin
mv */bin/linux-%{sdkarch}/release/* bin; rm -rf bin/*.so* */bin
mv bin pvcam_helper_color/* code_samples; rmdir pvcam_helper_color

%build

%install
. %{_specdir}/fn-build.sh
cd %{buildroot}; mkdir -p etc/profile.d etc/udev/rules.d \
	.%{_bindir} .%{_includedir} .%{_libdir}/pkgconfig \
	opt/pvcam/drivers/user-mode var/pvcam; cd -
install -m 0644 pvcam/etc/profile.d/*.sh %{buildroot}/etc/profile.d
install -m 0644 pvcam/lib/udev/rules.d/*.rules %{buildroot}/etc/udev/rules.d
install -m 0644 pvcam-sdk/sdk/pkgconfig/%{sdkarch}/*.pc \
	%{buildroot}%{_libdir}/pkgconfig
install -m 0755 pvcam/drivers/user-mode/pvcam_usb.%{sdkarch}.umd \
	%{buildroot}/opt/pvcam/drivers/user-mode
find pvcam/library/%{sdkarch} -type f -not -type l -exec \
	install -m 0755 -t %{buildroot}%{_libdir} '{}' '+'
_link_so %{buildroot}%{_libdir}/*.so.*
install -m 0644 pvcam-sdk/sdk/include/*.h %{buildroot}%{_includedir}
install -m 0755 pvcam/bin/*/%{sdkarch}/* %{buildroot}%{_bindir}
cp -r pvcam-sdk/sdk/doc pvcam-sdk/sdk/examples %{buildroot}/opt/pvcam
install -m 0644 HOWTO %{buildroot}/opt/pvcam/examples/code_samples
cp -r pvcam/drivers/in-kernel/pcie/src %{buildroot}/var/pvcam/module
install -m 0755 pvcam/drivers/in-kernel/pcie/hotplug_pcie.sh \
	%{buildroot}/opt/pvcam
%_file_list /opt /usr /var | grep -v '/usr/bin\>' > nobin.lst
%_file_list /etc | sed 's/^/%config(noreplace) /' >> nobin.lst
%_file_list /usr/bin > bin.lst
install -m 0755 pvcam-module-* %{buildroot}%{_bindir}
mv 'pvcam/doc/PVCamTest Color Tutorial.pdf' .

%files -f nobin.lst
/usr/bin/pvcam-module-*
%doc pvcam/pvcam_faq.txt pvcam/pvcam.license.txt pvcam/doc/*.pdf
%doc pvcam-sdk/pvcam-sdk_faq.txt pvcam-sdk/pvcam-sdk.license.txt

%files -n %{name}-tools -f %{_builddir}/%{name}/bin.lst
%doc "PVCamTest Color Tutorial.pdf"

%preun
pvcam-module-make clean || true

