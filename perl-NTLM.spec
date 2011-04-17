%define upstream_name    NTLM
%define upstream_version 1.08

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    An NTLM authentication module
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Authen/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Digest::HMAC_MD5)
BuildRequires: perl(MIME::Base64)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


