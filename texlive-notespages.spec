%global tl_name notespages
%global tl_revision 76790

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.8.1
Release:	%{tl_revision}.1
Summary:	Filling documents with notes pages and notes areas
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/notespages
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/notespages.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/notespages.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/notespages.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This package provides one macro to insert a single notes page and
another to fill the document with multiple notes pages, until the total
number of pages (so far) is a multiple of a given number. A third
command can be used to fill half empty pages with a notes area.

