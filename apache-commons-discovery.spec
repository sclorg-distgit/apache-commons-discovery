%global pkg_name apache-commons-discovery
%{?scl:%scl_package %{pkg_name}}
%{?java_common_find_provides_and_requires}

Name:           %{?scl_prefix}%{pkg_name}
Version:        0.5
Release:        10.1%{?dist}
Epoch:          2
Summary:        Apache Commons Discovery
License:        ASL 2.0
URL:            http://commons.apache.org/discovery
Source0:        http://www.apache.org/dist/commons/discovery/source/commons-discovery-%{version}-src.tar.gz
Patch0:         %{pkg_name}-addosgimanifest.patch
Patch1:         %{pkg_name}-remove-unreliable-test.patch
BuildArch:      noarch

BuildRequires:  %{?scl_prefix}maven-local
BuildRequires:  %{?scl_prefix}mvn(commons-logging:commons-logging)
BuildRequires:  %{?scl_prefix}mvn(junit:junit)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.commons:commons-parent:pom:)
BuildRequires:  %{?scl_prefix_maven}mvn(org.apache.maven.plugins:maven-assembly-plugin)

%description
The Discovery component is about discovering, or finding, implementations for
pluggable interfaces.  Pluggable interfaces are specified with the intent that
multiple implementations are, or will be, available to provide the service
described by the interface.  Discovery provides facilities for finding and
instantiating classes, and for lifecycle management of singleton (factory)
classes.

%package javadoc
Summary:        API documentation for %{name}

%description javadoc
%{summary}.

%prep
%setup -q -n commons-discovery-%{version}-src

%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%patch0
%patch1 -p1
%mvn_file : commons-discovery %{pkg_name}
%{?scl:EOF}

%build
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_build
%{?scl:EOF}

%install
%{?scl:scl enable %{scl_maven} %{scl} - << "EOF"}
%mvn_install
%{?scl:EOF}

%files -f .mfiles
%doc LICENSE.txt NOTICE.txt RELEASE-NOTES.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE.txt NOTICE.txt


%changelog
* Tue Jul 26 2016 Michael Simacek <msimacek@redhat.com> - 2:0.5-10.1
- Prepare for rh-java-common inclusion

* Thu Apr 4 2013 Krzysztof Daniel <kdaniel@redhat.com> 2:0.5-10
- Remove scl prefix from the jar.
- Drop javadoc subpackage.

* Tue Feb 19 2013 Krzysztof Daniel <kdaniel@redhat.com> 2:0.5-9
- Remove unnecessary obsoletes.

* Thu Feb 14 2013 Krzysztof Daniel <kdaniel@redhat.com> 2:0.5-8
- Initial contribution to SCL.

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:0.5-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Wed Feb 06 2013 Java SIG <java-devel@lists.fedoraproject.org> - 2:0.5-6
- Update for https://fedoraproject.org/wiki/Fedora_19_Maven_Rebuild
- Replace maven BuildRequires with maven-local

* Tue Jan 15 2013 Michal Srb <msrb@redhat.com> - 2:0.5-5
- Build with xmvn

* Wed Jul 18 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:0.5-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Thu May 17 2012 gil cattaneo <puntogil@libero.it> - 2:0.5-3
- add maven pom

* Thu Jan 12 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:0.5-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Mon Nov 7 2011 Alexander Kurtakov <akurtako@redhat.com> 2:0.5-1
- Update to 0.5 upstream release.
- Build with maven.

* Mon Feb 07 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 2:0.4-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Thu Jul  8 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2:0.4-5
- Add license to javadoc subpackage
- Fix jar symlink installation

* Wed May 12 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2:0.4-4
- Add obsoletes to javadoc subpackage
- Add proper symlinks for unversioned jar files

* Fri May  7 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2:0.4-3
- Add jpackage-utils as dep for -javadoc subpackage

* Fri May  7 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 2:0.4-2
- Fix provides

* Thu May  6 2010 Stanislav Ochotnicky <sochotnicky@redhat.com> - 0.4-1
- Rename and cleanup of jakarta-commons-discovery
