%define repo motorPIGCS2
%define commit R1-2
%{meta name license=EPICS github=epics-motor version=commit,2}

Summary:        EPICS - PI GCS2 motion controllers

%{inherit motor + global deps}
%description

%{inherit motor}

