%define repo StreamDevice
%define commit 2.8.16

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - Generic support for byte-stream based I/O

License:        LGPLv3+
URL:            https://github.com/paulscherrerinstitute/%{repo}
Source0:        %{github_archive paulscherrerinstitute %{repo} %{commit}}
Patch0:         %{name}-2.8.16-config-libs.patch

BuildRequires:  epics-asyn, epics-autosave, epics-iocStats, gcc-c++, make
Requires:       epics-asyn, epics-autosave, epics-iocStats

%description

%{inherit synapps - prep}

%{inherit synapps + prep}
rm -f GNUmakefile; cp %{epics_root}/utils/configure/RULES.ioc configure

