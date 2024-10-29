%define repo ADUVC
%define commit 0aa7bbfe
%{meta name license=XFree86 github=areaDetector version=commit,4}

Summary:        EPICS - USB Video Class (UVC) devices
Patch0:         %{name}-0aa7bbfe-config.patch
BuildRequires:  libusbx-devel
Requires:       libusbx

%{inherit ad + global deps}
%description

%{inherit ad + prep}
mv %{repo}/99-uvc.rules .

%{inherit ad + build}
cd %{etop_ad}/%{repo}/*Support/cameraDetector
mkdir -p %{etop_ad}/%{repo}/bin/%{epics_arch}
make %{?_smp_mflags}; mv uvc_locater %{etop_ad}/%{repo}/bin/%{epics_arch}

%{inherit ad + install}
mkdir -p %{buildroot}/etc/udev/rules.d
install -m 0644 99-uvc.rules %{buildroot}/etc/udev/rules.d

%{inherit ad + files}
%config(noreplace) /etc/udev/rules.d/99-uvc.rules

