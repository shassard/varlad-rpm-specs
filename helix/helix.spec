%global debug_package %{nil}

Name:       helix
Version:    22.03
Release:    1%{?dist}
Summary:    A post-modern modal text editor.

License:    MPL-2.0
URL:        https://github.com/helix-editor/helix
Source0:    %{url}/releases/download/%{version}/helix-%{version}-x86_64-linux.tar.xz

%description
A kakoune / neovim inspired editor, written in Rust.
The editing model is very heavily based on kakoune.
Features include Vim-like modal editing, multiple selections, built-in language server support and smart, incremental syntax highlighting and code editing via tree-sitter


%prep
%autosetup -n helix-v%{version}-x86_64-linux

%install
mkdir -p %{buildroot}%{_datadir}/helix
mv ./runtime %{buildroot}%{_datadir}/helix
mv hx %{buildroot}%{_datadir}/helix/hx
mkdir -p %{buildroot}%{_datadir}/licenses/helix
mv LICENSE %{buildroot}%{_datadir}/licenses/helix/LICENSE
mkdir -p %{buildroot}%{_docdir}/helix
mv README.md %{buildroot}%{_docdir}/helix/README.md

mkdir -p %{buildroot}%{_bindir}
touch %{buildroot}%{_bindir}/hx
cat >> %{buildroot}%{_bindir}/hx <<EOF
#!/usr/bin/env sh

HELIX_RUNTIME="%{_datadir}/helix/runtime" exec %{_datadir}/helix/hx "\$@"
EOF
chmod +x %{buildroot}%{_prefix}/bin/hx

%files
%license LICENSE
%doc README.md
%{_bindir}/hx
%{_datadir}/helix/

