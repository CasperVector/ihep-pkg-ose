%define repo iocStats
%define commit 3.1.16

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - IOC status and control

License:        EPICS Open License
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}
Patch0:         %{name}-3.1.16-files.patch

BuildRequires:  epics-seq, gcc-c++, make
Requires:       epics-seq

%description

%{inherit synapps - prep}

%{inherit synapps + prep}
sed -i 's/(IOCNAME):/(IOCNAME)/g' iocAdmin/Db/*

