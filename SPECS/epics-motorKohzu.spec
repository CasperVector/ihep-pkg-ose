%define repo motorKohzu
%define commit R1-0-1
%{meta name license=EPICS github=epics-motor version=commit,5}

Summary:        EPICS - Kohzu motion controllers
Patch0:         %{name}-1_0_1-aries.patch
Obsoletes:      epics-motorKohzuARIES

%{inherit motor + global deps}
%description

%{inherit motor - prep}

%{inherit motor + prep}

cp -r kohzuIOC kohzuARIESIOC
echo kohzuARIESIOC >> ioc.lst

