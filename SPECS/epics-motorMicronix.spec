%define repo motorMicronix
%define commit R1-0-1
%{meta name license=EPICS github=epics-motor version=commit,1}

Summary:        EPICS - Micronix motion controllers

%{inherit motor + deps}
%description

%{inherit motor}

