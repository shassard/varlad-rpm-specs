%global debug_package %{nil}

Name:       onefetch
Version:    2.11.0
Release:    1%{?dist}
Summary:    Git repository summary on your terminal 

License:    MIT
URL:        https://github.com/o2sh/onefetch
Source0:    %{url}/archive/refs/tags/v%{version}.tar.gz

%if 0%{?el8}
%else
BuildRequires: cargo >= 1.39
BuildRequires: rust >= 1.39
%endif
BuildRequires: gcc
BuildRequires: python3-devel

%description
Onefetch is a command-line Git information tool written in Rust that displays project information and code statistics for a local Git repository directly on your terminal. The tool is completely offline - no network access is required.
By default, the repo's information is displayed alongside the dominant language's logo, but you can further configure onefetch to instead use an image - on supported terminals -, a text input or nothing at all.
It automatically detects open source licenses from texts and provides the user with valuable information like code distribution, pending changes, number of dependencies (by package manager), top contributors (by number of commits), size on disk, creation date, LOC (lines of code), etc.
Onefetch can be configured via command-line flags to display exactly what you want, the way you want it to: you can customize ASCII/Text formatting, disable info lines, ignore files & directories, output in multiple formats (Json, Yaml), etc.
As of now, onefetch supports more than 50 different programming languages; if your language of choice isn't supported: Open up an issue and support will be added.


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
%license LICENSE.md
%doc README.md
%{_bindir}/onefetch
