%{eval arch}
%define dversion 20240723

Name:           ximea-sdk
Version:        4_27_10
Release:        2.el%{rhel}
Summary:        Ximea camera SDK

License:        Proprietary
URL:            https://www.ximea.com/
# https://www.ximea.com/downloads/recent/XIMEA_Linux_SP.tgz
Source0:        %{dist_srv}/XIMEA_Linux_SP-V%{version}.tgz
Source1:        %{codeberg_archive CasperVector ADXimea v%{dversion}}
Patch0:         %{name}-4_27_10-pkg.patch
Requires:       libusbx, libraw1394, libtiff, kernel-devel
%if %{rhel} == 8
Requires:       elfutils-libelf-devel
%endif

%description

%prep
%autosetup -p 1 -n package
tar xpf %{S:1}; mv adximea/documentation docs
rm -rf adximea bin/streamViewer.*
sed -i 's/plugdev/video/g' src/ximea_cam_pcie/*.sh
sed -i 's/GROUP="plugdev"/GROUP="video"/' libs/libusb/*.rules

%build

%install
. %{_specdir}/fn-build.sh
cd %{buildroot}; mkdir -p opt/XIMEA/lib var/ximea \
	.%{_libdir}/python%{_py3}/site-packages/ximea/libs \
	etc/udev/rules.d .%{_bindir} .%{_includedir}; cd -
cp -r data docs examples samples %{buildroot}/opt/XIMEA
install -m 0644 include/*.h %{buildroot}%{_includedir}
install -m 0644 libs/libusb/*.rules %{buildroot}/etc/udev/rules.d
install -m 0755 api/X%{_bits}/libm3api.so.* %{buildroot}%{_libdir}
_link_so %{buildroot}%{_libdir}/libm3api.so.*
install -m 0755 libs/gentl/X%{_bits}/* %{buildroot}/opt/XIMEA/lib
%if %{_arch} == x86_64
install -m 0755 libs/xiapi_dng_store/X%{_bits}/* %{buildroot}/opt/XIMEA/lib
%endif

cd bin; for name in *.%{_bits}; do
    install -m 0755 $name %{buildroot}%{_bindir}/${name%.%{_bits}}
done; cd -
install -m 0644 api/Python/v3/ximea/*.py \
	%{buildroot}%{_libdir}/python%{_py3}/site-packages/ximea
cp -r api/Python/v3/ximea/libs/x%{_bits} \
	%{buildroot}%{_libdir}/python%{_py3}/site-packages/ximea/libs
install -m 0755 ximea-module-* %{buildroot}%{_bindir}
cp -r src/ximea_cam_pcie %{buildroot}/var/ximea/module
%_file_list /opt /usr /var > noetc.lst

%files -f noetc.lst
%config(noreplace) /etc/udev/rules.d/*.rules
%doc README* License.txt

%preun
ximea-module-make clean || true

