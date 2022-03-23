%define repo asyn
%define commit R4-42

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - Generic-purpose interfacing to lower level

License:        EPICS Open License
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}
Patch0:         %{name}-4_42-files.patch

BuildRequires:  epics-ipac, epics-seq, gcc-c++, make
Requires:       epics-ipac, epics-seq

%description

%{inherit synapps}

