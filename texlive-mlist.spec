%global tl_name mlist
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.6a
Release:	%{tl_revision}.1
Summary:	Logical markup for lists
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mlist
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mlist.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mlist.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mlist.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The package defines commands that create macros for typesetting vectors,
matrices and functions, in a logical way. For example, logical indexing
can then be used to refer to elements or arguments without hard-coding
the symbols in the document.

