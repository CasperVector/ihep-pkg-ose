Name:           uldaq
Version:        1.2.1
Release:        1.el%{rhel}
Summary:        MCC Universal Library for Linux

License:        MIT
URL:            https://github.com/mccdaq/%{name}
Source0:        https://github.com/mccdaq/%{name}/releases/download/v%{version}/libuldaq-%{version}.tar.bz2
Patch0:         %{name}-1.2.1-pkg.patch

BuildRequires:  gcc, gcc-c++, make, libusbx-devel
Requires:       libusbx-devel

%description

%prep
%autosetup -n libuldaq-%{version}
sed -i 's/GROUP="adm", MODE="0666"/GROUP="dialout", MODE="0660"/' rules/*.rules

%build
./configure --prefix=/usr --libdir=%{_libdir}
make %{?_smp_mflags} CFLAGS="%{optflags}" CXXFLAGS="%{optflags}"

%install
make DESTDIR=%{buildroot} install

%files
%config(noreplace) /etc/udev/rules.d/50-uldaq.rules
%{_includedir}/*
%{_libdir}/lib*
%{_libdir}/pkgconfig/*
%doc README.md

