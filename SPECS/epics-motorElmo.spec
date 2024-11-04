%define repo motorElmo
%define commit v20230608
%{meta name license=EPICS codeberg=CasperVector version=commit,2}

Summary:        EPICS - Elmo motion controllers

%{inherit motor + global deps}
%description

%{inherit motor}

