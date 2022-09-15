%define repo motorAerotech
%define commit R1-1
%{meta name license=EPICS github=epics-motor version=commit,2}

Summary:        EPICS - Aerotech motion controllers

%{inherit motor + deps}
%description

%{inherit motor}

