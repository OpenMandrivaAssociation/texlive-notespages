Name:		texlive-notespages
Version:	41906
Release:	2
Summary:	Filling documents with notes pages and notes areas
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/notespages
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/notespages.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/notespages.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/notespages.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This package package provides one macro to insert a single
notes page and another to fill the document with multiple notes
pages, until the total number of pages (so far) is a multiple
of a given number. A third command can be used to fill half
empty pages with a notes area.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/notespages
%{_texmfdistdir}/tex/latex/notespages
%doc %{_texmfdistdir}/doc/latex/notespages

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
