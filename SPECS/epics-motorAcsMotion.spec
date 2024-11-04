%define repo motorAcsMotion
%define commit R2-2
%{meta name license=EPICS github=epics-motor version=commit,2}

Summary:        EPICS - ACSPL+ motion controllers

%{inherit motor + global deps}
%description

%{inherit motor}

