Name:           ros-hydro-dynamic-edt-3d
Version:        1.6.8
Release:        0%{?dist}
Summary:        ROS dynamic_edt_3d package

Group:          Development/Libraries
License:        BSD
URL:            http://octomap.github.io
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-hydro-catkin
Requires:       ros-hydro-octomap
BuildRequires:  cmake
BuildRequires:  ros-hydro-octomap

%description
The dynamicEDT3D library implements an inrementally updatable Euclidean distance
transform (EDT) in 3D. It comes with a wrapper to use the OctoMap 3D
representation and hooks into the change detection of the OctoMap library to
propagate changes to the EDT.

%prep
%setup -q

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
mkdir -p build && cd build
%cmake .. \
        -UINCLUDE_INSTALL_DIR \
        -ULIB_INSTALL_DIR \
        -USYSCONF_INSTALL_DIR \
        -USHARE_INSTALL_PREFIX \
        -ULIB_SUFFIX \
        -DCMAKE_INSTALL_PREFIX="/opt/ros/hydro" \
        -DCMAKE_PREFIX_PATH="/opt/ros/hydro" \
        -DSETUPTOOLS_DEB_LAYOUT=OFF \
        -DCATKIN_BUILD_BINARY_PACKAGE="1" \

make %{?_smp_mflags}

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree that was dropped by catkin, and source it.  It will
# set things like CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/hydro/setup.sh" ]; then . "/opt/ros/hydro/setup.sh"; fi
cd build
make %{?_smp_mflags} install DESTDIR=%{buildroot}

%files
/opt/ros/hydro

%changelog
* Sat Sep 06 2014 Christoph Sprunk <sprunkc@informatik.uni-freiburg.de> - 1.6.8-0
- Autogenerated by Bloom

