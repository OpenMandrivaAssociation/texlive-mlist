# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/mlist
# catalog-date 2009-07-04 13:21:27 +0200
# catalog-license lppl
# catalog-version 0.6a
Name:		texlive-mlist
Version:	0.6a
Release:	1
Summary:	Logical markup for lists
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mlist
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mlist.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mlist.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mlist.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
The package defines commands that create macros for typesetting
vectors, matrices and functions, in a logical way. For example,
logical indexing can then be used to refer to elements or
arguments without hard-coding the symbols in the document.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
