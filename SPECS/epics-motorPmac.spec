%define repo motorPmac
%define commit 20250725
%{meta name license=EPICS version=2.6.5,1.commit}
URL:            https://codeberg.org/CasperVector/%{repo}
Source0:        %{codeberg_archive CasperVector %{repo} v%{commit}}

Summary:        EPICS - DeltaTau PMAC motion controllers
Patch0:         %{name}-20250725-config.patch
BuildRequires:  epics-calc, libssh2-devel
Requires:       epics-calc, libssh2

%{inherit motor + global deps}
%description

%{inherit motor - prep}

%{inherit motor + prep}
echo 'CALC=$(SUPPORT)/calc' > %{repo}/configure/RELEASE.local
sed 's/lib64/lib/' \
	< %{repo}/configure/CONFIG_SITE.linux-x86_64.Common \
	> %{repo}/configure/CONFIG_SITE.linux-x86.Common
find %{repo}/etc -name '*].hwsetup' | while read name; do
	mv "$name" "$(echo "$name" | tr '[]' '()')"; done

