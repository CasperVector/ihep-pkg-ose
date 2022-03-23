%define repo optics
%define commit R2-13-5

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - Monochromators, slits, mirrors, diffractometers etc

License:        EPICS Open License
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}
Patch0:         %{name}-2_13_5-app-libs.patch

BuildRequires:  epics-asyn, epics-autosave, epics-busy, epics-calc
BuildRequires:  epics-iocStats, epics-seq, gcc-c++, make
Requires:       epics-asyn, epics-autosave, epics-busy, epics-calc
Requires:       epics-iocStats, epics-seq

%description

%{inherit synapps - prep}

%{inherit synapps + prep}
mv iocBoot/iocAny iocBoot/iocOptics; cd iocBoot
%_iocboot_makefiles .; make %{?_smp_mflags}

