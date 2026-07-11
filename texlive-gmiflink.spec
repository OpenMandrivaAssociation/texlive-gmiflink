%global tl_name gmiflink
%global tl_revision 15878

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.97
Release:	%{tl_revision}.1
Summary:	Simplify usage of \hypertarget and \hyperlink
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/gmiflink
License:	lppl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gmiflink.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/gmiflink.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Three hyperref-based macros that simplify usage of \hypertarget and
\hyperlink: one argument instead of the same one twice. Also \gmiflink
and \gmifref which typeset plain text instead of generating an error or
printing '??' if there is no respective hypertarget or label.

