%define repo edm
%define commit 1-12-105Q
%define cmd_flags CMD_CFLAGS='%{optflags} -Wno-error=format-security' \\\
	CMD_CXXFLAGS='%{optflags} -Wno-error=format-security'
%define etop_dest %{buildroot}%{etop_base}
%define __arch_install_post true
%{meta license=GPLv2+ version=commit,1}

Name:           epics-edm
Summary:        EPICS - Extensible Display Manager
URL:            https://controlssoftware.sns.ornl.gov/edm/
Source0:        https://epics.anl.gov/download/extensions/extensionsTop_20120904.tar.gz
Source1:        %{github_archive_ver gnartohl %{repo} %{commit} V}
Source2:        %{name}-fonts.list

BuildRequires:  epics-base, gcc-c++, make, libX11-devel, libXtst-devel
BuildRequires:  zlib-devel, giflib-devel, libpng-devel, motif-devel
Requires:       epics-base, libX11, libXtst, zlib
Requires:       giflib, libpng, motif, xorg-x11-fonts-Type1
Requires:       xorg-x11-fonts-misc, xorg-x11-fonts-100dpi, xorg-x11-fonts-75dpi
Requires:       xorg-x11-fonts-ISO8859-1-100dpi, xorg-x11-fonts-ISO8859-1-75dpi

%{inherit epics + global}
%description

%prep
%autosetup -n extensions
tar xpf %{S:1}
mv edm-%{commit} src/edm
cp %{S:2} src/edm/setup/fonts.list
sed -i '/DIRS :=/ s/=.*/= edm/' src/Makefile

%build

%install
. %{_specdir}/fn-build.sh
sed -i '/^EPICS_BASE=/ s@=.*@=%{etop_base}@' configure/RELEASE
make -k %{?_smp_mflags} %{cmd_flags} DESTDIR=%{buildroot} \
	INSTALL_LOCATION=%{etop_dest} install ||
	make -k %{?_smp_mflags} %{cmd_flags} DESTDIR=%{buildroot} \
		INSTALL_LOCATION=%{etop_dest} install ||
	make -j1 %{cmd_flags} DESTDIR=%{buildroot} \
		INSTALL_LOCATION=%{etop_dest} install
mkdir -p %{etop_dest}/edm/helpFiles
install -m 0644 src/edm/setup/* %{etop_dest}/edm
install -m 0644 src/edm/helpFiles/* %{etop_dest}/edm/helpFiles
rm -rf %{etop_dest}/edm/setup.sh %{etop_dest}/include
mkdir -p %{buildroot}/etc/profile.d; (
	echo 'EDMLIBS=%{etop_base}/lib/%{epics_arch}'
	echo 'export EDMLIBS'
	echo 'EDMFILES=%{etop_base}/edm'
	echo 'export EDMFILES'
	echo 'EDMOBJECTS=%{etop_base}/edm'
	echo 'export EDMOBJECTS'
	echo 'EDMPVOBJECTS=%{etop_base}/edm'
	echo 'export EDMPVOBJECTS'
	echo 'EDMHELPFILES=%{etop_base}/edm/helpFiles'
	echo 'export EDMHELPFILES'
	echo 'EDMDATAFILES=%{etop_res}/edl'
	echo 'export EDMDATAFILES'; echo
) > %{buildroot}/etc/profile.d/epics-edm.sh
%_rm_extras; %_file_list %{epics_root} > epics.lst

%files -f epics.lst
%config(noreplace) /etc/profile.d/epics-edm.sh

