Name:           fs-uae
Version:        2.8.3
Release:        5%{?dist}
Summary:        Amiga emulator with on-screen GUI and online play support

License:        GPLv2+
URL:            http://fs-uae.net/
Source0:        http://fs-uae.net/fs-uae/stable/%{version}/%{name}-%{version}.tar.gz
# Define unknown host CPU types as CPU_unknown
# https://github.com/glaubitz/fs-uae-debian/blob/master/debian/patches/0001-define-unknown-CPUs-as-CPU_unknown.patch
Patch0:         %{name}-2.8.3-define_unknown_CPUs.patch

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

# Fix desktop file
sed -i '/^MimeType=*/s/$/;/' \
  share/applications/%{name}.desktop

# Fix spurious executable permissions
chmod -x src/specialmonitors.cpp


%build
%ifarch %{ix86} x86_64
  %configure
%else
  %configure --disable-jit
%endif
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

