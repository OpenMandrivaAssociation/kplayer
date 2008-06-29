Summary:	MPlayer frontend for KDE
Name:		kplayer
Version:	0.7
Release:	%mkrel 1
License:	GPLv2+
Group:		Video
Url:		http://kplayer.sourceforge.net/
Source:	        http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
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
%setup_compile_flags
cmake . \
	-DCMAKE_INSTALL_PREFIX:PATH=%{_kde_prefix} \
	-DKDE_DISTRIBUTION_TEXT="Mandriva Linux release 2009.0 (Cooker) for x86_64" \
	-DKDE4_DATA_DIR=%{_kde_appsdir} \
    %if "%{_lib}" != "lib"
        -DLIB_SUFFIX=64
    %endif

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

cd %buildroot%_kde_datadir/doc/HTML
for i in *
do 
	mkdir $i/%name
	mv `find $i -type f` `find $i -type l` $i/%name/
done
cd -


%find_lang %{name} --with-html

%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(644,root,root,755)
%_kde_bindir/*
%_kde_appsdir/%name
%_kde_appsdir/konqueror/servicemenus/*.desktop
%_kde_iconsdir/*/*/*/*
%_kde_libdir/kde4/*
%_kde_datadir/applications/kde4/*.desktop
%_kde_datadir/kde4/services/*.desktop
