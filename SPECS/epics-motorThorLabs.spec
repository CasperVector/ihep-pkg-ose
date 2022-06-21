%define repo motorThorLabs
%define commit R1-0-1
%{meta name license=EPICS github=epics-motor version=commit,1}

Summary:        EPICS - Thorlabs motion controllers

%{inherit motor + deps}
%description

%{inherit motor}

