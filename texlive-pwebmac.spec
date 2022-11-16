Name:		texlive-pwebmac
Version:	63731
Release:	1
Summary:	Consolidated WEB macros for DVI and PDF output
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/pwebmac
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pwebmac.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pwebmac.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The original WEB system by Donald Knuth has the macros
webmac.tex that produce DVI output only; for historic reasons,
it will never be modified (apart from catastrophic errors). Han
The Thanh has modified these macros in his pdfwebmac.tex for
PDF output (only) with pdfTeX. Jonathan Kew's XeTeX has similar
macros xewebmac.tex by Khaled Hosny that modify webmac.tex for
PDF output; these macros can only be used with a specific "TeX
engine" each. The present pwebmac package integrates these
three WEB macro files similar to cwebmac.tex in Silvio Levy's
and Don Knuth's CWEB system, so pwebmac.tex can be used with
"plain TeX", pdfTeX, and XeTeX alike. Its initial application
is the production of PDF files for all major WEB programs for
"TeX and friends" as distributed in TeX Live. For this purpose,
the shell script makeall was whipped together; it provides
various commandline options and works around several "quirks"
in the WEB sources. WEB programmers who want to use pwebmac.tex
instead of the default webmac.tex in their programs have to
change the first line in the TeX file created by weave. From
there, all depends on the "TeX engine" you use.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/plain/pwebmac
%doc %{_texmfdistdir}/doc/plain/pwebmac

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
