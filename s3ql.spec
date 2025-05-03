#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

Summary:	Filesystem that stores data in Google Storage, Amazon S3 etc
Name:		s3ql
Version:	5.2.3
Release:	1
License:	GPL v3
Group:		Applications/System
Source0:	https://github.com/s3ql/s3ql/releases/download/%{name}-%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	b0b2397681fa1bb1a91c49eeb6cb78f3
URL:		https://github.com/s3ql/s3ql/
BuildRequires:	python3-Crypto
BuildRequires:	python3-Cython
BuildRequires:	python3-apsw >= 3.7.0
BuildRequires:	python3-defusedxml
BuildRequires:	python3-devel
BuildRequires:	python3-dugong >= 3.2
BuildRequires:	python3-pyfuse3
BuildRequires:	python3-modules >= 1:3.3
BuildRequires:	rpm-pythonprov
%if %{with tests}
BuildRequires:	python3-pytest-trio
BuildRequires:	python3-requests
%endif
Requires:	python3-Crypto
Requires:	python3-apsw >= 3.7.0
Requires:	python3-defusedxml
Requires:	python3-dugong >= 3.2
Requires:	python3-pyfuse3
Requires:	python3-modules >= 1:3.3
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
S3QL is a file system that stores all its data online using storage
services like Google Storage, Amazon S3, or OpenStack. S3QL
effectively provides a hard disk of dynamic, infinite capacity that
can be accessed from any computer with internet access running Linux,
FreeBSD or OS-X.

%prep
%setup -q

%build
rm src/s3ql/sqlite3ext.cpp
cython3 src/s3ql/sqlite3ext.pyx -o src/s3ql/sqlite3ext.cpp

%{py3_build}

%if %{with tests}
PYTEST_DISABLE_PLUGIN_AUTOLOAD=1 \
PYTEST_PLUGINS=trio \
%{__python3} -m pytest tests
%endif

%install
rm -rf $RPM_BUILD_ROOT

%{py3_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS README.rst
%attr(755,root,root) %{_bindir}/fsck.s3ql
%attr(755,root,root) %{_bindir}/mkfs.s3ql
%attr(755,root,root) %{_bindir}/mount.s3ql
%attr(755,root,root) %{_bindir}/s3ql*
%attr(755,root,root) %{_bindir}/umount.s3ql
%{py3_sitedir}/s3ql
%{py3_sitedir}/s3ql-%{version}-py*.egg-info
%{_mandir}/man1/*.1*
