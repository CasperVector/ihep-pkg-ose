%define repo softGlueZynq
%define commit R2-0-4
%{meta name license=EPICS github=epics-modules version=commit,3}

Summary:        EPICS - Rendition of softGlue for the Xilinx Zynq
BuildRequires:  epics-asyn, epics-scaler, epics-seq, gcc-c++, make
Requires:       epics-asyn, epics-scaler, epics-seq

%{inherit synapps + global}
%description

%{inherit synapps}

