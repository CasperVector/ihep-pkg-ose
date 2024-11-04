%define repo ADMinipix
%define commit v20230918
%{meta name license=EPICS codeberg=CasperVector version=commit,1}

Summary:        EPICS - Minipix area detectors
ExclusiveArch:  x86_64

%{inherit ad + global deps}
%description

%{inherit ad - prep}

%{inherit ad + prep}
sed -i 's/libudev\.so\.0/libudev\.so\.1/' \
	%{repo}/minipixSupport/os/%{epics_arch}/libokFrontPanel.so

