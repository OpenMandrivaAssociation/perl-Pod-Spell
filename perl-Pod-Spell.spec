%define modname	Pod-Spell
%define modver	1.01

Summary:	A formatter for spellchecking Pod
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	14
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}
Source0:	http://www.cpan.org/modules/by-module/Pod/%{modname}-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Pod::Escapes)
BuildRequires:	perl(Pod::Parser)
BuildRequires:	perl(Text::Wrap)
BuildRequires:	perl-devel

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
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README ChangeLog
%{_bindir}/podspell
%{perl_vendorlib}/Pod
%{_mandir}/man3/*

