%define repo motorAutomation1
%define commit R1-0
%define mdkver 2.12.1
%{meta name license=EPICS github=epics-motor version=commit,1}

Summary:        EPICS - Aerotech Automation1 motion controllers
ExclusiveArch:  x86_64
# Extracted from Automation1-MDKSetup-x.x.x.exe.
Source1:        %{dist_srv}/Automation1-APIs-%{mdkver}.tar.gz
Patch0:         %{name}-1_0-config.patch
Patch1:         %{name}-1_0-exec.patch
BuildRequires:  libsodium-devel
Requires:       libsodium

%{inherit motor + global deps}
%description

%{inherit motor - prep}

%{inherit motor + prep}
tar xpf %{S:1}
mkdir %{repo}/automation1Sup/Library
mv Automation1-APIs-*/C/Include %{repo}/automation1Sup
mv Automation1-APIs-*/C/Library/Linux %{repo}/automation1Sup/Library
chmod 0755 "$(cat ioc.lst)"/iocBoot/iocAutomation1/reset.sh

