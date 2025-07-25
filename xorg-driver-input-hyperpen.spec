Summary:	X.org input driver for Aiptek HyperPen devices
Summary(pl.UTF-8):	Sterownik wejściowy X.org dla urządzeń Aiptek HyperPen
Name:		xorg-driver-input-hyperpen
Version:	1.4.1
Release:	11
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-hyperpen-%{version}.tar.bz2
# Source0-md5:	75dc36477a291f8c2f7c808ab78a400a
Patch0:		am.patch
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	rpmbuild(macros) >= 1.389
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 0.99.2
BuildRequires:	xorg-xserver-server-devel >= 1.10.0
%{?requires_xorg_xserver_xinput}
Requires:	xorg-xserver-server >= 1.10.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for Aiptek HyperPen devices. It supports Aiptek
HyperPen 6000.

%description -l pl.UTF-8
Sterownik wejściowy X.org dla urządzeń Aiptek HyperPen. Obsługuje
Aiptek HyperPen 6000.

%prep
%setup -q -n xf86-input-hyperpen-%{version}
%patch -P0 -p1

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/input/hyperpen_drv.so
#%{_mandir}/man4/hyperpen.4*
