Summary:	Enables applications to manage information stored in an LDAP directory
Name:		ldapsdk
Version:	4.17
Release:	0.1
License:	NPL
Group:		Development/Libraries
URL:		http://www.mozilla.org/directory/
Source0:	ftp://ftp.mozilla.org/pub/directory/java-sdk/%{name}_java_20020819.tar.gz
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The Mozilla LDAP SDKs enable you to write applications which access,
manage, and update the information stored in an LDAP directory.

%package javadoc
Summary:	Javadoc for %{name}
Group:		Documentation

%description javadoc
Javadoc for %{name}.

%prep
%setup -q -n mozilla
for dir in `find . -type d -name CVS`; do rm -rf $dir; done

%build
cd directory/java-sdk
%{__make} -f ldap.mk \
	MOZ_SRC=. \
	JAVA_VERSION=1.4

%{__make} -f ldap.mk basepackage
%{__make} -f ldap.mk doc

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_javadir}
install directory/java-sdk/dist/packages/ldapjdk.jar $RPM_BUILD_ROOT%{_javadir}

install -d $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}
cp -r directory/java-sdk/dist/doc/* $RPM_BUILD_ROOT%{_javadocdir}/%{name}-%{version}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc directory/java-sdk/{ldapsp-relnotes.htm,relnotes.htm}
%{_javadir}/*

%files javadoc
%defattr(644,root,root,755)
%{_javadocdir}/%{name}-%{version}
