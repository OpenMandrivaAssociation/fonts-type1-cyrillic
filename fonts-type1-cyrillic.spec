Summary:	Cyrillic Type1 fonts
Name:		fonts-type1-cyrillic
Version:	1.1
Release:	%mkrel 16

# The "TopTeam" bulgarian company kindly donated good quality
# PS Type1 cyrillic font "Teams" to X community.
# info from: "Alexander Voropay" <a.voropay@globalone.ru>
Source0:	http://www.sensi.org/download/teams-1.1.tar.gz
#
Source1:	oldslavic.tar.bz2
License:	GPL+ and MIT
Group:		System/Fonts/Type1
BuildArch:	noarch
BuildRequires: fontconfig
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	freetype-tools
BuildRequires:	mkfontdir

%description
Scalable fonts including common Cyrillic glyphs.

%prep

%setup -n teams -a1 -q
mv doc teams
mkdir oldslavic
cp README COPYING oldslavic/

%build

%install
rm -fr %buildroot

install -d %buildroot/%_datadir/fonts/type1/cyrillic/
install -m 0644 *.pfb %buildroot/%_datadir/fonts/type1/cyrillic
# the *.pfb files don't show up in Xft; installing the *.pfa ones
install -m 0644 Teams/*.pfa %buildroot/%_datadir/fonts/type1/cyrillic
# 
install -m 0644 *.afm %buildroot/%_datadir/fonts/type1/cyrillic/
install -m 0644 Teams/*.afm %buildroot/%_datadir/fonts/type1/cyrillic/

mkfontdir %buildroot/%_datadir/fonts/type1/cyrillic
cp %buildroot/%_datadir/fonts/type1/cyrillic/fonts.dir %buildroot/%_datadir/fonts/type1/cyrillic/fonts.scale

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/type1/cyrillic \
    %{buildroot}%_sysconfdir/X11/fontpath.d/type1-cyrillic:pri=50

# not listed in xfs, as the fonts don't cover any of the X11 encodings
# they only have basic cyrillic

%clean
rm -fr %buildroot

%post
touch %{_datadir}/fonts/type1

%files
%defattr(0644,root,root,0755)
%doc README* teams/ oldslavic/
%_datadir/fonts/type1/cyrillic
%_sysconfdir/X11/fontpath.d/type1-cyrillic:pri=50



%changelog
* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.1-15mdv2011.0
+ Revision: 675432
- br fontconfig for fc-query used in new rpm-setup-build

* Tue May 17 2011 Funda Wang <fwang@mandriva.org> 1.1-14
+ Revision: 675191
- rebuild for new rpm-setup

* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1-13
+ Revision: 664341
- mass rebuild

* Thu Dec 02 2010 Oden Eriksson <oeriksson@mandriva.com> 1.1-12mdv2011.0
+ Revision: 605207
- rebuild

* Wed Jan 20 2010 Paulo Ricardo Zanoni <pzanoni@mandriva.com> 1.1-11mdv2010.1
+ Revision: 494121
- fc-cache is now called by an rpm filetrigger

* Tue Jun 17 2008 Thierry Vignaud <tv@mandriva.org> 1.1-10mdv2009.0
+ Revision: 220957
- rebuild

* Tue Mar 04 2008 Oden Eriksson <oeriksson@mandriva.com> 1.1-9mdv2008.1
+ Revision: 178722
- rebuild

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Wed Sep 19 2007 Adam Williamson <awilliamson@mandriva.org> 1.1-7mdv2008.0
+ Revision: 90331
- buildrequires mkfontdir
- rebuild for 2008
- adapt to new font policies
- new license policy
- clean spec


* Fri Nov 03 2006 Pablo Saratxaga <pablo@mandriva.com> 1.1-6mdv2007.0
+ Revision: 76298
- Import fonts-type1-cyrillic

* Fri Nov 03 2006 Pablo Saratxaga <pablo@mandriva.com> 1.1-6mdv2007.1
- use mkrel
- fixed package Group

* Wed Feb 08 2006 Frederic Crozat <fcrozat@mandriva.com> 1.1-5mdk
- Don't package fontconfig cache file
- Fix prereq
- touch parent directory to workaround rpm changing directory last modification
  time (breaking fontconfig cache consistency detection)

