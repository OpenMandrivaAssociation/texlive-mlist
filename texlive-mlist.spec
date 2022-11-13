Name:		texlive-mlist
Version:	15878
Release:	1
Summary:	Logical markup for lists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mlist
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mlist.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mlist.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mlist.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
The package defines commands that create macros for typesetting
vectors, matrices and functions, in a logical way. For example,
logical indexing can then be used to refer to elements or
arguments without hard-coding the symbols in the document.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mlist/mlist.cfg
%{_texmfdistdir}/tex/latex/mlist/mlist.sty
%doc %{_texmfdistdir}/doc/latex/mlist/README
%doc %{_texmfdistdir}/doc/latex/mlist/mlist.pdf
#- source
%doc %{_texmfdistdir}/source/latex/mlist/mlist.dtx
%doc %{_texmfdistdir}/source/latex/mlist/mlist.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
