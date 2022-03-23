%build
. %{_specdir}/fn-build.sh
cd %{epics_root}/%{repo}
make %{?_smp_mflags} %{cmd_flags}

