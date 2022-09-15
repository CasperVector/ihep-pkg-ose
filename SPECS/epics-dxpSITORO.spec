%define repo dxpSITORO
%define commit R1-2
%{meta name license=EPICS github=epics-modules version=commit,3}

Summary:        EPICS - XIA SITORO based FalconX spectrometers
Patch0:         %{name}-1_2-dynamic.patch
Patch1:         %{name}-1_2-files.patch
BuildRequires:  epics-ADCore, epics-mca, gcc-c++, make, libXext-devel
Requires:       epics-ADCore, epics-mca, libXext

%description

%{inherit synapps - prep}

%{inherit synapps + prep}
cd iocBoot/iocFalcon
cp ../iocFalconX4/Makefile .
cp ../iocFalconX4/*.ini dxp-4ch-4sca.ini
chmod 0755 *.sh
./dxp-chan.sh 4
./dxp-sca.sh 4

