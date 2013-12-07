Name:           kcm-drakauth
BuildRequires:  kdelibs4-devel
License:        GPLv3+
Group:          Graphical desktop/KDE
Summary:        A KDE Control Module for launching drakauth
Version:        1.0
Release:        5
BuildArch:      noarch
Source0:        %{name}-%{version}.tar.gz

%description
Drakauth launcher for KDE Control Center

%prep
%setup -q

%build
%cmake_kde4

%install
%makeinstall_std -C build

%files
%defattr(-,root,root)
%doc
%{_datadir}/kde4/services/kcm_drakauth.desktop

