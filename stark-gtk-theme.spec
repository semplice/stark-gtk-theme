# Spec file for package ceru-gtk-theme
#
# Copyright (c) 2014 Sam Hewitt <hewittsamuel@gmail.com>
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.
#


Name:		stark-gtk-theme
Version:	1.0
Release:	0

Summary:	Stark GTK Theme
License:    GPL-3.0+ or CC-BY-SA-3.0

Group:      System/GUI/GNOME
Url:        http://www.mokaproject.com/stark-gtk-theme
Source0:	%{name}-%{version}.tar.gz

Requires:	stark-gtk-theme, gtk-murrine-engine
BuildArch:	noarch


%description
Stark GTK3 Theme

%prep
%setup -q

%build

%install
install -dpm 0755 $RPM_BUILD_ROOT%{_datadir}/themes/
cp -a Stark-Ceru/ $RPM_BUILD_ROOT%{_datadir}/themes/
cp -a Stark-Lutu/ $RPM_BUILD_ROOT%{_datadir}/themes/
cp -a Stark-Roja/ $RPM_BUILD_ROOT%{_datadir}/themes/
cp -a Stark-Verd/ $RPM_BUILD_ROOT%{_datadir}/themes/
cp -a Stark-Viol/ $RPM_BUILD_ROOT%{_datadir}/themes/

%files
%doc {AUTHORS,LICENSE}
%{_datadir}/themes/Stark-Ceru/
%{_datadir}/themes/Stark-Lutu/
%{_datadir}/themes/Stark-Roja/
%{_datadir}/themes/Stark-Verd/
%{_datadir}/themes/Stark-Viol/
