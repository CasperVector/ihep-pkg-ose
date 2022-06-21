%define repo ADXspress3
%define commit 20220318
%{meta name license=LGPLv3+ version=2_6,3.commit}

Summary:        EPICS - Xspress3 readout devices from Quantum Detectors
URL:            https://github.com/CasperVector/%{repo}
Source0:        %{github_archive_ver CasperVector %{repo} %{commit} v}

%{inherit ad + deps}
%description

%{inherit ad - prep}

%{inherit ad + prep}
cd xspress3IOC
sed -i '/iocAdminSoft/ s/)"/):"/' iocBoot/iocXsp3CARS_extra/*.cmd
sed -i '/DEVIOCSTATS/,/^}$/ s/)"/):"/' xspress3App/Db/*.substitutions

