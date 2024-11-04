%define commit 20221104

Name:           phoebus
Version:        4.6.10
Release:        1.%{commit}.el%{rhel}
Summary:        Control System Studio (the Phoebus branch)
License:        EPLv1.0
URL:            https://controlssoftware.sns.ornl.gov/css_phoebus/

# https://controlssoftware.sns.ornl.gov/css_phoebus/nightly/phoebus-linux.zip
Source0:        %{dist_srv}/%{name}-linux-%{commit}.zip
Source1:        %{name}-csslogo.svg
Patch0:         %{name}-20221104-files.patch
Requires:       java-11-openjdk

%description

%prep
%setup -c -n %{name}
. %{_specdir}/fn-build.sh
_mv_commit %{name} %{version}
patch -p1 < %{P:0}

%build
cd %{name}
rm phoebus.bat phoebus.desktop phoebus.xml
mv settings_template.ini settings.ini

%install
. %{_specdir}/fn-build.sh
mkdir -p %{buildroot}/opt %{buildroot}%{_bindir} \
	%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/icons/hicolor/scalable/apps
cp -r %{name} %{buildroot}/opt
install -m 0755 %{name}.sh %{buildroot}%{_bindir}/%{name}
install -m 0644 %{S:1} \
	%{buildroot}%{_datadir}/icons/hicolor/scalable/apps/%{name}.svg
install -m 0644 %{name}.desktop %{buildroot}%{_datadir}/applications
%_file_list /opt /usr | grep -vF /opt/phoebus/settings.ini > noetc.lst

%files -f noetc.lst
%config(noreplace) /opt/phoebus/settings.ini

