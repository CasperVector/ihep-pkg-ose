Name:           picam-sdk
Version:        5.12.2
Release:        5.el%{rhel}
ExclusiveArch:  x86_64
Summary:        SDK for Princeton Instruments PICam cameras

License:        Proprietary
URL:            https://www.princetoninstruments.com/
# https://cdn.princetoninstruments.com/picam/archives/picam_sdk-v${version}.run
Source0:        %{dist_srv}/picam_sdk-v%{version}.run
Patch0:         %{name}-5.12.2-pkg.patch

Requires:       ebus-driver

%description

%prep
%setup -T -c -n %{name}
install -m 0755 %{S:0} .; ./picam_sdk-*.run --keep --noexec
cd install_image; patch -p1 < %{P:0}
chmod 0644 pi/documentation/*

%build

%install
. %{_specdir}/fn-build.sh
pidir=/opt/PrincetonInstruments/picam
cd %{buildroot}; mkdir -p .%{_bindir} .%{_includedir} .%{_libdir} \
	etc/udev/rules.d usr/lib/tmpfiles.d ."$pidir"
cd -; cd install_image
install -m 0755 pi/runtime/*.so.* %{buildroot}%{_libdir}
_link_so %{buildroot}%{_libdir}/*.so.*
install -m 0644 pi/runtime/*.dat %{buildroot}%{_libdir}
install -m 0644 pi/includes/* %{buildroot}%{_includedir}
install -m 0644 *.rules %{buildroot}/etc/udev/rules.d/99-picam.rules
install -m 0644 pi/misc/picam-tmp.conf %{buildroot}/usr/lib/tmpfiles.d
_fix_perm pi/samples; cp -r pi/samples %{buildroot}"$pidir"
cd -; %_file_list /opt /usr > noetc.lst

%files -f noetc.lst
%config(noreplace) /etc/udev/rules.d/*.rules
%doc install_image/pi/documentation/*

