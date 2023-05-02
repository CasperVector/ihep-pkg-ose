%define repo motorOms
%define commit 5219f8ce
%{meta name license=EPICS github=epics-motor version=1_1_7,3.commit}

Summary:        EPICS - OMS motion controllers

%{inherit motor + global deps}
%description

%{inherit motor}

