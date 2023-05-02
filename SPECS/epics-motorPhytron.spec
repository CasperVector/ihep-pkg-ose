%define repo motorPhytron
%define commit R1-1
%{meta name license=EPICS github=epics-motor version=commit,3}

Summary:        EPICS - Phytron motion controllers

%{inherit motor + global deps}
%description

%{inherit motor}

