%prep
%setup -c -n %{name}
%_moreapps_prep
cd ..; _mv_build %{repo} %{epics_root}/%{repo}

