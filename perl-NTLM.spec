%define upstream_name    NTLM
%define upstream_version 1.09
Name:		perl-%{upstream_name}
Version:	%perl_convert_version 1.09
Release:	1

Summary:	An NTLM authentication module
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Authen/NTLM-1.09.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Digest::HMAC_MD5)
BuildRequires:	perl(MIME::Base64)
BuildArch:	noarch

%description
    This module provides methods to use NTLM authentication.  It can
    be used as an authenticate method with the Mail::IMAPClient module
    to perform the challenge/response mechanism for NTLM connections
    or it can be used on its own for NTLM authentication with other
    protocols (eg. HTTP).

    The implementation is a direct port of the code from F<fetchmail>
    which, itself, has based its NTLM implementation on F<samba>.  As
    such, this code is not especially efficient, however it will still
    take a fraction of a second to negotiate a login on a PII which is
    likely to be good enough for most situations.

FUNCTIONS
    * ntlm_domain()

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sun Apr 17 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.80.0-1mdv2011.0
+ Revision: 654174
- update to new version 1.08

* Sat Feb 05 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.50.0-1
+ Revision: 636169
- import perl-NTLM


