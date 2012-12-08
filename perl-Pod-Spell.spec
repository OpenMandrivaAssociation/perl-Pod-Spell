%define upstream_name    Pod-Spell
%define upstream_version 1.01

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	A formatter for spellchecking Pod
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Pod::Escapes)
BuildRequires:	perl(Pod::Parser)
BuildRequires:	perl(Text::Wrap)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Pod::Spell is a Pod formatter whose output is good for spellchecking.
Pod::Spell rather like Pod::Text, except that it doesn't put much effort
into actual formatting, and it suppresses things that look like Perl
symbols or Perl jargon (so that your spellchecking program won't complain
about mystery words like "'$thing'" or "'Foo::Bar'" or "hashref").

This class provides no new public methods. All methods of interest are
inherited from Pod::Parser (which see). The especially interesting ones are
'parse_from_filehandle' (which without arguments takes from STDIN and sends
to STDOUT) and 'parse_from_file'. But you can probably just make do with
the examples in the synopsis though.

This class works by filtering out words that look like Perl or any form of
computerese (like "'$thing'" or "'N>7'" or "'@{$foo}{'bar','baz'}'",
anything in C<...> or F<...> codes, anything in verbatim paragraphs
(codeblocks), and anything in the stopword list. The default stopword list
for a document starts out from the stopword list defined by Pod::Wordlist,
and can be supplemented (on a per-document basis) by having '"=for
stopwords"' / '"=for :stopwords"' region(s) in a document.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README ChangeLog
%{_mandir}/man3/*
%{perl_vendorlib}/Pod
%{_bindir}/podspell


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.10.0-4mdv2012.0
+ Revision: 765601
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.10.0-3
+ Revision: 764129
- rebuilt for perl-5.14.x

* Sat May 21 2011 Oden Eriksson <oeriksson@mandriva.com> 1.10.0-2
+ Revision: 676773
- rebuild

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.10.0-1mdv2010.0
+ Revision: 404295
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.01-2mdv2009.0
+ Revision: 268714
- rebuild early 2009.0 package (before pixel changes)

* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2009.0
+ Revision: 213742
- import perl-Pod-Spell


* Sat May 31 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.01-1mdv2009.0
- first mdv release
