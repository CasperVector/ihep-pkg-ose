%define sdkver 24026764

Name:           hamamatsu-sdk
Version:        24.4.6764
Release:        1.el%{rhel}
ExclusiveArch:  x86_64
Summary:        Hamamatsu DCAM SDK

License:        Proprietary
URL:            https://dcam-api.com/
# https://www.hamamatsu.com/content/dam/hamamatsu-photonics/sites/static/sys/dcam-api-for-linux/tar-gz/$(basename ${S:0})
Source0:        %{dist_srv}/DCAM-API_Lite_for_Linux_v%{version}.tar.gz
# https://www.hamamatsu.com/content/dam/hamamatsu-photonics/sites/static/sys/dcam-sdk/$(basename ${S:1})
Source1:        %{dist_srv}/Hamamatsu_DCAMSDK4_v%{sdkver}.zip
Patch0:         %{name}-24.4.6764-pkg.patch

Requires:       libusb, firebird-driver

%description

%prep
%setup -n DCAM-API_Lite_for_Linux_v%{version}
unzip %{S:1}; patch -p1 < %{P:0}
sed -i 's/MODE="666"/GROUP="video", MODE="0660"/' \
	api/driver/usb/udev/rules.d/*.rules

%build

%install
. %{_specdir}/fn-build.sh
dcamdir=usr/local/hamamatsu_dcam/api
bdcamdir=%{buildroot}/"$dcamdir"
cd %{buildroot}; mkdir -p opt/hamamatsu "$dcamdir" .%{_bindir} \
	.%{_includedir} .%{_libdir} etc/ld.so.conf.d etc/udev/rules.d; cd -
cd %{buildroot}/opt/hamamatsu; mkdir -p camera_properties dcam_samples; cd -
cd "$bdcamdir"; mkdir -p etc/aslphx etc/modules modules; cd -
install -m 0755 tools/%{_arch}/* %{buildroot}%{_bindir}
install -m 0644 dcamsdk4/inc/* %{buildroot}%{_includedir}
install -m 0644 dcamsdk4/doc/camera_properties/* \
	%{buildroot}/opt/hamamatsu/camera_properties
install -m 0644 api/runtime/etc/ld.so.conf.d/*.conf \
	%{buildroot}/etc/ld.so.conf.d
install -m 0644 api/driver/usb/udev/rules.d/*.rules \
	%{buildroot}/etc/udev/rules.d
cp -r dcamsdk4/samples/* %{buildroot}/opt/hamamatsu/dcam_samples

cd api/runtime/%{_arch}
ver="$(ls core/libdcamapi.so.* | sed 's/.*\.so\.//')"
install -m 0755 core/libdcamapi.so.* "$bdcamdir"
install -m 0644 core/dcamlog.conf "$bdcamdir"/etc
install -m 0644 fbd/aslphx/* "$bdcamdir"/etc/aslphx
install -m 0755 core/libdcamdig.so.* \
	fbd/lib*.so.* usb*/lib*.so.* "$bdcamdir"/modules
install -m 0644 core/dcamdig.conf \
	fbd/*.conf usb*/*.conf "$bdcamdir"/etc/modules
sed -i "/module\\.version$/ s/\$/\\t$ver/" "$bdcamdir"/etc/modules/*.conf
cd -; cd %{buildroot}
_link_so "$dcamdir"/*.so.* "$dcamdir"/modules/*.so.*
ls "$dcamdir"/*.so* | sed 's@^@/@' | xargs ln -st %{buildroot}%{_libdir}
cd -; cd "$bdcamdir"/modules; for name in *.so; do
	ln -snf "$name".*.*.* "$name"; done
cd -; %_file_list /opt /usr > noetc.lst

%files -f noetc.lst
%config(noreplace) /etc/ld.so.conf.d/*.conf
%config(noreplace) /etc/udev/rules.d/*.rules
%doc doc/* dcamsdk4/doc/api_reference/*

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

