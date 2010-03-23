Summary:	MPlayer frontend for KDE
Name:		kplayer
Version:	0.7
Release:	%mkrel 5
License:	GPLv2+
Group:		Video
Url:		http://kplayer.sourceforge.net/
Source:	        http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
Patch0:		kplayer-0.7-linkage.patch
Patch1:		kplayer-0.7-docdir.patch
Patch2:		kplayer-0.7-out-of-source-build.patch
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
%patch0 -p0 -b .linkage
%patch1 -p0 -b .doc
%patch2 -p0 -b .build

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
%_kde_appsdir/konqueror/servicemenus/*.desktop
%_kde_iconsdir/*/*/*/*
%_kde_libdir/kde4/*
%_kde_datadir/applications/kde4/*.desktop
%_kde_datadir/kde4/services/*.desktop
