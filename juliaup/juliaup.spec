%global debug_package %{nil}

Name:       juliaup
Version:    1.7.21
Release:    1%{?dist}
Summary:    Julia installer and version multiplexer.

License:    MIT
URL:        https://github.com/JuliaLang/juliaup
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

%if 0%{?el8}
%else
BuildRequires: cargo >= 1.39
BuildRequires: rust >= 1.39
%endif

%description
One can use juliaup to install specific Julia versions, it alerts users when new Julia versions are released and provides a convenient Julia release channel abstraction.

%prep
%autosetup -p1
%if 0%{?el8}
  curl https://sh.rustup.rs -sSf | sh -s -- --profile minimal -y
%endif

%install
export CARGO_PROFILE_RELEASE_BUILD_OVERRIDE_OPT_LEVEL=3
%if 0%{?el8}
  $HOME/.cargo/bin/cargo install --root=%{buildroot}%{_prefix} --path=.
%else
  cargo install --root=%{buildroot}%{_prefix} --path=.
%endif

rm -f %{buildroot}%{_prefix}/.crates.toml \
    %{buildroot}%{_prefix}/.crates2.json
strip --strip-all %{buildroot}%{_bindir}/*
ln -s %{_bindir}/julialauncher %{_bindir}/julia


%files
%license LICENSE
%doc README.md
%{_bindir}/juliaup
%{_bindir}/julialauncher
%{_bindir}/juliainstaller
%{_bindir}/julia
