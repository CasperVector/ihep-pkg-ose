%define repo motorNPoint
%define commit R1-0-1
%{meta name license=EPICS github=epics-motor version=commit,4}

Summary:        EPICS - nPoint motion controllers

%{inherit motor + global deps}
%description

%{inherit motor}

