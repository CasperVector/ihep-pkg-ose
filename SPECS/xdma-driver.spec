%define repo dma_ip_drivers
%define commit d66f224c

Name:           xdma-driver
Version:        20240528
Release:        1.%{commit}.el%{rhel}
Summary:        Xilinx DMA IP Reference drivers

License:        GPLv2
URL:            https://github.com/Xilinx/%{repo}
Source0:        %{github_archive Xilinx %{repo} %{commit}}
Patch0:         %{name}-20240528-files.patch
Requires:       kernel-devel
%if %{rhel} == 8
Requires:       elfutils-libelf-devel
%endif

%description

%prep
%setup -c -n %{name}
. %{_specdir}/fn-build.sh
_mv_commit %{repo} %{commit}
cd %{repo}; patch -p1 < %{P:0}; cd XDMA/linux-kernel
mv COPYING LICENSE RELEASE readme.txt ../../..

%install
. %{_specdir}/fn-build.sh
cd %{buildroot}; mkdir -p .%{_bindir} etc/udev/rules.d var/xdma; cd -
cd %{repo}; install -m 0755 xdma-module-* %{buildroot}%{_bindir}
install -m 0644 99-xdma.rules %{buildroot}/etc/udev/rules.d
cp -r XDMA/linux-kernel %{buildroot}/var/xdma/module
cd -; %_file_list /usr /var > noetc.lst

%files -f noetc.lst
%config(noreplace) /etc/udev/rules.d/*.rules
%doc COPYING LICENSE RELEASE readme.txt

