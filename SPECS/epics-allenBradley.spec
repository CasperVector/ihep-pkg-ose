%define repo allenBradley
%define commit 2.3
%{meta name license=EPICS version=commit,3}

Summary:        EPICS - Allen Bradley driver and device support
URL:            https://epics.anl.gov/modules/bus/%{repo}/
Source0:        https://www.aps.anl.gov/epics/download/modules/%{repo}-%{commit}.tar.gz
Patch0:         %{name}-2.3-config.patch
BuildRequires:  epics-support, gcc-c++, make
Requires:       epics-support

%{inherit synapps + global}
%description

%{inherit synapps}

