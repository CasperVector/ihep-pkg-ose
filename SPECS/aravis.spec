Name:           aravis
Version:        0.8.20
Release:        3.el%{rhel}
Summary:        Glib/gobject based library implementing a GenICam interface

License:        GPLv2+
URL:            https://github.com/AravisProject/%{name}
Source0:        %{github_archive AravisProject %{name} %{version}}

BuildRequires:  gcc, gcc-c++, meson, gettext, intltool, glib2-devel
BuildRequires:  libxml2-devel, libusbx-devel, gtk3-devel, libnotify-devel
BuildRequires:  gstreamer1-devel, gstreamer1-plugins-base-devel
Requires:       glib2-devel, libusbx-devel, libxml2-devel

%description

%package -n %{name}-gui
Summary:        GUI components of %{name}
Requires:       %{name}, gstreamer1, gstreamer1-plugins-base, gtk3, libnotify

%description -n %{name}-gui

%prep
%autosetup
sed -i 's/MODE:="0666"/GROUP="video", MODE:="0660"/' src/aravis.rules

%build
meson setup --prefix=/usr -Dusb=enabled -Dviewer=enabled \
	-Dpacket-socket=enabled -Dfast-heartbeat=true -Dgst-plugin=disabled \
	-Ddocumentation=disabled -Dintrospection=disabled -Dtests=false build
ninja -C build

%install
%ninja_install -C build
mkdir -p %{buildroot}/etc/udev/rules.d
install -m 0644 src/aravis.rules \
	%{buildroot}/etc/udev/rules.d/99-aravis-cameras.rules
rm -rf %{buildroot}%{_mandir}/*/*

%files
%caps(cap_net_raw=ep) %{_bindir}/arv-tool*
%{_bindir}/arv-camera-test*
%{_bindir}/arv-fake-gv-camera*
%{_bindir}/arv-test*
%{_libdir}/lib*
%{_libdir}/pkgconfig/*
%{_includedir}/*
%{_datadir}/locale/*/LC_MESSAGES/*.mo
%config(noreplace) /etc/udev/rules.d/*.rules

%files -n %{name}-gui
%{_bindir}/arv-viewer*
%{_datadir}/icons/hicolor/*/apps/*.png
%{_datadir}/applications/*.desktop
%{_datadir}/metainfo/*.appdata.xml

