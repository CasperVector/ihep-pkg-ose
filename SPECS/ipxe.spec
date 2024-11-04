Name:           ipxe
Version:        1.21.1
Release:        1.el%{rhel}
Summary:        iPXE: open-source boot firmware

License:        GPLv2+
URL:            https://ipxe.org/
Source0:        %{github_archive_ver ipxe %{name} %{version} v}
Patch0:         %{name}-1.21.1-iflinkwait.patch

BuildRequires:  gcc, make, perl, xz-devel

%description

%prep
%autosetup -p 2 -n %{name}-%{version}/src

%build
make %{?_smp_mflags} bin/ipxe.pxe bin/undionly.kpxe bin-x86_64-efi/ipxe.efi

%install
mkdir -p %{buildroot}%{_datadir}/%{name}
cp bin/ipxe.pxe bin/undionly.kpxe bin-x86_64-efi/ipxe.efi \
	%{buildroot}%{_datadir}/%{name}

%files
%{_datadir}/%{name}/*

