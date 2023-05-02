%define repo motorSmartMotor
%define commit R1-0-1
%{meta name license=EPICS github=epics-motor version=commit,3}

Summary:        EPICS - SmartMotor motion controllers

%{inherit motor + global deps}
%description

%{inherit motor}

