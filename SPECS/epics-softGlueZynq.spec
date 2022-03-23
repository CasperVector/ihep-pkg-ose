%define repo softGlueZynq
%define commit R2-0-4

Name:           epics-%{repo}
Version:        %(echo %{commit} | sed 's/^R//; s/-/_/g')
Release:        1
Summary:        EPICS - Rendition of softGlue for the Xilinx Zynq

License:        EPICS Open License
URL:            https://github.com/epics-modules/%{repo}
Source0:        %{github_archive epics-modules %{repo} %{commit}}

BuildRequires:  epics-asyn, epics-scaler, epics-seq, gcc-c++, make
Requires:       epics-asyn, epics-scaler, epics-seq

%description

%{inherit synapps}

