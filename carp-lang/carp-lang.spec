%global debug_package %{nil}

Name:       carp
Version:    0.5.5
Release:    1%{?dist}
Summary:    A statically typed lisp, without a GC, for real-time applications.  

License:    Apache-2.0 license
URL:        https://github.com/carp-lang/Carp
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

Requires: clang
BuildRequires: gcc
BuildRequires: ncurses-devel
BuildRequires: stack <= 2.7.3-13

%description
Carp is a programming language designed to work well for interactive and performance sensitive use cases like games, sound synthesis and visualizations.


%prep
%autosetup -n Carp-%{version}

%install
stack build
mkdir -p %{buildroot}%{_bindir}
mkdir -p %{buildroot}%{_libdir}/carp
mkdir -p %{buildroot}%{_datadir}/carp
stack install --local-bin-path %{buildroot}%{_libexecdir}
mv ./core %{buildroot}%{_libdir}/carp
cat >> %{buildroot}%{_bindir}/carp <<EOF
#!/usr/bin/env sh

CARP_DIR="%{_libdir}/carp" exec %{_libexecdir}/carp "\$@"
EOF
chmod +x %{buildroot}%{_prefix}/bin/carp
cat >> %{buildroot}%{_bindir}/carp-header-parse <<EOF
#!/usr/bin/env sh

CARP_DIR="%{_libdir}/carp" exec %{_libexecdir}/carp-header-parse "\$@"
EOF
chmod +x %{buildroot}%{_prefix}/bin/carp-header-parse

mkdir -p %{buildroot}%{_datadir}/licenses/carp
mv LICENSE %{buildroot}%{_datadir}/licenses/carp/LICENSE
mkdir -p %{buildroot}%{_docdir}/carp
mv README.md %{buildroot}%{_docdir}/carp/README.md

%files
%license LICENSE
%doc README.md
%{_bindir}/carp
%{_bindir}/carp-header-parse
%{_libexecdir}/carp
%{_libexecdir}/carp-header-parse
%{_libdir}/carp/core/
