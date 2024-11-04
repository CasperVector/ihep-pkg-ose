%define repo motorOmsAsyn
%define commit R1-0-2
%{meta name license=EPICS github=epics-motor version=commit,4}

Summary:        EPICS - OMS motion controllers via asyn

%{inherit motor + global deps}
%description

%{inherit motor}

