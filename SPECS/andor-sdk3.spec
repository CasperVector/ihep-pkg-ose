%{eval arch}

Name:           andor-sdk3
Version:        3.15.30092.2
Release:        3.el%{rhel}
Summary:        SDK for Andor sCMOS cameras

License:        Proprietary
URL:            https://andor.oxinst.com/
Source0:        %{dist_srv}/%{name}-%{version}.tgz
Patch0:         %{name}-3.15.30092.2-pkg.patch

Requires:       bitflow-driver

%description

%prep
%autosetup -p 1 -n andor
sed -i -e 's/GROUP="users", MODE="666"/ GROUP="video", MODE="0660"/' \
	-e 's/MODE="0777"/GROUP="video", MODE="0770"/' etc/*.rules
chmod 0644 doc/*
cd Python/pyAndorSDK3
chmod -R go-w docs
mv LICENSE ../../pyAndorSDK3-LICENSE
mv README.pdf ../../pyAndorSDK3-README.pdf
mv changelog.txt pyAndorSDK3-ChangeLog.txt

%build

%install
. %{_specdir}/fn-build.sh
cd %{buildroot}; mkdir -p opt/andor opt/apogee \
	.%{_libdir}/python%{_py3}/site-packages/pyAndorSDK3 \
	etc/ld.so.conf.d etc/udev/rules.d .%{_bindir} .%{_includedir}; cd -
install -m 0644 inc/* %{buildroot}%{_includedir}
cp -r GenAPIinc %{buildroot}/opt/andor/include
install -m 0755 %{_arch}/*.so.* %{buildroot}%{_libdir}
cp -r %{_arch}/GenAPI %{buildroot}/opt/andor/lib
_link_so %{buildroot}%{_libdir}/*.so.*
install -m 0644 andor3.conf %{buildroot}/etc/ld.so.conf.d
install -m 0644 etc/*.rules \
	%{buildroot}/etc/udev/rules.d/99-andor3-cameras.rules
cp -r examples %{buildroot}/opt/andor
tar -C %{buildroot}/opt/apogee -xf etc-Apogee-camera.tgz
cp -r Python/pyAndorSDK3/docs/html %{buildroot}/opt/andor/pydocs
cp -r Python/pyAndorSDK3/examples %{buildroot}/opt/andor/pyexamples
install -m 0644 Python/pyAndorSDK3/pyAndorSDK3/*.py \
	%{buildroot}%{_libdir}/python%{_py3}/site-packages/pyAndorSDK3
%_file_list /opt /usr > noetc.lst

%files -f noetc.lst
%config(noreplace) /etc/ld.so.conf.d/*.conf
%config(noreplace) /etc/udev/rules.d/*.rules
%doc ReleaseNotes.txt pyAndorSDK3-* doc/*

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

