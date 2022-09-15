%define repo StreamDevice
%define commit 2.8.16
%{meta name license=LGPLv3+ github=paulscherrerinstitute version=commit,3}

Summary:        EPICS - Generic support for byte-stream based I/O
Patch0:         %{name}-2.8.16-config-libs.patch
BuildRequires:  epics-asyn, epics-autosave, epics-calc, epics-iocStats
BuildRequires:  gcc-c++, make
Requires:       epics-asyn, epics-autosave, epics-calc, epics-iocStats

%description

%{inherit synapps - prep}

%{inherit synapps + prep}
rm -f GNUmakefile; cp %{epics_root}/utils/configure/RULES.ioc configure

