%define repo motorElmo
%define commit v20250114
%{meta name license=EPICS codeberg=CasperVector version=commit,1}

Summary:        EPICS - Elmo motion controllers

%{inherit motor + global deps}
%description

%{inherit motor}

