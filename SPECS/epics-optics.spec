%define repo optics
%define commit R2-13-5
%define cmd_flags CMD_CFLAGS='%{optflags} -Wno-error=format-security' \\\
	CMD_CXXFLAGS='%{optflags} -Wno-error=format-security'
%{meta name license=EPICS github=epics-modules version=commit,3}

Summary:        EPICS - Monochromators, slits, mirrors, diffractometers etc
Patch0:         %{name}-2_13_5-app-libs.patch
BuildRequires:  epics-asyn, epics-autosave, epics-busy, epics-calc
BuildRequires:  epics-iocStats, epics-seq, gcc-c++, make
Requires:       epics-asyn, epics-autosave, epics-busy, epics-calc
Requires:       epics-iocStats, epics-seq

%{inherit synapps + global}
%description

%{inherit synapps - prep}

%{inherit synapps + prep}
mv iocBoot/iocAny iocBoot/iocOptics; cd iocBoot
%_iocboot_makefiles .; make %{?_smp_mflags}

