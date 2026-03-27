Name:           libxsp
Version:        2.4.0
Release:        2.el%{rhel}
ExclusiveArch:  x86_64
Summary:        SDK for detectors from X-Spectrum

License:        Proprietary
URL:            https://x-spectrum.de/
# Assembled from files on the computer provided by X-Spectrum.
Source0:        %{dist_srv}/%{name}-%{version}.tar.gz

Requires:       blosc, czmq, numactl-libs, yaml-cpp

%description

%prep
%autosetup

%build

%install
. %{_specdir}/fn-build.sh
cd %{buildroot}; mkdir -p .%{_bindir} \
	.%{_includedir} .%{_libdir} .%{_mandir}/man1; cd -
install -m 0755 convert_xsp_config %{buildroot}%{_bindir}
install -m 0644 libxsp.h %{buildroot}%{_includedir}
install -m 0755 libxsp.so.* %{buildroot}%{_libdir}
_link_so %{buildroot}%{_libdir}/libxsp.so.*
gzip -d < changelog.gz > changelog.txt
gzip -d  < convert_xsp_config.1.gz \
	> %{buildroot}%{_mandir}/man1/convert_xsp_config.1

%files
%{_bindir}/*
%{_includedir}/*
%{_libdir}/*
%{_mandir}/*/*
%doc LICENSE changelog.txt *.pdf

