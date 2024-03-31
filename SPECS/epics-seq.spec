%define repo seq
%define myrepo sequencer-mirror
%define commit R2-2-9
%{meta name license=EPICS version=commit,4}

Summary:        EPICS - SNL compiler and runtime sequencer
URL:            https://epics-modules.github.io/sequencer/
Source0:        %{github_archive mdavidsaver %{myrepo} %{commit}}
BuildRequires:  epics-support, gcc-c++, make, re2c
Requires:       epics-support

%{inherit synapps + global}
%description

%{inherit synapps - prep}

%prep
%setup -c -n %{name}
. %{_specdir}/fn-build.sh
_mv_commit %{myrepo} %{commit}; mv %{myrepo} %{repo}
_mv_build %{repo} %{epics_root}/%{repo}; cd %{epics_root}
make release MOD_='$(SUPPORT)/%{repo}' MODULE_LIST=MOD_
cd %{repo}; %_my_patch

