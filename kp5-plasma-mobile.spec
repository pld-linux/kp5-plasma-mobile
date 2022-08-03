#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.25.4
%define		qtver		5.15.2
%define		kpname		plasma-mobile
%define		kf5ver		5.39.0

Summary:	plasma-mobile
Name:		kp5-%{kpname}
Version:	5.25.4
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	86db281d990e794a0890b9b7933995fa
URL:		https://kde.org/
BuildRequires:	Qt5Core-devel >= 5.15.0
BuildRequires:	Qt5Gui-devel >= 5.15.0
BuildRequires:	Qt5Network-devel >= 5.15.0
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.82
BuildRequires:	kf5-ki18n-devel >= 5.82
BuildRequires:	kf5-kio-devel >= 5.82
BuildRequires:	kf5-knotifications-devel >= 5.82
BuildRequires:	kf5-kservice-devel >= 5.82
BuildRequires:	kf5-kwayland-devel >= 5.82
BuildRequires:	kf5-plasma-framework-devel >= 5.82
BuildRequires:	kp5-kwin-devel >= 5.23.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	xz
Obsoletes:	kp5-plasma-phone-components < 5.24.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		qt5dir		%{_libdir}/qt5

%description
UI components for Plasma Phone.

%description -l pl.UTF-8
Komponenty interfejsu użytkownika Plasma Phone.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	../
%ninja_build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

#%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwinwrapper
%{_libdir}/qt5/plugins/plasma/applets/plasma_applet_phonepanel.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_containment_phone_homescreen.so
%{_libdir}/qt5/plugins/plasma/applets/plasma_containment_phone_taskpanel.so
%{_libdir}/qt5/qml/org/kde/plasma/private/mobileshell
%{_datadir}/knotifications5/plasma_phone_components.notifyrc
%{_datadir}/metainfo/org.kde.plasma.phone.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.phoneshell.appdata.xml
%{_datadir}/plasma/look-and-feel/org.kde.plasma.phone
%{_datadir}/plasma/plasmoids/org.kde.phone.homescreen
%{_datadir}/plasma/plasmoids/org.kde.phone.panel
%{_datadir}/plasma/plasmoids/org.kde.phone.taskpanel
%{_datadir}/plasma/shells/org.kde.plasma.phoneshell
%{_datadir}/wayland-sessions/plasma-mobile.desktop
%{_libdir}/qt5/qml/org/kde/plasma/mm/libppc-mmqmlplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/mm/qmldir
%{_datadir}/kservices5/plasma-applet-org.kde.phone.homescreen.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.phone.panel.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.phone.taskpanel.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.phone.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.phoneshell.desktop
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/nightcolor/libnightcolorplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/nightcolor/qmldir

%{_libdir}/qt5/plugins/kcms/kcm_mobileshell.so
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/flashlight/libflashlightplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/flashlight/qmldir
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/powermenu/libpowermenuplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/powermenu/qmldir
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/screenrotation/libscreenrotationplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/screenrotation/qmldir
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/screenshot/libscreenshotplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/screenshot/qmldir

%dir %{_datadir}/kpackage/kcms/kcm_mobileshell
%dir %{_datadir}/kpackage/kcms/kcm_mobileshell/contents
%dir %{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui
%dir %{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui/mobileform
%{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui/VibrationForm.qml
%{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui/main.qml
%{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui/mobileform/AbstractFormDelegate.qml
%{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui/mobileform/FormButtonDelegate.qml
%{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui/mobileform/FormCard.qml
%{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui/mobileform/FormCardHeader.qml
%{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui/mobileform/FormCheckBoxDelegate.qml
%{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui/mobileform/FormComboBoxDelegate.qml
%{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui/mobileform/FormRadioButtonDelegate.qml
%{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui/mobileform/FormSectionText.qml
%{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui/mobileform/FormSwitchDelegate.qml
%{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui/mobileform/FormTextDelegate.qml
%{_datadir}/kpackage/kcms/kcm_mobileshell/metadata.desktop
%{_datadir}/kpackage/kcms/kcm_mobileshell/metadata.json
%{_datadir}/kservices5/kcm_mobileshell.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.quicksetting.airplanemode.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.quicksetting.audio.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.quicksetting.battery.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.quicksetting.bluetooth.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.quicksetting.caffeine.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.quicksetting.flashlight.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.quicksetting.keyboardtoggle.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.quicksetting.location.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.quicksetting.mobiledata.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.quicksetting.nightcolor.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.quicksetting.powermenu.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.quicksetting.screenrotation.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.quicksetting.screenshot.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.quicksetting.settingsapp.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.quicksetting.wifi.desktop
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.airplanemode
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.airplanemode/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.airplanemode/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.airplanemode/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.airplanemode/metadata.desktop
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.airplanemode/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.audio
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.audio/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.audio/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.audio/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.audio/metadata.desktop
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.audio/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.battery
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.battery/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.battery/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.battery/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.battery/metadata.desktop
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.battery/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.bluetooth
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.bluetooth/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.bluetooth/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.bluetooth/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.bluetooth/metadata.desktop
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.bluetooth/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.caffeine
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.caffeine/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.caffeine/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.caffeine/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.caffeine/metadata.desktop
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.caffeine/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.flashlight
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.flashlight/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.flashlight/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.flashlight/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.flashlight/metadata.desktop
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.flashlight/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle/metadata.desktop
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.location
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.location/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.location/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.location/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.location/metadata.desktop
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.location/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.mobiledata
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.mobiledata/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.mobiledata/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.mobiledata/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.mobiledata/metadata.desktop
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.mobiledata/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.nightcolor
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.nightcolor/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.nightcolor/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.nightcolor/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.nightcolor/metadata.desktop
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.nightcolor/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.powermenu
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.powermenu/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.powermenu/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.powermenu/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.powermenu/metadata.desktop
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.powermenu/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenrotation
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenrotation/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenrotation/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenrotation/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenrotation/metadata.desktop
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenrotation/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenshot
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenshot/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenshot/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenshot/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenshot/metadata.desktop
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenshot/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.settingsapp
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.settingsapp/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.settingsapp/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.settingsapp/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.settingsapp/metadata.desktop
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.settingsapp/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.wifi
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.wifi/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.wifi/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.wifi/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.wifi/metadata.desktop
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.wifi/metadata.json
