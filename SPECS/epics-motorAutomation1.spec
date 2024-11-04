%define repo motorAutomation1
%define commit ced3bee2
%define mdkver 2.5.1
%{meta name license=EPICS github=epics-motor version=commit,2}

Summary:        EPICS - Aerotech Automation1 motion controllers
ExclusiveArch:  x86_64
# Extracted from Automation1-MDKSetup-x.x.x.exe.
Source1:        %{dist_srv}/Automation1-APIs-%{mdkver}.tar.gz
Patch0:         %{name}-ced3bee2-config.patch
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

