%define repo ADUVC
%define commit 0aa7bbfe
%{meta name license=XFree86 github=areaDetector version=commit,2}

Summary:        EPICS - USB Video Class (UVC) devices
Patch0:         %{name}-0aa7bbfe-config.patch
BuildRequires:  libusbx-devel
Requires:       libusbx

%{inherit ad + deps}
%description

%{inherit ad - build}

%{inherit ad + build}
cd %{etop_ad}/%{repo}/*Support/cameraDetector
mkdir -p %{etop_ad}/%{repo}/bin/%{epics_arch}
make %{?_smp_mflags}; mv uvc_locater %{etop_ad}/%{repo}/bin/%{epics_arch}

