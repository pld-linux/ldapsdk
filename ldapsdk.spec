Summary:	Enables applications to manage information stored in an LDAP directory
Summary(pl.UTF-8):   Umożliwienie aplikacjom zarządzania informacjami w katalogu LDAP
Name:		ldapsdk
Version:	4.17
Release:	0.1
License:	NPL
Group:		Development/Libraries
Source0:	http://www.mozilla.org/directory/ldapsdk_java_20020819.tar.gz
# Source0-md5:	f0eef8fc5c4961cdebdd9b9188228431
URL:		http://www.mozilla.org/directory/
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	sed >= 4.0
Requires:	jre
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Mozilla LDAP SDKs enable you to write applications which access,
manage, and update the information stored in an LDAP directory.

%description -l pl.UTF-8
Mozilla LDAP SDK pozwala pisać aplikacje odwołujące się, zarządzające
i uaktualniające informacje przechowywane w katalogu LDAP.

%package javadoc
Summary:	Javadoc for LDAP SDK
Summary(pl.UTF-8):   Dokumentacja javadoc dla LDAP SDK
Group:		Documentation

%description javadoc
Javadoc for LDAP SDK.

%description javadoc -l pl.UTF-8
Dokumentacja javadoc dla LDAP SDK.

%prep
%setup -q -c
# remove CVS control files
find -name CVS -print0 | xargs -0 rm -rf

sed -i -e 's/ -classpath / -source 1.4 -classpath /' mozilla/directory/java-sdk/ldap.mk

%build
cd mozilla/directory/java-sdk
%{__make} -f ldap.mk \
	%{!?debug:DEBUG=0} \
	MOZ_SRC=. \
	JAVA_HOME="%{java_home}" \
	JAVA_VERSION=1.4

%{__make} -f ldap.mk basepackage
%{__make} -f ldap.mk doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
install mozilla/directory/java-sdk/dist/packages/ldapjdk.jar $RPM_BUILD_ROOT%{_javadir}

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -r mozilla/directory/java-sdk/dist/doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc mozilla/directory/java-sdk/{ldapsp-relnotes.htm,relnotes.htm}
%{_javadir}/ldapjdk.jar

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
