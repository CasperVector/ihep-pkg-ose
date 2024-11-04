Name:           andor-sdk2
Version:        2.104.30064.0
Release:        2.el%{rhel}
Summary:        SDK for Andor CCD cameras
ExclusiveArch:  x86_64

License:        Proprietary
URL:            https://andor.oxinst.com/
Source0:        %{dist_srv}/%{name}-%{version}.tgz
Patch0:         %{name}-2.104.30064.0-pkg.patch
Requires:       libusb

%description

%prep
%autosetup -p 1 -n andor
sed -i 's/MODE="0666"/GROUP="video", MODE="0660"/' script/spectrograph.rules

%build

%install
. %{_specdir}/fn-build.sh
cd %{buildroot}; mkdir -p etc/andor usr/local/etc opt/andor2 \
	etc/udev/rules.d .%{_includedir} .%{_libdir}; cd -
echo '/usr/local' > %{buildroot}/etc/andor/andor.install
cp -r etc %{buildroot}/usr/local/etc/andor
cp -r examples %{buildroot}/opt/andor2
install -m 0644 script/andor.rules \
	%{buildroot}/etc/udev/rules.d/99-andor2-cameras.rules
install -m 0644 script/spectrograph.rules \
	%{buildroot}/etc/udev/rules.d/98-spectrograph.rules
install -m 0644 include/*.h %{buildroot}%{_includedir}
for name in libandor libatsifio libatspectrograph libUSBI2C; do
	install -m 0755 lib/"$name"-%{_arch}.so.%{version} \
		%{buildroot}%{_libdir}/"$name".so.%{version}
	_link_so %{buildroot}%{_libdir}/"$name".so.%{version}; done
%_file_list /etc /opt /usr | sed '/\.rules/d' > norules.lst

%files -f norules.lst
%config(noreplace) /etc/udev/rules.d/*.rules
%doc doc/*

