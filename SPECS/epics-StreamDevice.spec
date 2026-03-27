%define repo StreamDevice
%define commit 2.8.16
%{meta name license=LGPLv3+ github=paulscherrerinstitute version=commit,6}

Summary:        EPICS - Generic support for byte-stream based I/O
Patch0:         %{name}-2.8.16-config-libs.patch
Patch1:         %{name}-2.8.16-bugs.patch
BuildRequires:  epics-asyn, epics-autosave, epics-busy
BuildRequires:  epics-calc, epics-iocStats, gcc-c++, make, pcre-devel
Requires:       epics-asyn, epics-autosave, epics-busy
Requires:       epics-calc, epics-iocStats, pcre

%{inherit synapps + global}
%description

%{inherit synapps - prep}

%{inherit synapps + prep}
rm -f GNUmakefile
cp %{epics_root}/utils/exampleIOC/configure/RULES.ioc configure
sed -i 's@/usr/lib64@%{_libdir}@' configure/RELEASE

