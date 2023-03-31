%define repo ADEiger
%define commit R3-4
%{meta name license=GPLv2 github=areaDetector version=commit,3}

Summary:        EPICS - Dectris Eiger pixel-array detector
Patch0:         %{name}-3_4-dynamic.patch
BuildRequires:  zeromq-devel
Requires:       zeromq

%{inherit ad + deps}
%description

%{inherit ad}

