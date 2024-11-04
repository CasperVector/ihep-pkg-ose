%define repo usb220
%define commit v20240722
%{meta name license=EPICS codeberg=CasperVector version=commit,1}

Summary:        EPICS - FUTEK USB220 devices
Patch0:         %{name}-20230418-libs.patch
BuildRequires:  epics-asyn, epics-autosave, epics-iocStats
BuildRequires:  gcc-c++, make, libusbx-devel
Requires:       epics-asyn, epics-autosave, epics-iocStats, libusbx

%{inherit synapps + global}
%description

%{inherit synapps + prep}

%{inherit synapps + build}
sup=$(echo *Sup)
for name in GetDeviceInformation GetReadings; do
	g++ -std=c++11 -Wall -o bin/%{epics_arch}/"$name" \
		"$sup"/examples/"$name"/main.cpp -lFUTEK_USB -lftd2xx \
		-lusb-1.0 -lpthread -I"$sup" -L "$sup"/os/%{epics_arch} \
		-Wl,-rpath,"$PWD/$sup"/os/%{epics_arch}; done

%{inherit synapps + install}
cd %{buildroot}%{epics_root}/%{repo}
mkdir -p %{buildroot}/etc/udev/rules.d
install -m 0644 *Sup/*-FUTEKUSB.rules %{buildroot}/etc/udev/rules.d

%{inherit synapps + files}
%config(noreplace) /etc/udev/rules.d/*-FUTEKUSB.rules

