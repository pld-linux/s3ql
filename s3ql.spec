#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

Summary:	Filesystem that stores data in Google Storage, Amazon S3 etc
Name:		s3ql
Version:	2.11.1
Release:	6
License:	GPL v3
Group:		Applications/System
Source0:	https://bitbucket.org/nikratio/s3ql/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	8d7f00e6af7013261288a94ac93f8bc1
URL:		https://bitbucket.org/nikratio/s3ql/
BuildRequires:	python3-Crypto
BuildRequires:	python3-apsw >= 3.7.0
BuildRequires:	python3-defusedxml
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-dugong >= 3.2
BuildRequires:	python3-llfuse >= 0.39
BuildRequires:	python3-modules >= 3.3
BuildRequires:	rpm-pythonprov
%{?with_tests:BuildRequires:	python3-requests}
Requires:	python3-Crypto
Requires:	python3-apsw >= 3.7.0
Requires:	python3-defusedxml
Requires:	python3-dugong >= 3.2
Requires:	python3-llfuse >= 0.39
Requires:	python3-modules >= 3.3
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
%{py3_build} \
	%{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%{py3_install}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes.txt README.rst
%attr(755,root,root) %{_bindir}/fsck.s3ql
%attr(755,root,root) %{_bindir}/mkfs.s3ql
%attr(755,root,root) %{_bindir}/mount.s3ql
%attr(755,root,root) %{_bindir}/s3ql*
%attr(755,root,root) %{_bindir}/umount.s3ql
%{py3_sitedir}/s3ql
%{py3_sitedir}/s3ql-%{version}-py*.egg-info
%{_mandir}/man1/*.1*
