%define repo asyn
%define commit R4-42
%{meta name license=EPICS github=epics-modules version=commit,2}

Summary:        EPICS - Generic-purpose interfacing to lower level
Patch0:         %{name}-4_42-files.patch
%if %{rhel} == 8
Patch1:         %{name}-4_42-rocky8.patch
%endif
BuildRequires:  epics-ipac, epics-seq, gcc-c++, make
Requires:       epics-ipac, epics-seq
%if %{rhel} == 8
BuildRequires:  libtirpc-devel, rpcgen
%endif

%description

%{inherit synapps}

