%global debug_package %{nil}

Name:       jpm
Version:    master
Release:    2%{?dist}
Summary:    Janet Project Manager 

License:    MIT
URL:        https://github.com/janet-lang/jpm
Source0:    %{url}/archive/refs/heads/master.zip

Requires: gcc
Requires: janet
BuildRequires: gcc
BuildRequires: janet

%description
JPM is the Janet Project Manager tool. It is for automating builds and downloading dependencies of Janet projects. This project is a port of the original jpm tool (which started as a single file script) to add more functionality, clean up code, make more portable and configurable, and refactor jpm into independent, reusable pieces that can be imported as normal Janet modules.
This also introduces parallel builds, possible MSYS support, a jpm configuration file, and more CLI options. Other improvements are planned such as parallel dependency downloading, more out of the box support for non-C toolchains and pkg-config, installation from sources besides git such as remote tarballs, zipfiles, or local directories, and more.

%prep
%autosetup -p1

%install
JANET_PATH=%{_libdir}/janet JANET_LIBPATH=%{_libdir} PREFIX=%{_prefix} DESTDIR=%{buildroot} janet bootstrap.janet 

%files
%license LICENSE
%doc README.md
%{_bindir}/jpm
%{_libdir}/*
%{_mandir}/*
