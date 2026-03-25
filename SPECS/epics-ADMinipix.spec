%define repo ADMinipix
%define commit v20250604
%{meta name license=EPICS codeberg=CasperVector version=commit,2}

Summary:        EPICS - Minipix area detectors
ExclusiveArch:  x86_64

%{inherit ad + global deps}
%description

%{inherit ad + prep build}

%{inherit ad + install}
cd %{buildroot}%{etop_ad}/%{repo}
mkdir -p %{buildroot}/etc/udev/rules.d
install -m 0644 *Support/99-minipix.rules %{buildroot}/etc/udev/rules.d

%{inherit ad + files}
%config(noreplace) /etc/udev/rules.d/99-minipix.rules

