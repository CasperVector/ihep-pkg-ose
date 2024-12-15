%define repo ADKinetix
%define commit R1-0
%{meta name license=EPICS github=NSLS-II version=commit,2}

Summary:        EPICS - PVCam driver with full Kinetix support
Patch0:         %{name}-1_0-support.patch
Patch1:         %{name}-1_0-glitches.patch
Patch2:         %{name}-1_0-serial.patch
BuildRequires:  pvcam-sdk
Requires:       pvcam-sdk

%{inherit ad + global deps}
%description

%{inherit ad - prep}

%{inherit ad + prep}
rm -rf %{repo}/*Support

