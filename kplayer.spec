Summary:	MPlayer frontend for KDE
Name:		kplayer
Version:	0.7.2
Release:	1
License:	GPLv2+
Group:		Video
Url:		http://kplayer.sourceforge.net/
Source:		http://fr2.rpmfind.net/linux/KDE/stable/%name/%version/src/%name-%version.tar.xz
BuildRequires:	kdelibs4-devel
Requires:	mplayer
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
KPlayer is a KDE media player based on MPlayer. With KPlayer 
you can easily play a wide variety of video and audio files 
and streams using a rich and friendly interface that
follows KDE standards.

Features include

    * video, audio and subtitle playback from file,
       URL, DVD, VCD, audio CD, TV, DVB, etc.,
       as well as KDE I/O Slaves;
    * volume, contrast, brightness, hue and saturation controls;
    * zooming, full screen and fixed aspect options;
    * status and progress display and seeking;
    * playlist;
    * message log;
    * configuration dialog;
    * file properties for setting file specific options.

KPlayer is available in Catalonian, Czech, Danish, English,
Finnish, French, German, Hungarian, Italian, Polish, Russian, 
Simplified Chinese and Spanish. 

%prep
%setup -q -n %name-%version

%build
%cmake_kde4
%make

%install
rm -rf %{buildroot}

%makeinstall_std -C build

# fix .desktop file
desktop-file-install \
	--vendor="" \
	--remove-key="Encoding" \
	--remove-mime-type="uri/mms;uri/mmst;uri/mmsu;uri/pnm;uri/rtsp;uri/rtspt;uri/rtspu" \
	--dir %{buildroot}%{_kde_applicationsdir} %{buildroot}%{_kde_applicationsdir}/%{name}.desktop

sed -i 's,kplayer.png,kplayer,g' %{buildroot}%{_kde_applicationsdir}/%{name}.desktop

%find_lang %{name} --with-html

%clean
rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(644,root,root,755)
%attr(0755,root,root) %_kde_bindir/*
%_kde_appsdir/%name
%_kde_iconsdir/*/*/*/*
%_kde_libdir/kde4/*
%_kde_datadir/applications/kde4/*.desktop
%_kde_datadir/kde4/services/*.desktop
%_kde_datadir/kde4/services/ServiceMenus/*.desktop


%changelog
* Fri Apr 27 2012 Crispin Boylan <crisb@mandriva.org> 0.7.2-1
+ Revision: 793946
- New release

* Sat Jun 11 2011 Funda Wang <fwang@mandriva.org> 0.7.1-1
+ Revision: 684279
- new version 0.7.1

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Fri Jun 04 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 0.7-6mdv2010.1
+ Revision: 547060
- Fix crash on Exit

* Tue Mar 23 2010 Ahmad Samir <ahmadsamir@mandriva.org> 0.7-5mdv2010.1
+ Revision: 526907
- fix .desktop file
- remove '< 2009.0' parts
- clean spec

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 0.7-4mdv2010.0
+ Revision: 438164
- rebuild

* Thu Feb 12 2009 Funda Wang <fwang@mandriva.org> 0.7-3mdv2009.1
+ Revision: 339642
- fix out of source build
- fix doc dir
- fix linkage

* Mon Jul 14 2008 Funda Wang <fwang@mandriva.org> 0.7-2mdv2009.0
+ Revision: 234424
- fix perm

* Sun Jun 29 2008 Funda Wang <fwang@mandriva.org> 0.7-1mdv2009.0
+ Revision: 229986
- add file list
- move doc files into correct dir
- it does not like build subdir
- Import source and spec
- Created package structure for kde4-kplayer.

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Nicolas Lécureuil <nlecureuil@mandriva.com>
    - Fix provides // Obsoletes
    - Rename spec file and fix spec file
    - Use new name policy

