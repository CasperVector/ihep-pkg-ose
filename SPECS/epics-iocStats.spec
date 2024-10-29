%define repo iocStats
%define commit 3.2.0
%{meta name license=EPICS github=epics-modules version=commit,1}

Summary:        EPICS - IOC status and control
Patch0:         %{name}-3.2.0-files.patch
BuildRequires:  epics-support, gcc-c++, make
Requires:       epics-support

%{inherit synapps + global}
%description

%{inherit synapps - prep}

%{inherit synapps + prep}
sed -i 's/(IOCNAME):/(IOCNAME)/g' iocAdmin/Db/*

