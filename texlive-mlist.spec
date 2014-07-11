# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/mlist
# catalog-date 2009-07-04 13:21:27 +0200
# catalog-license lppl
# catalog-version 0.6a
Name:		texlive-mlist
Version:	0.6a
Release:	8
Summary:	Logical markup for lists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mlist
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mlist.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mlist.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mlist.source.tar.xz
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
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 0.6a-2
+ Revision: 754022
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 0.6a-1
+ Revision: 719048
- texlive-mlist
- texlive-mlist
- texlive-mlist
- texlive-mlist

