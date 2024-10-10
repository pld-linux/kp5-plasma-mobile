#
# Conditional build:
%bcond_with	tests		# test suite

%define		kdeplasmaver	5.27.11
%define		qtver		5.15.2
%define		kpname		plasma-mobile
%define		kf5_ver		5.102.0

Summary:	plasma-mobile
Name:		kp5-%{kpname}
Version:	5.27.11
Release:	2
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	5df7642fa42db0acf4dd4c17a508311d
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
BuildRequires:	kf5-kirigami-addons-devel >= 0.7.0
BuildRequires:	kf5-knotifications-devel >= 5.82
BuildRequires:	kf5-kservice-devel >= 5.82
BuildRequires:	kf5-kwayland-devel >= 5.82
BuildRequires:	kf5-modemmanager-qt-devel >= 5.82
BuildRequires:	kf5-plasma-framework-devel >= 5.82
BuildRequires:	kp5-kwin-devel >= 5.23.0
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	xz
Obsoletes:	kp5-plasma-phone-components < 5.24.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
%attr(755,root,root) %{_bindir}/startplasmamobile
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/applets/plasma_applet_phonepanel.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/applets/plasma_containment_phone_homescreen.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/applets/plasma_containment_phone_homescreen_halcyon.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/applets/plasma_containment_phone_taskpanel.so
%attr(755,root,root) %{_libdir}/qt5/plugins/plasma/kcms/systemsettings/kcm_mobileshell.so
%dir %{_libdir}/qt5/qml/org/kde/plasma/mm
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/mm/libppc-mmqmlplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/mm/qmldir
%{_libdir}/qt5/qml/org/kde/plasma/private/mobileshell
%dir %{_libdir}/qt5/qml/org/kde/plasma/quicksetting
%dir %{_libdir}/qt5/qml/org/kde/plasma/quicksetting/nightcolor
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/quicksetting/nightcolor/libnightcolorplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/nightcolor/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/quicksetting/flashlight
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/quicksetting/flashlight/libflashlightplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/flashlight/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/quicksetting/powermenu
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/quicksetting/powermenu/libpowermenuplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/powermenu/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/quicksetting/record
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/quicksetting/record/librecordplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/record/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/quicksetting/screenrotation
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/quicksetting/screenrotation/libscreenrotationplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/screenrotation/qmldir
%dir %{_libdir}/qt5/qml/org/kde/plasma/quicksetting/screenshot
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/plasma/quicksetting/screenshot/libscreenshotplugin.so
%{_libdir}/qt5/qml/org/kde/plasma/quicksetting/screenshot/qmldir
%{_datadir}/knotifications5/plasma_phone_components.notifyrc
%dir %{_datadir}/kpackage/kcms/kcm_mobileshell
%dir %{_datadir}/kpackage/kcms/kcm_mobileshell/contents
%dir %{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui
%{_datadir}/kpackage/kcms/kcm_mobileshell/contents/ui/*.qml
%{_datadir}/kservices5/plasma-applet-org.kde.plasma.phone.desktop
%{_datadir}/metainfo/org.kde.phone.homescreen.appdata.xml
%{_datadir}/metainfo/org.kde.phone.homescreen.halcyon.appdata.xml
%{_datadir}/metainfo/org.kde.phone.panel.appdata.xml
%{_datadir}/metainfo/org.kde.phone.taskpanel.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.phone.appdata.xml
%{_datadir}/metainfo/org.kde.plasma.phoneshell.appdata.xml
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
%{_datadir}/plasma/look-and-feel/org.kde.plasma.phone
%{_datadir}/plasma/plasmoids/org.kde.phone.homescreen
%{_datadir}/plasma/plasmoids/org.kde.phone.homescreen.halcyon
%{_datadir}/plasma/plasmoids/org.kde.phone.panel
%{_datadir}/plasma/plasmoids/org.kde.phone.taskpanel
%dir %{_datadir}/plasma/quicksettings
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.airplanemode
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.audio
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.battery
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.bluetooth
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.caffeine
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.donotdisturb
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.flashlight
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.keyboardtoggle
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.mobiledata
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.nightcolor
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.powermenu
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.record
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenrotation
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.screenshot
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.settingsapp
%{_datadir}/plasma/quicksettings/org.kde.plasma.quicksetting.wifi
%{_datadir}/plasma/shells/org.kde.plasma.phoneshell
%{_datadir}/wayland-sessions/plasma-mobile.desktop
%{_desktopdir}/kcm_mobileshell.desktop
