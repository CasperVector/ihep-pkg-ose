Name:           ebus-driver
Version:        4.1.7.3988
Release:        1.el%{rhel}
Summary:        Driver for Pleora eBUS

License:        Proprietary
URL:            https://www.pleora.com/
Source0:        %{dist_srv}/picam_sdk-5.12.2.run
Patch0:         %{name}-4.1.7.3988-pkg.patch

Requires:       expat, gcc, make, kernel-devel
%if %{rhel} == 8
Requires:       elfutils-libelf-devel
%endif

%description

%prep
%setup -T -c -n %{name}
install -m 0755 %{S:0} . && ./picam_sdk-*.run --keep --noexec
cd install_image; patch -p1 < %{P:0}
cd pleora; rm bin/*.bin lib/libPvGUI.so*
cd module/*/; mv libebTransportLayer-%{_arch}.a \
	libebTransportLayer-%{_arch}.a_shipped
cd ../../bin; rm install_daemon.sh install_libraries.sh \
	set_socket_buffer_size.sh uninstall.sh; cd ../lib
ls | grep '\.so\>' | grep -vE '[0-9]{4,}$' | xargs rm -v
find genicam -name '*.so' -exec chmod 0755 '{}' '+'

%build

%install
. %{_specdir}/fn-build.sh
pldir=/opt/pleora/ebus_sdk/%{_arch}
cd %{buildroot}; mkdir -p var/ebus ."$pldir"/lib \
	etc/ld.so.conf.d .%{_bindir} .%{_includedir} .%{_libdir}
cd -; cd install_image
install -m 0755 pleora/lib/*.so.* %{buildroot}%{_libdir}
cp -r pleora/lib/genicam %{buildroot}"$pldir"/lib
_link_so %{buildroot}%{_libdir}/*.so.*
install -m 0644 eBUS_SDK.conf %{buildroot}/etc/ld.so.conf.d
install -m 0644 pleora/include/* %{buildroot}%{_includedir}
install -m 0755 ebus-module-* %{buildroot}%{_bindir}
cp -r pleora/bin pleora/share %{buildroot}"$pldir"
cp -r pleora/module/ebUniversalProForEthernet %{buildroot}/var/ebus/module
cd -; %_file_list /opt /usr /var > noetc.lst

%files -f noetc.lst
%config(noreplace) /etc/ld.so.conf.d/*.conf

%pre -n ebus-driver
[ -f %{_libdir}/libexpat.so.0 ] || ln -s libexpat.so.1 %{_libdir}/libexpat.so.0

%preun -n ebus-driver
if [ "$(realpath %{_libdir}/libexpat.so.0)" = %{_libdir}/libexpat.so.1 ]
	then rm %{_libdir}/libexpat.so.0; fi
ebus-module-make clean || true

%post -n ebus-driver -p /sbin/ldconfig
%postun -n ebus-driver -p /sbin/ldconfig

