%define repo calc
%define commit R3-7-4

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - [as]Calcout and transform records

License:        EPICS Open License
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}
Patch0:         %{name}-3_7_4-config.patch

BuildRequires:  epics-seq, gcc-c++, make
Requires:       epics-seq

%description

%{inherit synapps}

