%define repo Galil
%define repotail 3-0
%define commit 3-6
%{meta name license=EPICS version=commit,3}

Summary:        EPICS - Driver for Galil products based on asyn
URL:            https://github.com/motorapp/%{repo}-%{repotail}
Source0:        %{github_archive_ver motorapp %{repo}-%{repotail} %{commit} V}
BuildRequires:  epics-asyn, epics-autosave, epics-busy, epics-calc, epics-ipac
BuildRequires:  epics-motor, epics-seq, epics-sscan, gcc-c++, make
Requires:       epics-asyn, epics-autosave, epics-busy, epics-calc, epics-ipac
Requires:       epics-motor, epics-seq, epics-sscan

%{inherit synapps + global}
%description

%{inherit synapps - prep}

%prep
%setup -c -n %{name}
. %{_specdir}/fn-build.sh
_mv_commit %{repo} %{repotail}-%{commit}; cd %{repo}
mv %{commit}/* %{commit}/.ci-local .; rmdir %{commit}
cp config/GALILRELEASE configure/RELEASE.local; cd -
_mv_build %{repo} %{epics_root}/%{repo}; cd %{epics_root}
make release THIS_MODULE='$(SUPPORT)/%{repo}' MODULE_LIST=THIS_MODULE
cd %{repo}; %_my_patch

