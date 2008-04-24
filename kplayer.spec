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
%cmake_kde4
make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}
cd build
%makeinstall_std
cd ..

%find_lang %{name}

%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor

%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -f %{name}.lang
%defattr(644,root,root,755)
