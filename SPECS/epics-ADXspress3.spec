%define repo ADXspress3
%define commit 20220318

Name:           epics-%{repo}
Version:        2_6
Release:        3.%{commit}
Summary:        EPICS - Xspress3 readout devices from Quantum Detectors

License:        LGPLv2+
URL:            https://github.com/CasperVector/%{repo}
Source0:        %{github_archive_ver CasperVector %{repo} %{commit} v}

BuildRequires:  epics-ADCore, gcc-c++, make, libXext-devel
Requires:       epics-ADCore, libXext

%description

%{inherit ad - prep}

%{inherit ad + prep}
cd xspress3IOC
sed -i '/iocAdminSoft/ s/)"/):"/' iocBoot/iocXsp3CARS_extra/*.cmd
sed -i '/DEVIOCSTATS/,/^}$/ s/)"/):"/' xspress3App/Db/*.substitutions

