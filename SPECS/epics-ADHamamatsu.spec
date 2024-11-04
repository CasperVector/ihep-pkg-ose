%define repo ADHamamatsu
%define commit v20240710
%{meta name license=EPICS codeberg=CasperVector version=commit,1}

Summary:        EPICS - Driver for devices using the Hamamatsu DCAM API
Patch0:         %{name}-20221228-support.patch
BuildRequires:  hamamatsu-sdk
Requires:       hamamatsu-sdk

%{inherit ad + global deps}
%description

%{inherit ad - prep}

%{inherit ad + prep}
rm -rf %{repo}/*Support

