%define svn		862
%define release 		0.%{svn}.4
%define major		0
%define libname		%mklibname %{name} %{major}
%define develname	%mklibname %{name} -d
Name:			akamaru
Version:			0.1
Release:			%{release}
Summary:			Physics engine used by kiba-dock
Group:			System/X11
URL:			http://www.kiba-dock.org/
Source0:			%{name}-%{svn}.tar.lzma
Patch0:			akamaru-0.1-build.patch
License:			BSD
BuildRequires:		intltool
BuildRequires:		pkgconfig(glib-2.0)

%description
Akamaru is a simple, but fun, physics engine prototype. It is used by
kiba-dock, a dock applet.

%package -n %{libname}
Group:		System/Libraries
Summary:	Shared library for %{name}
Provides:	lib%{name} = %{version}-%{release}

%description -n %{libname}
Akamaru is a simple, but fun, physics engine prototype. It is used by
kiba-dock, a dock applet.

%package -n %{develname}
Group:		Development/C
Summary:	Development headers for %{name}
Provides:	%{name}-devel = %{version}-%{release}
Requires:	%{libname} = %{version}-%{release}

%description -n %{develname}
Akamaru is a simple, but fun, physics engine prototype. It is used by
kiba-dock, a dock applet. This package contains development headers
for Akamaru.

%prep
%setup -q -n %{name}
%patch0 -p1 -b .build

%build
export LDFLAGS="${LDFLAGS} -lm" 
sh autogen.sh -V
%configure
%make 

%install
%makeinstall_std

%files -n %{libname}
%{_libdir}/lib%{name}.so.%{major}*

%files -n %{develname}
%doc AUTHORS ChangeLog README
%{_includedir}/%{name}
%{_libdir}/lib%{name}.so
#{_libdir}/lib%{name}.*a
%{_libdir}/pkgconfig/%{name}.pc


