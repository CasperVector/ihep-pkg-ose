%define repo motorOms
%define commit 5219f8ce
%{meta name license=EPICS github=epics-motor version=1_1_7,2.commit}

Summary:        EPICS - OMS motion controllers

%{inherit motor + deps}
%description

%{inherit motor}

