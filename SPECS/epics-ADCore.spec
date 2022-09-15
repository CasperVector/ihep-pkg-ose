%define repo ADCore
%define commit R3-11
%define etop_ad %{epics_root}/areaDetector
%define opimask */arrayPlot.* edl/simTop.edl
%include %{_specdir}/classes/unbloat.spec
%{meta name license=MIT github=areaDetector version=commit,3}

Summary:        EPICS - areaDetector base classes and standard plugins
Patch0:         %{name}-3_11-bugs.patch
BuildRequires:  epics-ADSupport, epics-asyn, gcc-c++, make, libXext-devel
Requires:       epics-ADSupport, epics-asyn, epics-autosave, epics-busy
Requires:       epics-calc, epics-iocStats, epics-seq, epics-sscan, libXext

%description

%prep
%setup -c -n %{name}
. %{_specdir}/fn-build.sh
_mv_commit %{repo} %{commit}
cd %{repo}/iocBoot
cp EXAMPLE_commonPlugins.cmd commonPlugins.cmd
cp EXAMPLE_commonPlugin_settings.req commonPlugin_settings.req
cd ..; cat %{P:0} | patch -p1
cd ..; _mv_build %{repo} %{etop_ad}/%{repo}

%build
. %{_specdir}/fn-build.sh; cd %{etop_ad}/%{repo}
make %{?_smp_mflags} %{cmd_flags}

%install
. %{_specdir}/fn-build.sh; %_link_ops %{etop_ad}
_mv_dest %{etop_ad}/%{repo} %{buildroot}%{etop_ad}; %_mask_opi
%_rm_extras; %_file_list %{etop_ad}/%{repo} %{etop_res} > epics.lst

%files -f epics.lst

