%define repo motorAerotech
%define commit R1-1
%{meta name license=EPICS github=epics-motor version=commit,4}

Summary:        EPICS - Aerotech motion controllers

%{inherit motor + global deps}
%description

%{inherit motor}

