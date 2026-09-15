%{meta license=EPICS version=3_1_17,5}

Name:           epics-medm
Summary:        EPICS - Motif Editor and Display Manager
URL:            https://epics.anl.gov/extensions/medm/index.php
Source0:        https://epics.anl.gov/download/extensions/extensionsTop_20120904.tar.gz
Source1:        %{github_archive epics-extensions medm MEDM%{version}}

BuildRequires:  epics-base, gcc-c++, make, libX11-devel, motif-devel
Requires:       epics-base, libX11, motif
Requires:       xorg-x11-fonts-misc, xorg-x11-fonts-ISO8859-1-100dpi

%{inherit epics + global}
%description

%prep
%autosetup -n extensions
tar xpf %{S:1}
mv medm-MEDM%{version} src/medm

%build

%install
. %{_specdir}/fn-build.sh
sed -i '/^EPICS_BASE=/ s@=.*@=%{etop_base}@' configure/RELEASE
make -k %{?_smp_mflags} %{cmd_flags} DESTDIR=%{buildroot} \
	INSTALL_LOCATION=%{buildroot}%{etop_base} install ||
	make -j1 %{cmd_flags} DESTDIR=%{buildroot} \
		INSTALL_LOCATION=%{buildroot}%{etop_base} install
mkdir -p %{buildroot}/etc/profile.d; (
	echo 'EPICS_DISPLAY_PATH=%{etop_res}/adl'
	echo 'export EPICS_DISPLAY_PATH'; echo
) > %{buildroot}/etc/profile.d/epics-medm.sh
mkdir -p %{buildroot}%{etop_base}/medm
cp src/medm/medm/fonts.alias.sun %{buildroot}%{etop_base}/medm/fonts.alias
%_rm_extras; %_file_list %{epics_root} > epics.lst

%files -f epics.lst
%config(noreplace) /etc/profile.d/epics-medm.sh

%post
for name in /usr/share/X11/fonts/misc/fonts.alias \
	/usr/share/fonts/X11/misc/fonts.alias; do
	if [ -f "$name" ]; then
		sed -i '/^widgetDM/d' "$name"
		cat %{etop_base}/medm/fonts.alias >> "$name"; break
	fi
done

