%global debug_package %{nil}

Name:       juliaup
Version:    1.7.20
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
macchina lets you view system information, like your kernel version, uptime, memory usage, processor load and much more. macchina is basic by default and extensible by design.


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


%files
%license LICENSE
%doc README.md
%{_bindir}/juliaup
%(_bindir)/julialauncher
%(_bindir)/juliainstaller
