%define repo ADAravis
%define commit R2-2-1
%{meta name license=EPICS github=areaDetector version=commit,6}

Summary:        EPICS - GenICam cameras using the Aravis library
Patch0:         %{name}-1_2-files.patch
Patch1:         %{name}-1_2-gerror.patch
BuildRequires:  epics-ADGenICam, aravis
Requires:       epics-ADGenICam, aravis

%{inherit ad + global deps}
%description

%{inherit ad}

