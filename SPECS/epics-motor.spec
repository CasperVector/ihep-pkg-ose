%define repo motor
%define commit R7-2-2

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - Core motor support

License:        EPICS Open License
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}
Patch0:         %{name}-7_2_2-config-libs.patch
Patch1:         %{name}-7_2_2-bugs.patch

BuildRequires:  epics-asyn, epics-busy, epics-seq, gcc-c++, make
Requires:       epics-asyn, epics-busy, epics-seq
Requires:       epics-autosave, epics-iocStats

%description

%{inherit synapps}

