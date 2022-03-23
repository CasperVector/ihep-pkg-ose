%define repo camac
%define commit R2-7-4

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - CAMAC controllers and modules

License:        EPICS Open License
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}
Patch0:         %{name}-2_7_4-config.patch

BuildRequires:  epics-calc, epics-motor, epics-scaler, gcc-c++, make
Requires:       epics-calc, epics-motor, epics-scaler

%description

%{inherit synapps}

