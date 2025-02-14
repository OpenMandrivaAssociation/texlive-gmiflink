Name:		texlive-gmiflink
Version:	15878
Release:	2
Summary:	Simplify usage of \hypertarget and \hyperlink
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gmiflink
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmiflink.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/gmiflink.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
