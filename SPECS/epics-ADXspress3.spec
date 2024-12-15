%define repo ADXspress3
%define commit 20250201
%define cmd_flags CMD_CFLAGS='%{optflags} -Wno-error=format-security' \\\
	CMD_CXXFLAGS='%{optflags} -Wno-error=format-security'
%{meta name license=LGPLv3+ version=3.2.8,1.commit}

Summary:        EPICS - Xspress3 readout devices from Quantum Detectors
URL:            https://codeberg.org/CasperVector/%{repo}
Source0:        %{codeberg_archive CasperVector %{repo} v%{commit}}

%{inherit ad + global deps}
%description

%{inherit ad - prep}

%{inherit ad + prep}
cd xspress3IOC
sed -i '/iocAdminSoft/ s/)"/):"/' iocBoot/iocXsp3CARS_extra/*.cmd
sed -i '/DEVIOCSTATS/,/^}$/ s/)"/):"/' xspress3App/Db/*.substitutions

