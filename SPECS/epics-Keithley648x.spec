%define repo Keithley648x
%define commit 3731db83

Name:           epics-%{repo}
Version:        0
Release:        8.%{commit}
Summary:        EPICS - Keithley 6485/7 picoammeters

License:        EPICS Open License
URL:            https://github.com/BCDA-APS/%{repo}
Source0:        %{github_archive BCDA-APS %{repo} %{commit}}
Patch0:         %{name}-3731db83-libs-files.patch

BuildRequires:  epics-autosave, epics-asyn, epics-iocStats, gcc-c++, make
Requires:       epics-autosave, epics-asyn, epics-iocStats
Obsoletes:      epics-Keithley_648x

%description

%{inherit synapps - prep}
%{inherit moreapps + prep}

