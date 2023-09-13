#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.27.8
%define		qtver		5.15.2
%define		kpname		plasma-mobile
%define		kf5_ver		5.102.0

Summary:	plasma-mobile
Name:		kp5-%{kpname}
Version:	5.27.8
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	5d6cde521ae2539c921fda62efdefd8a
URL:		https://kde.org/
BuildRequires:	Qt5Core-devel >= 5.15.0
BuildRequires:	Qt5Gui-devel >= 5.15.0
BuildRequires:	Qt5Network-devel >= 5.15.0
BuildRequires:	Qt5Qml-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	cmake >= 3.16.0
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.82
BuildRequires:	kf5-ki18n-devel >= 5.82
BuildRequires:	kf5-kio-devel >= 5.82
BuildRequires:	kf5-knotifications-devel >= 5.82
BuildRequires:	kf5-kservice-devel >= 5.82
BuildRequires:	kf5-kwayland-devel >= 5.82
BuildRequires:	kf5-modemmanager-qt-devel >= 5.82
BuildRequires:	kf5-plasma-framework-devel >= 5.82
BuildRequires:	kirigami-addons-devel >= 0.7.0
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
%cmake -B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	-DHTML_INSTALL_DIR=%{_kdedocdir}
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kpname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kpname}.lang
%defattr(644,root,root,755)
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
%dir %{_libdir}/qt5/qml/org/kde/plasma/mm
%{_libdir}/qt5/qml/org/kde/plasma/mm/libppc-mmqmlplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/mm/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/quicksetting
%dir %{_libdir}/qt5/qml/org/kde/plasma/quicksetting/nightcolor
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/nightcolor/libnightcolorplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/nightcolor/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/quicksetting/flashlight
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/flashlight/libflashlightplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/flashlight/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/quicksetting/powermenu
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/powermenu/libpowermenuplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/powermenu/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/quicksetting/screenrotation
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/screenrotation/libscreenrotationplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/screenrotation/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/quicksetting/screenshot
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/screenshot/libscreenshotplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/screenshot/qmldir
%dir %{_datadir}/kpackage/kcms/kcm_mobileshell
%dir %{_datadir}/kpackage/kcms/kcm_mobileshell/contents
%dir %{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui
%{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui/VibrationForm.qml
%{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui/main.qml
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.airplanemode
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.airplanemode/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.airplanemode/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.airplanemode/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.airplanemode/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.audio
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.audio/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.audio/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.audio/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.audio/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.battery
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.battery/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.battery/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.battery/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.battery/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.bluetooth
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.bluetooth/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.bluetooth/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.bluetooth/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.bluetooth/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.caffeine
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.caffeine/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.caffeine/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.caffeine/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.caffeine/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.flashlight
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.flashlight/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.flashlight/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.flashlight/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.flashlight/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.mobiledata
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.mobiledata/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.mobiledata/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.mobiledata/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.mobiledata/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.nightcolor
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.nightcolor/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.nightcolor/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.nightcolor/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.nightcolor/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.powermenu
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.powermenu/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.powermenu/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.powermenu/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.powermenu/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenrotation
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenrotation/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenrotation/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenrotation/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenrotation/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenshot
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenshot/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenshot/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenshot/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenshot/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.settingsapp
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.settingsapp/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.settingsapp/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.settingsapp/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.settingsapp/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.wifi
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.wifi/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.wifi/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.wifi/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.wifi/metadata.json

%attr(755,root,root) %{_bindir}/startplasmamobile
%{_libdir}/qt5/plugins/plasma/applets/plasma_containment_phone_homescreen_halcyon.so
%{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_mobileshell.so
%{_desktopdir}/kcm_mobileshell.desktop
%{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui/QuickSettingsForm.qml
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.phone.desktop
%{_datadir}/metainfo/org.kde.phone.homescreen.appdata.xml
%{_datadir}/metainfo/org.kde.phone.homescreen.halcyon.appdata.xml
%{_datadir}/metainfo/org.kde.phone.panel.appdata.xml
%{_datadir}/metainfo/org.kde.phone.taskpanel.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.airplanemode.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.audio.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.battery.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.bluetooth.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.caffeine.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.donotdisturb.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.flashlight.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.keyboardtoggle.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.mobiledata.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.nightcolor.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.powermenu.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.record.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.screenrotation.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.screenshot.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.settingsapp.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.quicksetting.wifi.appdata.xml
%dir %{_datadir}/plasma/plasmoids/org.kde.phone.homescreen.halcyon
%dir %{_datadir}/plasma/plasmoids/org.kde.phone.homescreen.halcyon/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.phone.homescreen.halcyon/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.phone.homescreen.halcyon/contents/ui/Clock.qml
%{_datadir}/plasma/plasmoids/org.kde.phone.homescreen.halcyon/contents/ui/FavoritesAppDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.phone.homescreen.halcyon/contents/ui/FavoritesGrid.qml
%{_datadir}/plasma/plasmoids/org.kde.phone.homescreen.halcyon/contents/ui/FavoritesView.qml
%{_datadir}/plasma/plasmoids/org.kde.phone.homescreen.halcyon/contents/ui/FolderGrid.qml
%{_datadir}/plasma/plasmoids/org.kde.phone.homescreen.halcyon/contents/ui/GridAppDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.phone.homescreen.halcyon/contents/ui/GridAppList.qml
%{_datadir}/plasma/plasmoids/org.kde.phone.homescreen.halcyon/contents/ui/HomeScreen.qml
%{_datadir}/plasma/plasmoids/org.kde.phone.homescreen.halcyon/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.phone.homescreen.halcyon/metadata.json
%dir %{_datadir}/plasma/quicksettings
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.donotdisturb
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.donotdisturb/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.donotdisturb/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.donotdisturb/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.donotdisturb/metadata.json
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.record
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.record/contents
%dir %{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.record/contents/ui
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.record/contents/ui/main.qml
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.record/metadata.json
%dir %{_libdir}/qt5/qml/org/kde/plasma/quicksetting/record
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/record/librecordplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/record/qmldir
