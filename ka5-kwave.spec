%define		kdeappsver	21.08.0
%define		kframever	5.56.0
%define		qtver		5.9.0
%define		kaname		kwave
Summary:	Sound editor
Name:		ka5-%{kaname}
Version:	21.08.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	http://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	209c5d97cc34b79c284dbced10e250df
URL:		http://www.kde.org/
BuildRequires:	ImageMagick
BuildRequires:	ImageMagick-coder-svg
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5Gui-devel >= 5.11.1
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5Network-devel >= 5.11.1
BuildRequires:	Qt5Widgets-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	flac-devel
BuildRequires:	flac-c++-devel
BuildRequires:	gettext-devel
BuildRequires:	id3lib-devel
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-karchive-devel >= %{kframever}
BuildRequires:	kf5-kcompletion-devel >= %{kframever}
BuildRequires:	kf5-kconfig-devel >= %{kframever}
BuildRequires:	kf5-kconfigwidgets-devel >= %{kframever}
BuildRequires:	kf5-kcoreaddons-devel >= %{kframever}
BuildRequires:	kf5-kcrash-devel >= %{kframever}
BuildRequires:	kf5-kdbusaddons-devel >= %{kframever}
BuildRequires:	kf5-kdoctools-devel >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kiconthemes-devel >= %{kframever}
BuildRequires:	kf5-kio-devel >= %{kframever}
BuildRequires:	kf5-kservice-devel >= %{kframever}
BuildRequires:	kf5-ktextwidgets-devel >= %{kframever}
BuildRequires:	kf5-kwidgetsaddons-devel >= %{kframever}
BuildRequires:	kf5-kxmlgui-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	opus-devel
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kwave is a sound editor built on the KDE Frameworks 5.

%description -l pl.UTF-8
Kwave to edytor dźwięku zbudowany na bazie KDE Frameworks 5.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kwave
%ghost %{_libdir}/libkwave.so.21
%attr(755,root,root) %{_libdir}/libkwave.so.*.*.*
%ghost %{_libdir}/libkwavegui.so.21
%attr(755,root,root) %{_libdir}/libkwavegui.so.*.*.*
%dir %{_libdir}/qt5/plugins/kwave
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_about.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_amplifyfree.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_band_pass.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_codec_ascii.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_codec_audiofile.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_codec_flac.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_codec_mp3.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_codec_ogg.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_codec_wav.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_debug.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_export_k3b.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_fileinfo.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_goto.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_insert_at.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_lowpass.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_newsignal.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_noise.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_normalize.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_notch_filter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_pitch_shift.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_playback.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_record.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_reverse.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_samplerate.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_saveblocks.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_selectrange.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_sonagram.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_stringenter.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_volume.so
%attr(755,root,root) %{_libdir}/qt5/plugins/kwave/kwaveplugin_zero.so
%{_desktopdir}/org.kde.kwave.desktop
%{_iconsdir}/hicolor/scalable/actions/kwave_player_end.svgz
%{_iconsdir}/hicolor/scalable/actions/kwave_player_fwd.svgz
%{_iconsdir}/hicolor/scalable/actions/kwave_player_loop.svgz
%{_iconsdir}/hicolor/scalable/actions/kwave_player_pause.svgz
%{_iconsdir}/hicolor/scalable/actions/kwave_player_pause_2.svgz
%{_iconsdir}/hicolor/scalable/actions/kwave_player_play.svgz
%{_iconsdir}/hicolor/scalable/actions/kwave_player_record.svgz
%{_iconsdir}/hicolor/scalable/actions/kwave_player_rew.svgz
%{_iconsdir}/hicolor/scalable/actions/kwave_player_start.svgz
%{_iconsdir}/hicolor/scalable/actions/kwave_player_stop.svgz
%{_iconsdir}/hicolor/scalable/actions/kwave_viewmag.svgz
%{_iconsdir}/hicolor/scalable/actions/kwave_viewmagfit.svgz
%{_iconsdir}/hicolor/scalable/actions/kwave_zoom_in.svgz
%{_iconsdir}/hicolor/scalable/actions/kwave_zoom_original.svgz
%{_iconsdir}/hicolor/scalable/actions/kwave_zoom_out.svgz
%{_iconsdir}/hicolor/scalable/apps/kwave.svgz
%{_datadir}/kservicetypes5/kwave-plugin.desktop
%{_datadir}/kwave
%{_datadir}/metainfo/org.kde.kwave.appdata.xml
