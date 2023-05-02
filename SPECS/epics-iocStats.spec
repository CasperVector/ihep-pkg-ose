%define repo iocStats
%define commit 3.1.16
%{meta name license=EPICS github=epics-modules version=commit,3}

Summary:        EPICS - IOC status and control
Patch0:         %{name}-3.1.16-files.patch
BuildRequires:  epics-seq, gcc-c++, make
Requires:       epics-seq

%{inherit synapps + global}
%description

%{inherit synapps - prep}

%{inherit synapps + prep}
sed -i 's/(IOCNAME):/(IOCNAME)/g' iocAdmin/Db/*

