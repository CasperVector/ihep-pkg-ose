%define repo motorOptem
%define commit v20241224
%{meta name license=EPICS codeberg=CasperVector version=commit,1}

Summary:        EPICS - Optem motion controllers

%{inherit motor + global deps}
%description

%{inherit motor}

