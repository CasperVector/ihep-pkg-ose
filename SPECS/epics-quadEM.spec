%define repo quadEM
%define commit R9-4

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - Quad electrometers and picoammeters

License:        EPICS Open License
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}

BuildRequires:  epics-ADCore, epics-ipac, epics-ipUnidig
BuildRequires:  gcc-c++, make, libXext-devel
Requires:       epics-ADCore, epics-ipac, epics-ipUnidig, libXext

%description

%{inherit synapps}

