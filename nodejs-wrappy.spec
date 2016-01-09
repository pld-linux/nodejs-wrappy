#
# Conditional build:
%bcond_with	tests		# build with tests

%define		commit 006a8cbac6b99988315834c207896eed71fd069a
%define		pkg	wrappy
Summary:	Callback wrapping utility
Name:		nodejs-%{pkg}
Version:	1.0.1
Release:	1
License:	ISC
Group:		Development/Libraries
Source0:	https://github.com/npm/wrappy/archive/%{commit}/wrappy-%{commit}.tar.gz
# Source0-md5:	cf45c69076ebb4fcf013834b1dd9dae8
URL:		https://github.com/npm/wrappy
BuildRequires:	rpmbuild(macros) >= 1.634
BuildRequires:	sed >= 4.0
%if %{with tests}
BuildRequires:	nodejs-tap
%endif
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Callback wrapping utility for node.js

%prep
%setup -qc
mv %{pkg}-*/* .

%build
%if %{with tests}
tap test/*.js
%endif

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -p %{pkg}.js package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.md LICENSE
%{nodejs_libdir}/%{pkg}
