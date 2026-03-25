%define repo support
%define commit R6-2-1
%define icommit R2-21-1
%{meta name license=EPICS github=EPICS-synApps version=commit,4}

Summary:        EPICS - synApps support files
Source1:        %{github_archive epics-modules ip %{icommit}}
Source2:        %{name}-6_2_1.release
Source3:        %{name}-sup.mk
Patch0:         %{name}-6_2_1-mingw.patch
BuildRequires:  epics-base, make
Requires:       epics-base

%{inherit epics + global}
%description

%prep
%setup -c -n %{name}
. %{_specdir}/fn-build.sh
_mv_commit %{repo} %{commit}
tar xpf %{S:1}; _mv_commit ip %{icommit}
cd %{repo}; patch -p1 < %{P:0}

%build
basetop=%{etop_base}/templates/makeBaseApp/top
mkdir -p %{repo}/utils/exampleIOC/exampleSup \
	%{repo}/utils/exampleIOC/exampleApp/src \
	%{repo}/utils/exampleIOC/iocBoot/iocExample
install -m 0644 %{S:3} %{repo}/utils/exampleIOC/exampleSup/Makefile
cp -r "$basetop"/configure %{repo}/utils/exampleIOC
cp ip/configure/CONFIG_SITE ip/configure/RELEASE \
	%{repo}/utils/exampleIOC/configure
cp "$basetop"/Makefile %{repo}/utils/exampleIOC
cp "$basetop"/exampleApp/Makefile %{repo}/utils/exampleIOC/exampleApp
cp "$basetop"/exampleApp/src/_APPNAME_Main.cpp \
	%{repo}/utils/exampleIOC/exampleApp/src/exampleMain.c
cp "$basetop"/iocBoot/Makefile %{repo}/utils/exampleIOC/iocBoot
sed 's/$(EPICS_HOST_ARCH)/%{epics_arch}/' \
	< "$basetop"/iocBoot/ioc/Makefile@Common \
	> %{repo}/utils/exampleIOC/iocBoot/iocExample/Makefile
grep -rl '\<DXPSITORO\>' | xargs sed -i 's/\<DXPSITORO\>/DXP_SITORO/g'
sed 's,@epics_root@,%{epics_root},g; s,@etop_base@,%{etop_base},g' \
	< %{S:2} > %{repo}/configure/RELEASE
%_chown_me %{epics_root}; mv %{repo}/* %{epics_root}; cd %{epics_root}
perl -CSD ./configure/makeReleaseConsistent.pl \
	%{epics_root} %{etop_base} configure/RELEASE \
	utils/exampleIOC/configure/RELEASE
chmod 0644 utils/exampleIOC/configure/RELEASE
sed -ri '/ASYN/ s/^/#/; /IPAC|SNCSEQ/ d' utils/exampleIOC/configure/RELEASE
make %{?_smp_mflags} MODULE_LIST=

%install
. %{_specdir}/fn-build.sh
%_mv_me %{epics_root}; %_do_rm_patch
%_file_list %{epics_root} > epics.lst

%files -f epics.lst

