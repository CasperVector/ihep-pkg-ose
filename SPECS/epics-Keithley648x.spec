%define repo Keithley648x
%define commit 3731db83
%{meta name license=EPICS github=BCDA-APS version=0,9.commit}

Summary:        EPICS - Keithley 6485/7 picoammeters
Patch0:         %{name}-3731db83-libs-files.patch
BuildRequires:  epics-autosave, epics-asyn, epics-iocStats, gcc-c++, make
Requires:       epics-autosave, epics-asyn, epics-iocStats
Obsoletes:      epics-Keithley_648x

%description

%{inherit synapps - prep}
%{inherit moreapps + prep}

