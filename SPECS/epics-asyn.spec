%define repo asyn
%define commit R4-44-2
%{meta name license=EPICS github=epics-modules version=commit,1}

Summary:        EPICS - Generic-purpose interfacing to lower level
Patch0:         %{name}-4_44_2-bugs-files.patch
Patch1:         %{name}-4_44_2-centos7.patch
Patch2:         %{name}-4_44_2-usbtmc.patch
%if %{rhel} == 8
Patch3:         %{name}-4_42-rocky8.patch
%endif
BuildRequires:  epics-ipac, epics-seq, gcc-c++, make, libusbx-devel
Requires:       epics-ipac, epics-seq, libusbx
%if %{rhel} == 8
BuildRequires:  libtirpc-devel, rpcgen
%endif

%{inherit synapps + global}
%description

%{inherit synapps - prep}

%{inherit synapps + prep}
rm configure/CONFIG_SITE.*
sed -i -e 's@^#EPICS_BASE=.*@EPICS_BASE=%{etop_base}@' \
	-e 's@^#SUPPORT=.*@SUPPORT=%{epics_root}@' configure/RELEASE

