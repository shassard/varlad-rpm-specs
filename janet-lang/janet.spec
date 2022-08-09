%global debug_package %{nil}

Name:       janet
Version:    1.23.0
Release:    1%{?dist}
Summary:    A dynamic language and bytecode vm 

License:    MIT
URL:        https://github.com/janet-lang/janet
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

BuildRequires: gcc
Requires: gcc

%description
Janet is a functional and imperative programming language and bytecode interpreter. It is a lisp-like language, but lists are replaced by other data structures (arrays, tables (hash table), struct (immutable hash table), tuples). The language also supports bridging to native code written in C, meta-programming with macros, and bytecode assembly.

%prep
%autosetup -p1

%install
make
PREFIX=%{_prefix} LIBDIR=%{_prefix}/lib64 make install DESTDIR=%{buildroot}

strip --strip-all %{buildroot}%{_bindir}/*


%files
%license LICENSE
%doc README.md
%{_bindir}/janet
%{_libdir}/*
%{_includedir}/*
%{_datadir}/*
