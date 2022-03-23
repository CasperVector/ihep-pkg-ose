%define repo std
%define commit R3-6-3
%define opimask */arrayPlot.*

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - epid and throttle records

License:        EPICS Open License
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}

BuildRequires:  epics-asyn, epics-seq, gcc-c++, make
Requires:       epics-asyn, epics-seq

%description

%{inherit synapps}

