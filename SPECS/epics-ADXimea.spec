%define repo ADXimea
%define commit v20240723
%{meta name license=EPICS codeberg=CasperVector version=commit,2}

Summary:        EPICS - Driver for Ximea cameras
Patch0:         %{name}-20230328-support.patch
BuildRequires:  epics-ADGenICam, ximea-sdk
Requires:       epics-ADGenICam, ximea-sdk

%{inherit ad + global deps}
%description

%{inherit ad - prep}

%{inherit ad + prep}
rm -rf %{repo}/documentation %{repo}/*Support
cd ximeaIOC/iocBoot/iocXimea
%{etop_ad}/ADGenICam/scripts/makeDb.py \
	--devInt64 ximeaFeature.json ximeaFeature.template

