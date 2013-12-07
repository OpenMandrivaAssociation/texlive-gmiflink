# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/gmiflink
# catalog-date 2008-08-13 17:41:00 +0200
# catalog-license lppl
# catalog-version v0.97
Name:		texlive-gmiflink
Version:	v0.97
Release:	6
Summary:	Simplify usage of \hypertarget and \hyperlink
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/gmiflink
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmiflink.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmiflink.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Three hyperref-based macros that simplify usage of \hypertarget
and \hyperlink: one argument instead of the same one twice.
Also \gmiflink and \gmifref which typeset plain text instead of
generating an error or printing '??' if there is no respective
hypertarget or label.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/gmiflink/gmiflink.sty
%doc %{_texmfdistdir}/doc/latex/gmiflink/README
%doc %{_texmfdistdir}/doc/latex/gmiflink/gmiflink.pdf

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> v0.97-2
+ Revision: 752360
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> v0.97-1
+ Revision: 718565
- texlive-gmiflink
- texlive-gmiflink
- texlive-gmiflink
- texlive-gmiflink

