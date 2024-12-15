%define repo ADSupport
%define commit R1-10
%define acommit R3-11
%{meta name license=MIT github=areaDetector}

Version:        %(echo %{commit}.%{acommit} | sed 's/\<R//g; s/-/_/g')
Release:        5.el%{rhel}
Summary:        EPICS - Support libraries for areaDetector
Source1:        %{github_archive areaDetector areaDetector %{acommit}}
Patch0:         %{name}-1_10-config.patch
BuildRequires:  epics-support, gcc-c++, make, libXext-devel
Requires:       epics-support, libXext

%{inherit epics + global}
%description

%prep
%setup -c -n %{name}
. %{_specdir}/fn-build.sh
_mv_commit %{repo} %{commit}
tar xpf %{S:1}; _mv_commit areaDetector %{acommit}
mv %{repo} areaDetector; cd areaDetector/configure
cp EXAMPLE_CONFIG_SITE.local CONFIG_SITE.local
cp EXAMPLE_RELEASE_PRODS.local RELEASE_PRODS.local
cp EXAMPLE_RELEASE_LIBS.local RELEASE_LIBS.local
cp EXAMPLE_RELEASE.local RELEASE.local
sed -i 's@$(TOP)/\.\./\.\./\.\.@%{epics_root}/areaDetector@' \
	RELEASE_PRODS_INCLUDE
cd ..; cat %{P:0} | patch -p1
cd ..; _mv_build areaDetector %{etop_ad}
cd %{epics_root}; make release MODULE_LIST=AREA_DETECTOR

%build
. %{_specdir}/fn-build.sh; cd %{etop_ad}/%{repo}
make %{?_smp_mflags} %{cmd_flags}

%install
. %{_specdir}/fn-build.sh; %_link_ops %{etop_ad}
_mv_dest %{etop_ad} %{buildroot}%{epics_root}
%_rm_extras; %_file_list %{etop_ad} > epics.lst

%files -f epics.lst

