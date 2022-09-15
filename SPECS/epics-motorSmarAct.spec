%define repo motorSmarAct
%define commit R1-2-1
%{meta name license=EPICS github=epics-motor version=commit,2}

Summary:        EPICS - SmarAct motion controllers

%{inherit motor + deps}
%description

%{inherit motor}

