Summary:	A framework for Voice over IP (VoIP) and Instant Messaging (IM)
Summary(pl):	Szkielet do VoIP (Voice over IP) i IM (Instant Messaging)
Name:		tapioca
Version:	0.3.9
Release:	1
License:	GPL
Group:		Networking/Instant messaging
Source0:	http://dl.sourceforge.net/tapioca-voip/%{name}-%{version}.tar.gz
# Source0-md5:	e88c400394c092c2688bb2d490c80ccb
URL:		http://tapioca-voip.sourceforge.net/wiki/index.php/Tapioca
BuildRequires:	glib2-devel >= 2.0
BuildRequires:	dbus-devel >= 0.36
BuildRequires:	dbus-glib-devel >= 0.36
BuildRequires:	pkgconfig
Requires:	%{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tapioca is a framework for Voice over IP (VoIP) and Instant Messaging
(IM). Its main goal is to provide an easy way for developing and using
VoIP and IM services in any kind of application. It was designed to be
cross-platform, lightweight, thread-safe, having mobile devices and
applications in mind.

Tapioca's main goals are:
 - Create a solution that integrates all components used by VoIP and
   IM applications in a single, reliable and easy to use framework,
   which is able to work on different platforms.
 - Spare resources, providing central services for multiple
   applications. Eg.: The control of all incoming and outgoing SIP
   requests are managed by the SIP service, avoiding the creation of
   one SIP stack and allocation of a network port for each SIP-based
   application.
- Reduce the overhead of control layers and library dependencies.

%description -l pl
Tapioca to szkielet do VoIP (Voice over IP) i IM (Instant Messaging,
czyli komunikatorów). G³ównym jego celem jest zapewnienie ³atwego
sposobu tworzenia i u¿ywania us³ug VoIP i IM w dowolnym rodzaju
aplikacji. Zosta³ zaprojektowany jako wieloplatformowy, lekki,
bezpieczny dla w±tków, a tak¿e z my¶l± o urz±dzeniach i aplikacjach
przeno¶nych.

G³ówne cele projektu Tapioca to:
 - stworzenie rozwi±zania integruj±cego wszystkie komponenty u¿ywane
   przez aplikacje VoIP i IM w pojedynczym, pewnym i ³atwym w u¿yciu
   szkielecie, nadaj±cym siê do wykorzystania na ró¿nych platformach
 - oszczêdno¶æ zasobów poprzez udostêpnienie centralnych us³ug dla
   wielu aplikacji; na przyk³ad: sterowanie wszystkimi przychodz±cymi
   i wychodz±cymi ¿±daniami SIP jest obs³ugiwane przez us³ugê SIP, co
   zapobiega tworzeniu jednego stosu SIP i przydzielania portu
   sieciowego dla ka¿dej aplikacji opartej na SIP
 - ograniczenie narzutu warstw steruj±cych i zale¿no¶ci bibliotek

%package libs
Summary:	Tapioca library
Summary(pl):	Biblioteka Tapioca
Group:		Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	dbus-glib >= 0.36

%description libs
Tapioca library.

%description libs -l pl
Biblioteka Tapioca.

%package libs-devel
Summary:	Headers for development using Tapioca framework
Summary(pl):	Pliki nag³ówkowe szkieletu Tapioca
Group:		Development/Libraries
Requires:	%{name}-libs = %{version}-%{release}
Requires:	glib2-devel >= 2.0
Requires:	dbus-glib-devel >= 0.36

%description libs-devel
Headers of tapioca for development.

%description libs-devel -l pl
Pliki nag³ówkowe szkieletu Tapioca.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	libs -p /sbin/ldconfig
%postun	libs -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_datadir}/dbus-1/services/org.tapioca.Server.service
 
%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

%files libs-devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/*
