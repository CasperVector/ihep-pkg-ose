%define repo motorParker
%define commit R1-1
%{meta name license=EPICS github=epics-motor version=commit,1}

Summary:        EPICS - Parker motion controllers

%{inherit motor + deps}
%description

%{inherit motor}

