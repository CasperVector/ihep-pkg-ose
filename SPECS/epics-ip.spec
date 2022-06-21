%define repo ip
%define commit R2-21-1
%{meta name license=EPICS github=epics-modules version=commit,2}

Summary:        EPICS - Misc devices dating back to Industry Pack cards
Patch0:         %{name}-2_21_1-app-libs-files.patch
BuildRequires:  epics-asyn, epics-autosave, epics-calc
BuildRequires:  epics-iocStats, epics-ipac, epics-seq, gcc-c++, make
Requires:       epics-asyn, epics-autosave, epics-calc
Requires:       epics-iocStats, epics-ipac, epics-seq

%description

%{inherit synapps - prep}

%{inherit synapps + prep}
mv iocs/ipExample/ipExampleApp/src/ipExampleInclude.dbd \
	ipApp/src/ipAppInclude.dbd
mv iocs/ipExample/iocBoot .; rm -rf iocs
mv iocBoot/iocIpExample iocBoot/iock2kdmm
chmod 0755 iocBoot/ioc*/st.cmd
for d in iocBoot/ioc*/; do [ -f "$d"/Makefile ] ||
	cp %{epics_root}/utils/ioc.mk "$d"/Makefile; done
cd iocBoot; make %{?_smp_mflags}

