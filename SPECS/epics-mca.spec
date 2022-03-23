%define repo mca
%define commit R7-9

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - Multi-channel analysers and multi-channel scalers

License:        EPICS Open License
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}
Patch0:         %{name}-7_9-scaler.patch

BuildRequires:  epics-asyn, epics-autosave, epics-busy, epics-calc, epics-scaler
BuildRequires:  epics-seq, epics-sscan, gcc-c++, make, libusbx-devel
Requires:       epics-asyn, epics-autosave, epics-busy, epics-calc, epics-scaler
Requires:       epics-seq, epics-sscan, libusbx

%description

%{inherit synapps}

