%global debug_package   %{nil}

Summary:	Parsing Expression Grammar Template Library
Name:		pegtl
Version:	2.8.3
Release:	2
Group:		Development/C++
License:	MIT
URL:		https://github.com/taocpp/%{name}/
Source0:	https://github.com/taocpp/%{name}/archive/PEGTL-%{version}.tar.gz
BuildRequires:	cmake
BuildArch:	noarch

%description
The Parsing Expression Grammar Template Library (PEGTL) is a zero-dependency
C++11 header-only library for creating parsers according to a Parsing
Expression Grammar (PEG).

%package devel
Summary:	Development files for %{name}
Group:		Development/C++
Provides:	%{name} = %{EVRD}
Provides:	PEGTL = %{EVRD}
Provides:	PEGTL-devel = %{EVRD}

%description devel
The %{name}-devel package contains C++ header files for developing
applications that use %{name}.

%prep
%autosetup -n PEGTL-%{version} -p1

%build
%cmake \
    -DCMAKE_BUILD_TYPE=None \
    -DPEGTL_INSTALL_CMAKE_DIR:PATH=%{_datadir}/cmake/Modules \
    -DPEGTL_BUILD_EXAMPLES:BOOL=OFF \
    -DPEGTL_BUILD_TESTS:BOOL=OFF

%make_build

%install
%make_install -C build

rm -rf %{buildroot}%{_docdir}/tao/pegtl/LICENSE

%files devel
%doc README.md doc/
%license LICENSE
%{_includedir}/*
%{_datadir}/cmake/Modules
