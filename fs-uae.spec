Name:           fs-uae
Version:        3.1.66
Release:        1%{?dist}
Summary:        Amiga emulator with on-screen GUI and online play support

License:        GPLv2+
URL:            http://fs-uae.net/
Source0:        http://fs-uae.net/files/FS-UAE/Stable/%{version}/%{name}-%{version}.tar.xz

BuildRequires:  gcc-c++
BuildRequires:  automake
BuildRequires:  libpng-devel
BuildRequires:  glew-devel
BuildRequires:  glib2-devel
BuildRequires:  openal-soft-devel
BuildRequires:  SDL2-devel
BuildRequires:  libXi-devel
BuildRequires:  libmpeg2-devel
BuildRequires:  zlib-devel
BuildRequires:  freetype-devel
BuildRequires:  zip
BuildRequires:  gettext
BuildRequires:  desktop-file-utils
Requires:       hicolor-icon-theme


%description
FS-UAE is an Amiga emulator for Windows, Linux and Mac OS X
based on UAE/WinUAE, with a focus on emulating games.

Features include emulation of Amiga 500, 1200, 4000, CD32
and CDTV, perfectly smooth scrolling on 50Hz displays, support
for floppy images in ADF and IPF formats, CD-ROM images in ISO
or BIN/CUE format, mounting folders on your computer as Amiga
hard drives, support for Picasso 96 drivers for high-color and
high-resolution Workbench displays, and more.

A unique feature is support for cross-platform online play. You
can now play Amiga games against (or with) friends over the
Internet.

The emulator uses the latest Amiga emulation code from the
WinUAE project and requires a moderately fast computer with
accelerated graphics (OpenGL) to work. A game pad or joystick is
recommended, but not required (FS-UAE can emulate a joystick
using the cursor keys and right ctrl/alt keys).


%prep
%autosetup -p1

# Do not use bundled libmpeg2
rm -rf libmpeg2

# Fix spurious executable permissions
chmod -x src/specialmonitors.cpp


%build
%configure --disable-jit
%make_build


%install
%make_install

# Validate desktop file
desktop-file-validate \
  %{buildroot}%{_datadir}/applications/%{name}.desktop

%find_lang %{name}


%files -f %{name}.lang
%{_bindir}/%{name}
%{_bindir}/%{name}-device-helper
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/icons/hicolor/*/apps/%{name}.png
%{_datadir}/mime/packages/%{name}.xml
%doc %{_pkgdocdir}
%exclude %{_pkgdocdir}/COPYING
%license COPYING


%changelog
* Sat Dec 25 2021 Andrea Musuruane <musuruan@gmail.com> - 3.1.66-1
- Updated to new upstream release

* Mon Aug 02 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.0.5-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Sun Mar 21 2021 Andrea Musuruane <musuruan@gmail.com> - 3.0.5-4
- Fix FTBFS for gcc-11

* Wed Feb 03 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.0.5-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Mon Aug 17 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Sat Apr 25 2020 Andrea Musuruane <musuruan@gmail.com> - 3.0.5-1
- Updated to new upstream release

* Tue Feb 04 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 3.0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Nov 30 2019 Andrea Musuruane <musuruan@gmail.com> - 3.0.2-1
- Updated to new upstream release

* Mon Aug 12 2019 Andrea Musuruane <musuruan@gmail.com> - 3.0.0-1
- Updated to new upstream release

* Fri Aug 09 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.8.3-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Mon Mar 04 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.8.3-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 26 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.8.3-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Sat May 19 2018 Andrea Musuruane <musuruan@gmail.com> - 2.8.3-5
- Added gcc dependency

* Sat May 19 2018 Andrea Musuruane <musuruan@gmail.com> - 2.8.3-4
- Removed obsolete scriptlets

* Thu Mar 01 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.8.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sat Sep 09 2017 Andrea Musuruane <musuruan@gmail.com> - 2.8.3-2
- Fixed FTBFS

* Sat Sep 09 2017 Andrea Musuruane <musuruan@gmail.com> - 2.8.3-1
- Updated to new upstream version
- Improved macro usage
- Dropped mimeinfo scriptlet

* Wed May 18 2016 Andrea Musuruane <musuruan@gmail.com> - 2.6.2-2
- Fix FTBFS with GCC 6

* Sun Apr 03 2016 Andrea Musuruane <musuruan@gmail.com> - 2.6.2-1
- First release

