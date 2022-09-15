%define repo softGlue
%define commit R2-8-3
%{meta name license=EPICS github=epics-modules version=commit,2}

Summary:        EPICS - Construct small, simple, digital electronic circuits
BuildRequires:  epics-asyn, epics-ipac, gcc-c++, make
Requires:       epics-asyn, epics-ipac

%description

%{inherit synapps}

