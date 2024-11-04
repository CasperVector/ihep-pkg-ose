%define repo motorBoci
%define commit v20241104
%{meta name license=EPICS codeberg=CasperVector version=commit,1}

Summary:        EPICS - BOCIC motion controllers

%{inherit motor + global deps}
%description

%{inherit motor}

