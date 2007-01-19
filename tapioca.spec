Summary:	A framework for Voice over IP (VoIP) and Instant Messaging (IM)
Name:		tapioca
Version:	0.3.9
Release:	1
License:	GPL
URL:		http://tapioca-voip.sourceforge.net/wiki/index.php/Tapioca
Group:		Networking/Instant messaging
Source0:	http://dl.sourceforge.net/tapioca-voip/%{name}-%{version}.tar.gz
# Source0-md5:	e88c400394c092c2688bb2d490c80ccb
Buildrequires:  glib2-devel
BuildRequires:  dbus-devel >= 0.36
BuildRequires:  dbus-glib-devel >= 0.36
BuildRequires:  pkgconfig
Requires:       %{name}-libs = %{version}-%{release}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Tapioca is a framework for Voice over IP (VoIP) and 
Instant Messaging (IM). Its main goal is to provide 
an easy way for developing and using VoIP and IM 
services in any kind of application. It was designed 
to be cross-platform, lightweight, thread-safe, having 
mobile devices and applications in mind.

	Tapioca's main goals are:
	
    * Create a solution that integrates all components 
used by VoIP and IM applications in a single, reliable 
and easy to use framework, which is able to work on different 
platforms.

    * Spare resources, providing central services for multiple 
applications. Eg.: The control of all incoming and outgoing SIP 
requests are managed by the SIP service, avoiding the creation of
 one SIP stack and allocation of a network port for each SIP-based 
application.

    * Reduce the overhead of control layers and library dependencies.

%package libs
Summary:	Tapioca library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description libs
Library for tapioca

%package libs-devel
Summary:	Headers for development
Group:		Development/C
Requires:	%{name}-libs = %{version}-%{release}

%description libs-devel
Headers of tapioca for development.

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
%attr(7554,root,root) %{_bindir}/*
%{_datadir}/dbus-1/services/org.tapioca.Server.service
 
%files libs
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*

%files libs-devel
%defattr(644,root,root,755)
%{_libdir}/lib*.la
%{_pkgconfigdir}/*.pc
%{_includedir}/*
