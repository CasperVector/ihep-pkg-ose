%define repo KAYA_Vision_Point_Setup
Name:           kaya-driver
Version:        5.4.0.7320
Release:        1.el%{rhel}
Summary:        Driver for KAYA frame grabbers

License:        Proprietary
URL:            https://kayainstruments.com/
# Unavailable from the following, and instead obtained from Tucsen:
# https://storage.kayainstruments.com/s/vision-point?path=%2FVision+Point+Installation+for+Linux%2FArchive
Source0:        %{dist_srv}/%{repo}_2020.3_RedHat_CentOS_7.9.2009_x64__branches-sw_5_4_x_2020_3_build_5.4.0.7320M_2021-08-20_21-16-34.tar.gz
Patch0:         %{name}-5.4.0.7320-pkg.patch
Requires:       opencv, kernel-devel
%if %{rhel} == 8
Requires:       elfutils-libelf-devel
%endif

%description

%prep
%setup -c -n %{name}
. %{_specdir}/fn-build.sh
mv %{repo}_*_build_%{version}*/ %{repo}
chmod -R go-w %{repo}; cd %{repo}; patch -p1 < %{P:0}
chmod 0755 Vision\ Point/lib/*.so*
rm Vision\ Point/lib/KYServiceClientConsole

%install
. %{_specdir}/fn-build.sh
kayadir=opt/KAYA_Instruments
bkayadir=%{buildroot}/"$kayadir"
cd %{buildroot}; mkdir -p etc/ld.so.conf.d .%{_bindir} \
	.%{_prefix}/lib/systemd/system var/kaya "$kayadir"
cd -; cd %{repo}
install -m 0755 kaya-module-* KYService/KYService %{buildroot}%{_bindir}
cp -r Vision\ Point/include %{buildroot}%{_includedir}
cp -r Vision\ Point/lib Vision\ Point/Examples Doc "$bkayadir"
install -m 0644 kaya.conf %{buildroot}/etc/ld.so.conf.d
cp -r PCI_drv_Linux %{buildroot}/var/kaya/module
install -m 0644 *.service %{buildroot}%{_prefix}/lib/systemd/system
cd -; cd %{buildroot}/var/kaya/module
rm -f *.ko *.sh *.service
cd -; %_file_list /opt /usr /var > noetc.lst

%files -f noetc.lst
%config(noreplace) /etc/ld.so.conf.d/*.conf

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

