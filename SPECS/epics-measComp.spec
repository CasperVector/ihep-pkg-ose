%define repo measComp
%define commit R3-0

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - USB and ethernet I/O modules from Measurement Computing

License:        EPICS Open License
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}

BuildRequires:  epics-asyn, epics-autosave, epics-busy, epics-calc
BuildRequires:  epics-mca, epics-scaler, epics-seq, epics-sscan
BuildRequires:  gcc-c++, make, libusbx-devel, hidapi-devel
Requires:       epics-asyn, epics-autosave, epics-busy, epics-calc
Requires:       epics-mca, epics-scaler, epics-seq, epics-sscan, libusbx, hidapi

%description

%{inherit synapps}

