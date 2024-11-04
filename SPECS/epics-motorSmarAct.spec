%define repo motorSmarAct
%define commit R1-2-1
%{meta name license=EPICS github=epics-motor version=commit,4}

Summary:        EPICS - SmarAct motion controllers

%{inherit motor + global deps}
%description

%{inherit motor}

