%define repo motorKohzuAsyn
%define commit v20241104
%{meta name license=EPICS codeberg=CasperVector version=commit,1}

Summary:        EPICS - Kohzu motion controllers using asynMotor

%{inherit motor + global deps}
%description

%{inherit motor}

