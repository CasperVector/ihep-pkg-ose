%define repo support
%define commit R6-2-1
%define xcommit R6-2-1
%define icommit R2-21-1
%include %{_specdir}/classes/unbloat.spec
%{meta name license=EPICS github=EPICS-synApps version=commit,1}

Summary:        EPICS - synApps support files
Source1:        %{github_archive epics-modules xxx %{xcommit}}
Source2:        %{github_archive epics-modules ip %{icommit}}
Source3:        %{name}-6_2_1.release
BuildRequires:  epics-base, make
Requires:       epics-base

%description

%prep
%setup -c -n %{name}
. %{_specdir}/fn-build.sh
_mv_commit %{repo} %{commit}
tar xpf %{S:1}; _mv_commit xxx %{xcommit}
tar xpf %{S:2}; _mv_commit ip %{icommit}

%build
cp xxx/xxxApp/src/xxxMain.c %{repo}/utils/appMain.c
cp xxx/xxxApp/Makefile %{repo}/utils/app.mk
cp xxx/iocBoot/Makefile %{repo}/utils/iocBoot.mk
cp xxx/iocBoot/iocxxx/Makefile %{repo}/utils/ioc.mk
cp -r xxx/configure %{repo}/utils
cp ip/configure/RELEASE %{repo}/utils/configure/RELEASE
grep -rl '\<DXPSITORO\>' | xargs sed -i 's/\<DXPSITORO\>/DXP_SITORO/g'
sed 's,@epics_root@,%{epics_root},g; s,@etop_base@,%{etop_base},g' \
	< %{S:3} > %{repo}/configure/RELEASE
%_chown_me %{epics_root}; mv %{repo}/* %{epics_root}; cd %{epics_root}
perl -CSD ./configure/makeReleaseConsistent.pl \
	%{epics_root} %{etop_base} configure/RELEASE utils/configure/RELEASE
sed -ri '/ASYN/ s/^/#/; /IPAC|SNCSEQ/ d' utils/configure/RELEASE
make %{?_smp_mflags} MODULE_LIST=

%install
. %{_specdir}/fn-build.sh
%_mv_me %{epics_root}; %_do_rm_patch
%_file_list %{epics_root} > epics.lst

%files -f epics.lst

