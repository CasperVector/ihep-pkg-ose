%define repo Keithley648x
%define commit 6a27b019
%{meta name license=EPICS github=BCDA-APS version=20201031,1.commit}

Summary:        EPICS - Keithley 6485/7 picoammeters
Patch0:         %{name}-6a27b019-libs-files.patch
BuildRequires:  epics-asyn, epics-autosave, epics-iocStats, gcc-c++, make
Requires:       epics-asyn, epics-autosave, epics-iocStats
Obsoletes:      epics-Keithley_648x

%{inherit synapps + global}
%description

%{inherit synapps - prep}

%prep
%setup -c -n %{name}
%_moreapps_prep

