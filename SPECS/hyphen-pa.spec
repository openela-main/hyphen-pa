Name: hyphen-pa
Summary: Punjabi hyphenation rules
Epoch: 1
Version: 0.7.0
Release: 19%{?dist}
Source: http://download.savannah.gnu.org/releases/smc/hyphenation/patterns/%{name}-%{version}.tar.bz2
URL: http://wiki.smc.org.in
License: LGPLv3+
BuildArch: noarch
Requires: hyphen
Supplements: (hyphen and langpacks-pa)

%description
Punjabi hyphenation rules.

%prep
%setup -q

%build

%install
mkdir -p %{buildroot}/%{_datadir}/hyphen
install -m644 -p *.dic %{buildroot}/%{_datadir}/hyphen

pushd %{buildroot}/%{_datadir}/hyphen/
pa_IN_aliases="pa_PK"
for lang in $pa_IN_aliases; do
        ln -s hyph_pa_IN.dic hyph_$lang.dic
done
popd

%files
%doc README COPYING ChangeLog
%{_datadir}/hyphen/*

%changelog
* Mon Aug 09 2021 Mohan Boddu <mboddu@redhat.com> - 1:0.7.0-19
- Rebuilt for IMA sigs, glibc 2.34, aarch64 flags
  Related: rhbz#1991688

* Fri Apr 16 2021 Mohan Boddu <mboddu@redhat.com> - 1:0.7.0-18
- Rebuilt for RHEL 9 BETA on Apr 15th 2021. Related: rhbz#1947937

* Tue Jan 26 2021 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7.0-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Tue Jul 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7.0-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jan 29 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7.0-15
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7.0-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Fri Feb 01 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7.0-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7.0-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7.0-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7.0-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7.0-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 19 2016 Parag Nemade <pnemade AT redhat DOT com> - 1:0.7.0-8
- Add Supplements: tag for langpacks naming guidelines
- Clean the specfile to follow current packaging guidelines

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1:0.7.0-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7.0-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7.0-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1:0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Nov 29 2012 Parag <pnemade AT redhat DOT com> - 1:0.7.0-2
- Correct the changelog entry

* Tue Nov 27 2012 Parag <pnemade AT redhat DOT com> - 1:0.7.0-1
- Resolves:rh#880294- package does not follow naming guidelines

* Wed Nov 21 2012 Parag <pnemade AT redhat DOT com> - 0.20111229-2
- Add %%doc files

* Thu Aug 02 2012 Parag <pnemade AT redhat DOT com> - 0.20111229-1
- Update to new upstream 0.7.0

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100204-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100204-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20100204-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Mon Feb 08 2010 Parag <pnemade AT redhat.com> - 0.20100204-1
- update to 20100204

* Thu Sep 24 2009 Parag <pnemade@redhat.com> - 0.20090924-1
- update to 20090924

* Mon Aug 17 2009 Parag <pnemade@redhat.com> - 0.20090813-1
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20081213-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Mon Apr 06 2009 Caolan McNamara <caolanm@redhat.com> - 0.20081213-1
- initial version
