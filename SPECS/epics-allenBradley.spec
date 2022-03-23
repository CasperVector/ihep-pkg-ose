%define repo allenBradley
%define commit 2.3

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - Allen Bradley driver and device support

License:        EPICS Open License
URL:            https://epics.anl.gov/modules/bus/%{repo}/
Source0:        https://www.aps.anl.gov/epics/download/modules/%{repo}-%{commit}.tar.gz
Patch0:         %{name}-2.3-config.patch

BuildRequires:  epics-support, gcc-c++, make
Requires:       epics-support

%description

%{inherit synapps}

