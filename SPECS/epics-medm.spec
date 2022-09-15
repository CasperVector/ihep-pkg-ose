%{meta license=EPICS version=3_1_17,2}

Name:           epics-medm
Summary:        EPICS - Motif Editor and Display Manager
URL:            https://epics.anl.gov/extensions/medm/index.php
Source0:        https://epics.anl.gov/download/extensions/extensionsTop_20120904.tar.gz
Source1:        %{github_archive epics-extensions medm MEDM%{version}}
Source2:        https://epics.anl.gov/EpicsDocumentation/ExtensionsManuals/MEDM/medmfonts.ali.txt

BuildRequires:  epics-base, gcc-c++, make, perl
BuildRequires:  libX11-devel, libXft-devel, fontconfig-devel
BuildRequires:  libjpeg-devel, libpng-devel, motif-devel, dos2unix
Requires:       epics-base, libX11, libXft, motif
Requires:       fontconfig, libjpeg, libpng, xorg-x11-fonts-Type1
Requires:       xorg-x11-fonts-misc, xorg-x11-fonts-100dpi, xorg-x11-fonts-75dpi
Requires:       xorg-x11-fonts-ISO8859-1-100dpi, xorg-x11-fonts-ISO8859-1-75dpi

%description

%prep
%autosetup -n extensions
tar xpf %{S:1}
mv medm-MEDM%{version} src/medm

%build

%install
. %{_specdir}/fn-build.sh
sed -i '/^EPICS_BASE=/ s@=.*@=%{etop_base}@' configure/RELEASE
make %{?_smp_mflags} %{cmd_flags} DESTDIR=%{buildroot} \
	INSTALL_LOCATION=%{buildroot}%{etop_base} install ||
	make -j1 %{cmd_flags} DESTDIR=%{buildroot} \
		INSTALL_LOCATION=%{buildroot}%{etop_base} install
mkdir -p %{buildroot}/etc/profile.d; (
	echo 'EPICS_DISPLAY_PATH=%{etop_res}/adl'
	echo 'export EPICS_DISPLAY_PATH'; echo
) > %{buildroot}/etc/profile.d/epics-medm.sh
mkdir -p %{buildroot}%{etop_res}/misc
(echo; dos2unix < %{S:2}) > %{buildroot}%{etop_res}/misc/medmfonts.ali.txt
%_rm_extras; %_file_list %{epics_root} > epics.lst

%files -f epics.lst
%config(noreplace) /etc/profile.d/epics-medm.sh

%post
for name in /usr/share/X11/fonts/misc/fonts.alias \
	/usr/share/fonts/X11/misc/fonts.alias; do
	if [ -f "$name" ]; then
		sed -i '/^widgetDM/d' "$name"
		cat %{etop_res}/misc/medmfonts.ali.txt >> "$name"; break
	fi
done

