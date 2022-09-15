%define repo motorOriel
%define commit R1-0-1
%{meta name license=EPICS github=epics-motor version=commit,2}

Summary:        EPICS - Oriel motion controllers

%{inherit motor + deps}
%description

%{inherit motor}

