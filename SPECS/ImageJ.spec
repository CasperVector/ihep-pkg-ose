%define fcommit 2.9.0
%define vcommit R1-7

Name:           ImageJ
Version:        1.53t
Release:        1.el%{rhel}
Summary:        ImageJ with ADViewer and HDF5
License:        Mixed
URL:            https://imagej.net/

# https://wsr.imagej.net/distros/cross-platform/ij153.zip
Source0:        %{dist_srv}/ij-%{version}.zip
Source1:        https://downloads.imagej.net/fiji/releases/%{fcommit}/fiji-%{fcommit}-nojre.zip
Source2:        %{github_archive areaDetector ADViewers %{vcommit}}
Patch0:         %{name}-1.53t-files.patch
BuildRequires:  java-1.8.0-openjdk-devel, libicns-utils
Requires:       java-1.8.0-openjdk

%description

%prep
%setup -c -n %{name}
. %{_specdir}/fn-build.sh
unzip %{S:1}; tar xpf %{S:2}; _mv_commit ADViewers %{vcommit}
patch -p1 < %{P:0}

%build
mv ADViewers/ImageJ/EPICS_areaDetector .
/usr/lib/jvm/java-1.8.0-openjdk/bin/javac -source 1.8 -target 1.8 \
	-Xlint:unchecked -deprecation -classpath \
	ImageJ/ij.jar:"$(echo EPICS_areaDetector/*.jar | tr ' ' ':')" \
	EPICS_areaDetector/*.java
mv EPICS_areaDetector ImageJ/plugins
cd Fiji.app/jars; mv \
	commons-io-*.jar commons-lang3-*.jar base-*.jar jhdf5-*.jar \
	../../ImageJ/plugins/jars; cd -
mv Fiji.app/plugins/HDF5_Vibez-*.jar ImageJ/plugins
icns2png -x ImageJ/ImageJ.app/Contents/Resources/ImageJ.icns
cd ImageJ; rm -rf ImageJ.app ImageJ.exe run; cd -
chmod -R go-w ImageJ

%install
. %{_specdir}/fn-build.sh
mkdir -p %{buildroot}/opt %{buildroot}%{_bindir} \
	%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/icons/hicolor/128x128/apps
cp -r %{name} %{buildroot}/opt
install -m 0755 %{name}.sh %{buildroot}%{_bindir}/%{name}
install -m 0644 %{name}_128x128x32.png \
	%{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{name}.png
install -m 0644 %{name}.desktop %{buildroot}%{_datadir}/applications
%_file_list /opt /usr > all.lst

%files -f all.lst

