%define module   Pod-Spell
%define version    1.01
%define release    %mkrel 2

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    A formatter for spellchecking Pod
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Pod/%{module}-%{version}.tar.gz
BuildRequires: perl(Pod::Escapes)
BuildRequires: perl(Pod::Parser)
BuildRequires: perl(Text::Wrap)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README ChangeLog
%{_mandir}/man3/*
%{perl_vendorlib}/Pod
%{_bindir}/podspell

