%define repo autosave
%define commit R5-10-2
%{meta name license=EPICS github=epics-modules version=commit,3}

Summary:        EPICS - Automatic save/restore of PVs
Patch0:         %{name}-5_10_2-files.patch
BuildRequires:  epics-support, gcc-c++, make
Requires:       epics-support

%{inherit synapps + global}
%description

%{inherit synapps}

