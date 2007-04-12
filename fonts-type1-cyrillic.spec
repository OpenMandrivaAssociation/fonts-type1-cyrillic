Summary:	Cyrillic Type1 fonts
Name:		fonts-type1-cyrillic
Version:	1.1
Release:	%mkrel 6

# The "TopTeam" bulgarian company kindly donated good quality
# PS Type1 cyrillic font "Teams" to X community !
# info from: "Alexander Voropay" <a.voropay@globalone.ru>
Source0:	http://www.sensi.org/download/teams-1.1.tar.gz
#
Source1:	oldslavic.tar.bz2

License:	Free
Group:		System/Fonts/Type1
BuildArch:	noarch
BuildRoot:	%_tmppath/%name-%version-%release-root
BuildRequires:	freetype-tools
Requires(post): fontconfig
Requires(postun): fontconfig

%description
Scalable fonts including common Cyrillic glyphs

%prep

%setup -n teams -a1 -q
mv doc teams
mkdir oldslavic
cp README COPYING oldslavic/

%build
cat > README << EOF
The "Teams" fonts are under X11 licence, see under the teams/ directory

The "OldSlavic" font is under the GPL, see under the oldslavic/ directory
EOF

%install
rm -fr %buildroot

install -d %buildroot/%_datadir/fonts/type1/cyrillic/
install -d %buildroot/%_datadir/fonts/afms/cyrillic/
install -m 0644 *.pfb %buildroot/%_datadir/fonts/type1/cyrillic
# the *.pfb files don't show up in Xft; installing the *.pfa ones
install -m 0644 Teams/*.pfa %buildroot/%_datadir/fonts/type1/cyrillic
# 
install -m 0644 *.afm %buildroot/%_datadir/fonts/afms/cyrillic/
install -m 0644 Teams/*.afm %buildroot/%_datadir/fonts/afms/cyrillic/

(
cd %buildroot/%_datadir/fonts/type1/cyrillic
# OOo requries afm files in same dire as fonts
ln ../../afms/cyrillic/*.afm .
)

# not listed in xfs, as the fonts don't cover any of the X11 encodings
# they only have basic cyrillic

%clean
rm -fr %buildroot

%postun
# 0 means a real uninstall
if [ "$1" = "0" ]; then
   [ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache
fi

%post
touch %{_datadir}/fonts/type1
[ -x %_bindir/fc-cache ] && %{_bindir}/fc-cache

%files
%defattr(0644,root,root,0755)
%doc README* teams/ oldslavic/
%dir %_datadir/fonts/afms/
%dir %_datadir/fonts/afms/cyrillic
%_datadir/fonts/afms/cyrillic/*.afm
%dir %_datadir/fonts/type1/
%dir %_datadir/fonts/type1/cyrillic
%_datadir/fonts/type1/cyrillic/*.pfa
%_datadir/fonts/type1/cyrillic/*.pfb
%_datadir/fonts/type1/cyrillic/*.afm


