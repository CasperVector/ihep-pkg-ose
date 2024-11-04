Name:           libxsp
Version:        2.4.0
Release:        1.el%{rhel}
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
cd %{buildroot}; mkdir -p .%{_includedir} .%{_libdir}; cd -
install -m 0644 libxsp.h %{buildroot}%{_includedir}
install -m 0755 libxsp.so.* %{buildroot}%{_libdir}
_link_so %{buildroot}%{_libdir}/libxsp.so.*
gzip -d < changelog.gz > changelog.txt

%files
%{_includedir}/*
%{_libdir}/*
%doc changelog.txt *.pdf

