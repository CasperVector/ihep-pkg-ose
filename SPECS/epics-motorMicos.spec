%define repo motorMicos
%define commit R2-0
%{meta name license=EPICS github=epics-motor version=commit,2}

Summary:        EPICS - Micos motion controllers

%{inherit motor + deps}
%description

%{inherit motor}

