%define repo motorPIGCS2
%define commit R1-1
%{meta name license=EPICS github=epics-motor version=commit,3}

Summary:        EPICS - PI GCS2 motion controllers

%{inherit motor + global deps}
%description

%{inherit motor}

