%define repo seq
%define commit 2.2.9
%{meta name license=EPICS version=commit,1}

Summary:        EPICS - SNL compiler and runtime sequencer
URL:            https://www-csr.bessy.de/control/SoftDist/sequencer
Source0:        %{url}/releases/%{repo}-%{commit}.tar.gz
BuildRequires:  epics-support, gcc-c++, make, re2c
Requires:       epics-support

%description

%{inherit synapps}

