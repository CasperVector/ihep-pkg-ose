%define repo ip
%define commit R2-21-1

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - Misc devices dating back to Industry Pack cards

License:        EPICS Open License
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}
Patch0:         %{name}-2_21_1-app-libs-files.patch

BuildRequires:  epics-asyn, epics-autosave, epics-iocStats
BuildRequires:  epics-ipac, epics-seq, gcc-c++, make
Requires:       epics-asyn, epics-autosave, epics-iocStats
Requires:       epics-ipac, epics-seq

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

