#
# Conditional build:
%bcond_with	java	# build db-java (required for openoffice)
%bcond_without	tcl	# don't build Tcl bindings
%bcond_with	pmutex	# use POSIX mutexes (only process-private with linuxthreads)
%bcond_with	nptl	# synonym for pmutex (NPTL provides full interface)
#
%{?with_nptl:%define	with_pmutex	1}
Summary:	Berkeley DB database library for C
Summary(pl):	Biblioteka C do obs³ugi baz Berkeley DB
Name:		db4.3
Version:	4.3.21
Release:	0.1
License:	Sleepycat public license (GPL-like, see LICENSE)
Group:		Libraries
# alternative site (sometimes working): http://www.berkeleydb.com/
#Source0Download: http://www.sleepycat.com/download/
Source0:	http://www.sleepycat.com/update/snapshot/db-%{version}.tar.gz
# Source0-md5:	014950aaadd531f6f9064c81a2018423
URL:		http://www.sleepycat.com/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	ed
%{?with_java:BuildRequires:	jdk}
BuildRequires:	libtool
BuildRequires:	libstdc++-devel
BuildRequires:	sed >= 4.0
%{?with_tcl:BuildRequires:	tcl-devel >= 8.4.0}
Obsoletes:	db4
BuildRoot:	%{tmpdir}/db-%{version}-root-%(id -u -n)

%description
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB is used by many applications,
including Python and Perl, so this should be installed on all systems.

%description -l pl
Berkeley Database (Berkeley DB) to zestaw narzêdzi programistycznych
zapewniaj±cych obs³ugê baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley db jest u¿ywana w wielu aplikacjach, w tym w
Pythonie i Perlu.

%package devel
Summary:	Header files for Berkeley database library
Summary(pl):	Pliki nag³ówkowe do biblioteki Berkeley Database
Group:		Development/Libraries
Requires:	db = %{epoch}:%{version}-%{release}
Obsoletes:	db3-devel
Obsoletes:	db4-devel

%description devel
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching and database
recovery. DB supports C, C++, Java and Perl APIs.

This package contains the header files, libraries, and documentation
for building programs which use Berkeley DB.

%description devel -l pl
Berkeley Database (Berkeley DB) to zestaw narzêdzi programistycznych
zapewniaj±cych obs³ugê baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley DB obs³uguje dostêp do bazy przez B-drzewa i
funkcje mieszaj±ce ze sta³± lub zmienn± wielko¶ci± rekordu,
transakcje, kroniki, pamiêæ dzielon± i odtwarzanie baz. Ma wsparcie
dla C, C++, Javy i Perla.

Ten pakiet zawiera pliki nag³ówkowe i dokumentacjê do budowania
programów u¿ywaj±cych Berkeley DB.

%package static
Summary:	Static libraries for Berkeley database library
Summary(pl):	Statyczne biblioteki Berkeley Database
Group:		Development/Libraries
Requires:	db-devel = %{epoch}:%{version}-%{release}
Obsoletes:	db3-static
Obsoletes:	db4-static

%description static
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching and database
recovery. DB supports C, C++, Java and Perl APIs.

This package contains the static libraries for building programs which
use Berkeley DB.

%description static -l pl
Berkeley Database (Berkeley DB) to zestaw narzêdzi programistycznych
zapewniaj±cych obs³ugê baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley DB obs³uguje dostêp do bazy przez B-drzewa i
funkcje mieszaj±ce ze sta³± lub zmienn± wielko¶ci± rekordu,
transakcje, kroniki, pamiêæ dzielon± i odtwarzanie baz. Ma wsparcie
dla C, C++, Javy i Perla.

Ten pakiet zawiera statyczne biblioteki do budowania programów
u¿ywaj±cych Berkeley DB.

%package cxx
Summary:	Berkeley database library for C++
Summary(pl):	Biblioteka baz danych Berkeley dla C++
Group:		Libraries
Obsoletes:	db4-cxx

%description cxx
Berkeley database library for C++.

%description cxx -l pl
Biblioteka baz danych Berkeley dla C++.

%package cxx-devel
Summary:	Header files for db-cxx library
Summary(pl):	Pliki nag³ówkowe biblioteki db-cxx
Group:		Development/Libraries
Requires:	db-cxx = %{epoch}:%{version}-%{release}
Requires:	db-devel = %{epoch}:%{version}-%{release}
Conflicts:	db-devel < 4.1.25-3

%description cxx-devel
Header files for db-cxx library.

%description cxx-devel -l pl
Pliki nag³ówkowe biblioteki db-cxx.

%package cxx-static
Summary:	Static version of db-cxx library
Summary(pl):	Statyczna wersja biblioteki db-cxx
Group:		Development/Libraries
Requires:	db-cxx-devel = %{epoch}:%{version}-%{release}
Conflicts:	db-static < 4.2.50-1

%description cxx-static
Static version of db-cxx library.

%description cxx-static -l pl
Statyczna wersja biblioteki db-cxx.

%package java
Summary:	Berkeley database library for Java
Summary(pl):	Biblioteka baz danych Berkeley dla Javy
Group:		Libraries
Requires:	jre

%description java
Berkeley database library for Java.

%description java -l pl
Biblioteka baz danych Berkeley dla Javy.

%package java-devel
Summary:	Development files for db-java library
Summary(pl):	Pliki programistyczne biblioteki db-java
Group:		Development/Languages/Java
Requires:	db-java = %{epoch}:%{version}-%{release}
Conflicts:	db-devel < 4.1.25-3

%description java-devel
Development files for db-java library.

%description java-devel -l pl
Pliki programistyczne biblioteki db-java.

%package tcl
Summary:	Berkeley database library for Tcl
Summary(pl):	Biblioteka baz danych Berkeley dla Tcl
Group:		Development/Languages/Tcl
Requires:	tcl
Obsoletes:	db4-tcl

%description tcl
Berkeley database library for Tcl.

%description tcl -l pl
Biblioteka baz danych Berkeley dla Tcl.

%package tcl-devel
Summary:	Development files for db-tcl library
Summary(pl):	Pliki programistyczne biblioteki db-tcl
Group:		Development/Languages/Tcl
Requires:	tcl
Requires:	db-tcl = %{epoch}:%{version}-%{release}
Conflicts:	db-devel < 4.1.25-3

%description tcl-devel
Development files for db-tcl library.

%description tcl-devel -l pl
Pliki programistyczne biblioteki db-tcl.

%package utils
Summary:	Command line tools for managing Berkeley DB databases
Summary(pl):	Narzêdzia do obs³ugi baz Berkeley DB z linii poleceñ
Group:		Applications/Databases
Requires:	db = %{epoch}:%{version}-%{release}
Obsoletes:	db4-utils

%description utils
The Berkeley Database (Berkeley DB) is a programmatic toolkit that
provides embedded database support for both traditional and
client/server applications. Berkeley DB includes B+tree, Extended
Linear Hashing, Fixed and Variable-length record access methods,
transactions, locking, logging, shared memory caching and database
recovery. DB supports C, C++, Java and Perl APIs.

This package contains command line tools for managing Berkeley DB
databases.

%description utils -l pl
Berkeley Database (Berkeley DB) to zestaw narzêdzi programistycznych
zapewniaj±cych obs³ugê baz danych w aplikacjach tradycyjnych jak i
klient-serwer. Berkeley DB obs³uguje dostêp do bazy przez B-drzewa i
funkcje mieszaj±ce ze sta³± lub zmienn± wielko¶ci± rekordu,
transakcje, kroniki, pamiêæ dzielon± i odtwarzanie baz. Ma wsparcie
dla C, C++, Javy i Perla.

Ten pakiet zawiera narzêdzia do obs³ugi baz Berkeley DB z linii
poleceñ.

%prep
%setup -q -n db-%{version}

%build
cd dist
cp -f %{_datadir}/aclocal/libtool.m4 aclocal/libtool.ac
cp -f %{_datadir}/automake/config.sub .
cp -f %{_datadir}/libtool/ltmain.sh .
sh s_config
cd ..

cp -a build_unix build_unix.static

cd build_unix.static

CC="%{__cc}"
CXX="%{__cxx}"
CFLAGS="%{rpmcflags}"
CXXFLAGS="%{rpmcflags} -fno-implicit-templates"
LDFLAGS="%{rpmldflags}"
export CC CXX CFLAGS CXXFLAGS LDFLAGS

../dist/%configure \
	--enable-compat185 \
	--disable-shared \
	--enable-static \
	--enable-rpc \
	--%{?with_pmutex:en}%{!?with_pmutex:dis}able-posixmutexes \
	--enable-cxx

# (temporarily?) disabled because of compilation errors:
#	--enable-dump185 \

%{__make} library_build

cd ../build_unix

../dist/%configure \
	--prefix=%{_prefix} \
	--libdir=%{_libdir} \
	--enable-compat185 \
	--enable-rpc \
	--%{?with_pmutex:en}%{!?with_pmutex:dis}able-posixmutexes \
	--enable-cxx \
	%{?with_tcl:--enable-tcl} \
	%{?with_tcl:--with-tcl=/usr/lib} \
	%{?with_java:--enable-java} \
	--disable-static \
	--enable-shared 

%{__make} library_build \
	TCFLAGS='-I$(builddir) -I%{_includedir}' \
	LIBSO_LIBS="\$(LIBS)" \
	LIBTSO_LIBS="\$(LIBS) -ltcl"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_includedir},%{_libdir},%{_bindir}}
%if %{with java}
install -d $RPM_BUILD_ROOT%{_javadir}
%endif

%{__make} -C build_unix.static library_install \
	docdir=%{_docdir}/db-%{version}-docs \
	DESTDIR=$RPM_BUILD_ROOT

%{__make} -C build_unix library_install \
	docdir=%{_docdir}/db-%{version}-docs \
	DESTDIR=$RPM_BUILD_ROOT \
	LIB_INSTALL_FILE_LIST=""

cd $RPM_BUILD_ROOT%{_libdir}
ln -sf libdb-4.3.so libdb.so
ln -sf libdb-4.3.so libdb4.so
ln -sf libdb-4.3.so libdb-4.so
ln -sf libdb-4.3.so libndbm.so
ln -sf libdb-4.3.la libdb.la
ln -sf libdb-4.3.la libdb4.la
ln -sf libdb-4.3.la libndbm.la
%if %{with java}
ln -sf libdb_java-4.3.la libdb_java.la
mv -f *.jar $RPM_BUILD_ROOT%{_javadir}
%endif
%if %{with tcl}
ln -sf libdb_tcl-4.3.so libdb_tcl.so
ln -sf libdb_tcl-4.3.la libdb_tcl.la
%endif
ln -sf libdb_cxx-4.3.la libdb_cxx.la
mv -f libdb.a libdb-4.3.a
ln -sf libdb-4.3.a libdb.a
ln -sf libdb-4.3.a libdb4.a
ln -sf libdb-4.3.a libndbm.a
mv -f libdb_cxx.a libdb_cxx-4.3.a
ln -sf libdb_cxx-4.3.a libdb_cxx.a
ln -sf libdb_cxx-4.3.so libdb_cxx.so
ln -sf libdb_cxx-4.3.so libdb_cxx-4.so

sed -i "s/old_library=''/old_library='libdb-4.3.a'/" libdb-4.3.la
sed -i "s/old_library=''/old_library='libdb_cxx-4.3.a'/" libdb_cxx-4.3.la

cd -
rm -f examples_c*/tags
install -d $RPM_BUILD_ROOT%{_examplesdir}/db-%{version}
cp -rf examples_c/* $RPM_BUILD_ROOT%{_examplesdir}/db-%{version}

install -d $RPM_BUILD_ROOT%{_examplesdir}/db-cxx-%{version}
cp -rf examples_cxx/* $RPM_BUILD_ROOT%{_examplesdir}/db-cxx-%{version}

%if %{with java}
install -d $RPM_BUILD_ROOT%{_examplesdir}/db-java-%{version}
cp -rf examples_java/* $RPM_BUILD_ROOT%{_examplesdir}/db-java-%{version}
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	tcl -p /sbin/ldconfig
%postun	tcl -p /sbin/ldconfig

%post	cxx -p /sbin/ldconfig
%postun	cxx -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc LICENSE README
%attr(755,root,root) %{_libdir}/libdb-4.3.so
%dir %{_docdir}/db-%{version}-docs
%{_docdir}/db-%{version}-docs/sleepycat
%{_docdir}/db-%{version}-docs/index.html

%files devel
%defattr(644,root,root,755)
%{_libdir}/libdb-4.3.la
%{_libdir}/libdb-4.so
%{_libdir}/libdb.la
%{_libdir}/libdb.so
%{_libdir}/libdb4.la
%{_libdir}/libdb4.so
%{_libdir}/libndbm.la
%{_libdir}/libndbm.so
%{_includedir}/db.h
%{_includedir}/db_185.h
%{_docdir}/db-%{version}-docs/api_c
%{_docdir}/db-%{version}-docs/images
%{_docdir}/db-%{version}-docs/ref
%{_examplesdir}/db-%{version}

%files static
%defattr(644,root,root,755)
%{_libdir}/libdb-4.3.a
%{_libdir}/libdb4.a
%{_libdir}/libdb.a
%{_libdir}/libndbm.a

%files cxx
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb_cxx-4.3.so

%files cxx-devel
%defattr(644,root,root,755)
%{_includedir}/db_cxx.h
%{_libdir}/libdb_cxx-4.3.la
%{_libdir}/libdb_cxx-4.so
%{_libdir}/libdb_cxx.la
%{_libdir}/libdb_cxx.so
%{_docdir}/db-%{version}-docs/api_cxx
%{_examplesdir}/db-cxx-%{version}

%files cxx-static
%defattr(644,root,root,755)
%{_libdir}/libdb_cxx-4.3.a
%{_libdir}/libdb_cxx.a

%if %{with java}
%files java
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb_java*.so
%{_javadir}/db.jar

%files java-devel
%defattr(644,root,root,755)
%{_libdir}/libdb_java-4.3.la
%{_libdir}/libdb_java.la
%{_libdir}/libdb_java.so
%{_docdir}/db-%{version}-docs/java
%{_examplesdir}/db-java-%{version}
%endif

%if %{with tcl}
%files tcl
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libdb_tcl-4.3.so

%files tcl-devel
%defattr(644,root,root,755)
%{_libdir}/libdb_tcl-4.3.la
%{_libdir}/libdb_tcl.la
%{_libdir}/libdb_tcl.so
%{_docdir}/db-%{version}-docs/api_tcl
%endif

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/berkeley_db_svc
%attr(755,root,root) %{_bindir}/db*_archive
%attr(755,root,root) %{_bindir}/db*_checkpoint
%attr(755,root,root) %{_bindir}/db*_deadlock
%attr(755,root,root) %{_bindir}/db*_dump
#%attr(755,root,root) %{_bindir}/db*_dump185
%attr(755,root,root) %{_bindir}/db*_load
%attr(755,root,root) %{_bindir}/db*_printlog
%attr(755,root,root) %{_bindir}/db*_recover
%attr(755,root,root) %{_bindir}/db*_stat
%attr(755,root,root) %{_bindir}/db*_upgrade
%attr(755,root,root) %{_bindir}/db*_verify
%{_docdir}/db-%{version}-docs/utility
