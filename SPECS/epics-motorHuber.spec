%define repo motorHuber
%define commit v20241104
%{meta name license=EPICS codeberg=CasperVector version=commit,1}

Summary:        EPICS - Motion controllers from Huber diffractometers

%{inherit motor + global deps}
%description

%{inherit motor}

