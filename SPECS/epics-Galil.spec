%define repo Galil
%define repotail 3-0
%define commit 3-6
%{meta name license=EPICS version=commit,4}

Summary:        EPICS - Driver for Galil products based on asyn
URL:            https://github.com/motorapp/%{repo}-%{repotail}
Source0:        https://github.com/motorapp/%{repo}-%{repotail}/archive/V%{commit}/%{repo}-%{commit}.tar.gz
BuildRequires:  epics-asyn, epics-autosave, epics-busy, epics-calc, epics-ipac
BuildRequires:  epics-motor, epics-seq, epics-sscan, gcc-c++, make
Requires:       epics-asyn, epics-autosave, epics-busy, epics-calc, epics-ipac
Requires:       epics-motor, epics-seq, epics-sscan

%{inherit synapps + global}
%description

%{inherit synapps - prep}

%prep
%setup -c -n %{name}
. %{_specdir}/fn-build.sh; _mv_commit %{repo} %{commit}
cd %{repo}; mv %{commit}/* %{commit}/.ci-local .; rmdir %{commit}
cp config/GALILRELEASE configure/RELEASE.local; cd -
_mv_build %{repo} %{epics_root}/%{repo}; cd %{epics_root}
make release MOD_='$(SUPPORT)/%{repo}' MODULE_LIST=MOD_
cd %{repo}; %_my_patch

