Summary:	Cyrillic Type1 fonts
Name:		fonts-type1-cyrillic
Version:	1.1
Release:	27
License:	GPLv2 and MIT
Group:		System/Fonts/Type1
# The "TopTeam" bulgarian company kindly donated good quality
# PS Type1 cyrillic font "Teams" to X community.
# info from: "Alexander Voropay" <a.voropay@globalone.ru>
Source0:	http://www.sensi.org/download/teams-1.1.tar.gz
Source1:	oldslavic.tar.bz2
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	freetype-tools
BuildRequires:	mkfontdir

%description
Scalable fonts including common Cyrillic glyphs.

%prep
%setup -qn teams -a1
mv doc teams
mkdir oldslavic
cp README COPYING oldslavic/

%build

%install
install -d %{buildroot}/%{_datadir}/fonts/type1/cyrillic/
install -m 0644 *.pfb %{buildroot}/%{_datadir}/fonts/type1/cyrillic
# the *.pfb files don't show up in Xft; installing the *.pfa ones
install -m 0644 Teams/*.pfa %{buildroot}/%{_datadir}/fonts/type1/cyrillic
# 
install -m 0644 *.afm %{buildroot}/%{_datadir}/fonts/type1/cyrillic/
install -m 0644 Teams/*.afm %{buildroot}/%{_datadir}/fonts/type1/cyrillic/

mkfontdir %{buildroot}/%{_datadir}/fonts/type1/cyrillic
cp %{buildroot}/%{_datadir}/fonts/type1/cyrillic/fonts.dir %{buildroot}/%{_datadir}/fonts/type1/cyrillic/fonts.scale

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/type1/cyrillic \
    %{buildroot}%{_sysconfdir}/X11/fontpath.d/type1-cyrillic:pri=50

# not listed in xfs, as the fonts don't cover any of the X11 encodings
# they only have basic cyrillic

%post
touch %{_datadir}/fonts/type1

%files
%doc README* teams/ oldslavic/
%{_datadir}/fonts/type1/cyrillic
%{_sysconfdir}/X11/fontpath.d/type1-cyrillic:pri=50

