%define repo sscan
%define commit R2-11-5
%define opimask */arrayPlot.*
%{meta name license=EPICS github=epics-modules version=commit,2}

Summary:        EPICS - sscan record and related software
Patch0:         %{name}-2_11_4-app-libs-files.patch
BuildRequires:  epics-autosave, epics-calc, epics-iocStats, gcc-c++, make
Requires:       epics-autosave, epics-calc, epics-iocStats

%description

%{inherit synapps - prep}

%{inherit synapps + prep}
chmod 0755 iocBoot/iocSscan/st.cmd
mv documentation/saveData.req iocBoot/iocSscan
cd iocBoot; %_iocboot_makefiles .; make %{?_smp_mflags}

