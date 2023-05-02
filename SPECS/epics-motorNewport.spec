%define repo motorNewport
%define commit 070c93e1
%{meta name license=EPICS github=epics-motor version=1_1_3,3.commit}

Summary:        EPICS - Newport motion controllers

%{inherit motor + global deps}
%description

%{inherit motor}

