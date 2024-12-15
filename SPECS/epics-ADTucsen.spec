%define repo ADTucsen
%define commit v20241203
%define cmd_flags CMD_CXXFLAGS='%{optflags} -Wno-write-strings'
%{meta name license=EPICS codeberg=CasperVector version=commit,1}

Summary:        EPICS - Tucsen cameras with the TUCam API

%{inherit ad + global deps}
%description

%{inherit ad + prep}

%{inherit ad + build}
cd %{epics_root}/"$(cat ioc.lst)"/iocBoot/ioc*
ln -s %{etop_ad}/%{repo}/*Support/os/%{epics_arch}/*.cti .

%{inherit ad + install}
cd %{buildroot}%{etop_ad}/%{repo}
mkdir -p %{buildroot}/etc/tucam
install -m 0644 *Support/tuusb.conf %{buildroot}/etc/tucam

%{inherit ad + files}
/etc/tucam/tuusb.conf

