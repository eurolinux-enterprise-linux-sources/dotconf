Name:		dotconf
Version:	1.3
Release:	8%{?dist}
Summary:	Libraries to parse configuration files

Group:		System Environment/Libraries
License:	LGPLv2
URL:		http://www.azzit.de/dotconf/
#SCV https://github.com/williamh/dotconf/tags
Source:		%{name}-%{version}.tar.gz
 

%description
Dotconf is a library used to handle configuration files.

%package	devel
Summary:	Development files for %{name}
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	pkgconfig


%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q

%build
%configure --disable-static --docdir=%{_datadir}/doc/%{name}-devel-%{version}
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p"

iconv -f iso-8859-2 -t utf-8 -o iconv.tmp AUTHORS
mv iconv.tmp AUTHORS
iconv -f iso-8859-2 -t utf-8 -o iconv.tmp doc/dotconf-features.txt
mv iconv.tmp doc/dotconf-features.txt
rm examples/maketest.sh
find %{buildroot} -type f -name "*.a" -o -name "*.la" | xargs rm -f


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%doc README AUTHORS COPYING
%{_libdir}/libdotconf*.so.*

%files devel
%doc %{_docdir}
%{_libdir}/libdotconf*.so
%{_includedir}/dotconf.h
%{_libdir}/pkgconfig/dotconf.pc

%changelog
* Fri Jan 24 2014 Daniel Mach <dmach@redhat.com> - 1.3-8
- Mass rebuild 2014-01-24

* Fri Dec 27 2013 Daniel Mach <dmach@redhat.com> - 1.3-7
- Mass rebuild 2013-12-27

* Tue Jul 16 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.3-6
- Fix multilib issues (thanks Rui Matos)

* Tue Feb  5 2013 Peter Robinson <pbrobinson@fedoraproject.org> 1.3-5
- Update URLs and note github SCV url

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Wed Dec  8 2010 Peter Robinson <pbrobinson@fedoraproject.org> - 1.3-1
- New upstream 1.3 release, update URL/Source

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.13-8
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Thu Jul 03 2008 Mamoru Tasaka <mtasaka@ioa.s.u-tokyo.ac.jp> - 1.0.13-7
- Override config.{sub,guess} explicitly due to redhat-rpm-build-config
  behavior change on F-10+, otherwise build fails on ppc64

* Sun Mar 09 2008 Assim Deodia<assim.deodia@gmail.com> 1.0.13-6
- fixed m4-underquote error

* Fri Feb 29 2008 Assim Deodia<assim.deodia@gmail.com> 1.0.13-5
- fixed AUTHORS utf-8
- fixed doc/dotconf-features.txt utf-8

* Sat Feb 23 2008 Assim Deodia<assim.deodia@gmail.com> 1.0.13-4
- Applied patch macro

* Sat Feb 23 2008 Assim Deodia<assim.deodia@gmail.com> 1.0.13-3
- Resolved Multilib issue

* Fri Feb 22 2008 Assim Deodia<assim.deodia@gmail.com> 1.0.13-2
- Inclusion of pkgconfig
- Removal of INSTALL file
- Proper placement of Library files
- Creating devel sub-package
- Chaning source URL

* Sun Feb 17 2008 Assim Deodia<assim.deodia@gmail.com> 1.0.13-1
- Initial Commit
