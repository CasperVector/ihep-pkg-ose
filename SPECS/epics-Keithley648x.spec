%define repo Keithley648x
%define commit 3731db83
%{meta name license=EPICS github=BCDA-APS version=commit,11}

Summary:        EPICS - Keithley 6485/7 picoammeters
Patch0:         %{name}-3731db83-libs-files.patch
BuildRequires:  epics-asyn, epics-autosave, epics-iocStats, gcc-c++, make
Requires:       epics-asyn, epics-autosave, epics-iocStats
Obsoletes:      epics-Keithley_648x

%{inherit synapps + global}
%description

%{inherit synapps - prep}

%prep
%setup -c -n %{name}
%_moreapps_prep

