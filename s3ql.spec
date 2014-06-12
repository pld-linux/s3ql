#
# Conditional build:
%bcond_without	tests	# do not perform "make test"

Summary:	Filesystem that stores data in Google Storage, Amazon S3 etc
Name:		s3ql
Version:	2.8.1
Release:	1
License:	GPL v3
Group:		Applications/System
Source0:	https://bitbucket.org/nikratio/s3ql/downloads/%{name}-%{version}.tar.bz2
# Source0-md5:	b0c173fa97a0b4b77caa3fd66022f228
URL:		https://bitbucket.org/nikratio/s3ql/
BuildRequires:	python3-Crypto
BuildRequires:	python3-apsw
BuildRequires:	python3-devel
BuildRequires:	python3-distribute
BuildRequires:	python3-dugong
BuildRequires:	python3-modules
BuildRequires:	rpm-pythonprov
Requires:	python3-Crypto
Requires:	python3-apsw
Requires:	python3-dugong
Requires:	python3-llfuse
Requires:	python3-modules
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
CC="%{__cc}" \
CFLAGS="%{rpmcflags}" \
%{__python3} setup.py build --build-base build-3 %{?with_tests:test}

%install
rm -rf $RPM_BUILD_ROOT

%{__python3} setup.py \
	build --build-base build-3 \
	install --skip-build \
	--optimize=2 \
	--root=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CREDITS.txt Changes.txt INSTALL.txt README.rst
%attr(755,root,root) %{_bindir}/fsck.s3ql
%attr(755,root,root) %{_bindir}/mkfs.s3ql
%attr(755,root,root) %{_bindir}/mount.s3ql
%attr(755,root,root) %{_bindir}/s3ql*
%attr(755,root,root) %{_bindir}/umount.s3ql
%{py3_sitedir}/s3ql
%{py3_sitedir}/s3ql-%{version}-py*.egg-info
%{_mandir}/man1/*.1*
