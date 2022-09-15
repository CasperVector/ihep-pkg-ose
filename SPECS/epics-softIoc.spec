%{meta license=EPICS version=7.0.6.1,2}

Name:           epics-softIoc
Summary:        EPICS - softIoc extended with useful supports
URL:            https://epics.anl.gov/
Source0:        https://epics.anl.gov/download/base/base-%{version}.tar.gz
Patch0:         %{name}-7.0.6.1-app-libs.patch
BuildRequires:  epics-iocStats, gcc-c++, make, perl
Requires:       epics-iocStats

%description

%prep
%setup -c %{name}
mkdir softIoc
mv base-%{version}/modules/database/src/std/softIoc softIoc/src
cp -r %{epics_root}/utils/configure softIoc/configure
sed '/TOP/ s/=.*/= ./' < %{epics_root}/utils/app.mk > softIoc/Makefile
cd softIoc; patch -p1 < %{P:0}; sed -i \
	'/epicsInstallDir/ s@.*@#define EPICS_BASE "%{etop_base}"@' src/softMain.cpp

%build
cd softIoc
make %{?_smp_mflags} %{cmd_flags}

%install
. %{_specdir}/fn-build.sh
mkdir -p %{buildroot}%{etop_base}; cd softIoc
cp -r dbd bin %{buildroot}%{etop_base}; cd -
%_rm_extras; %_file_list %{epics_root} > epics.lst

%files -f epics.lst

