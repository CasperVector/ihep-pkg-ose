%define repo dxp
%define commit R6-0

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - DSP-based multi-channel analysers from XIA

License:        EPICS Open License
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}

BuildRequires:  epics-ADCore, epics-mca
BuildRequires:  gcc-c++, make, libXext-devel, libusb-devel
Requires:       epics-ADCore, epics-mca, libXext, libusb

%description

%{inherit synapps}

