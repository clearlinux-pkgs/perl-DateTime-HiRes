#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: cpan
# autospec version: v25
# autospec commit: 9594167
#
Name     : perl-DateTime-HiRes
Version  : 0.04
Release  : 12
URL      : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-HiRes-0.04.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DR/DROLSKY/DateTime-HiRes-0.04.tar.gz
Summary  : 'Create DateTime objects with sub-second current time resolution'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-DateTime-HiRes-license = %{version}-%{release}
Requires: perl-DateTime-HiRes-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(DateTime)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
# NAME
DateTime::HiRes - Create DateTime objects with sub-second current time resolution

%package dev
Summary: dev components for the perl-DateTime-HiRes package.
Group: Development
Provides: perl-DateTime-HiRes-devel = %{version}-%{release}
Requires: perl-DateTime-HiRes = %{version}-%{release}

%description dev
dev components for the perl-DateTime-HiRes package.


%package license
Summary: license components for the perl-DateTime-HiRes package.
Group: Default

%description license
license components for the perl-DateTime-HiRes package.


%package perl
Summary: perl components for the perl-DateTime-HiRes package.
Group: Default
Requires: perl-DateTime-HiRes = %{version}-%{release}

%description perl
perl components for the perl-DateTime-HiRes package.


%prep
%setup -q -n DateTime-HiRes-0.04
cd %{_builddir}/DateTime-HiRes-0.04

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} -I. Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DateTime-HiRes
cp %{_builddir}/DateTime-HiRes-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/perl-DateTime-HiRes/95a011b714b86bd1b5de31bf9a3a7e8095af545f || :
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DateTime::HiRes.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DateTime-HiRes/95a011b714b86bd1b5de31bf9a3a7e8095af545f

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
