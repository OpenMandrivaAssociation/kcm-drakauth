# These macros are not present on the target distribution and are provided explicitly here
%define make_jobs %{__make} %{?_smp_mflags} VERBOSE=1

%define _kde4_configkcfgdir %{_kde4_sharedir}/config.kcfg

Name:           kcm-drakauth
BuildRequires:  kdelibs4-devel
License:        GPLv3+
Group:          Graphical desktop/KDE
Summary:        A KDE Control Module for launching drakauth
Version:        1.0
Release:        4
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

