%define repo Yokogawa_DAS
%define commit R2-0-1

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - Yokogawa GM10 and MW100

License:        EPICS Open License
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}

BuildRequires:  epics-support, gcc-c++, make
Requires:       epics-support

%description

%{inherit synapps}

