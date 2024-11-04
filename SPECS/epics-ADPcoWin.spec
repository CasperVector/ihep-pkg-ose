%define repo ADPcoWin
%define commit R6-0
%{meta name license=Apache github=areaDetector version=commit,1}

Summary:        EPICS - areaDetector driver for PCO cameras
Patch0:         %{name}-6_0-build.patch
Patch1:         %{name}-6_0-linux.patch
BuildRequires:  pco-sdk
Requires:       pco-sdk

%{inherit ad + global deps}
%description

%{inherit ad - prep}

%{inherit ad + prep}
cd %{repo}/pcowinApp/src; rm -rf dll64 lib64 include
grep -rl 'unsigned long' . | xargs sed -i 's/unsigned long/DWORD/g'

