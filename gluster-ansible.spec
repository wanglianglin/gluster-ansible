%global rolesdir %{_sysconfdir}/ansible/roles/gluster.ansible
%global docdir %{_datadir}/doc/gluster.ansible
%global buildnum 2

Name:      gluster-ansible-roles
Version:   1.0.0
Release:   2%{?dist}
Summary:   Ansible roles for GlusterFS deployment and management

URL:       https://github.com/gluster/gluster-ansible
Source0:   %{url}/archive/v%{version}.tar.gz#/%{name}-%{version}-%{buildnum}.tar.gz
License:   GPLv3
BuildArch: noarch

Requires:  ansible >= 2.6
Requires:  gluster-ansible-infra >= 0.3
Requires:  gluster-ansible-features >= 0.3
Requires:  gluster-ansible-cluster >= 0.1
Requires:  gluster-ansible-repositories >= 0.2
Requires:  gluster-ansible-maintenance >= 0.1

%description
Collection of Ansible roles for the deploying and managing GlusterFS clusters.

%prep
%autosetup -p1

%build

%install
mkdir -p %{buildroot}/%{rolesdir}
cp -a playbooks/ %{buildroot}/%{rolesdir}

mkdir -p %{buildroot}/%{docdir}
install -p -m 644 README.md LICENSE %{buildroot}/%{docdir}


%files
%{rolesdir}
%doc %{docdir}

%license LICENSE

%changelog
* Fri Feb 22 2019 Sachidananda Urs <sac@redhat.com> 1.0.0-2
- Update example playbooks to clean up failed deployments

* Thu Feb 21 2019 Sachidananda Urs <sac@redhat.com> 1.0.0-1
- Bump the version number, stable enought to call 1.0.0

* Tue Oct 23 2018 Sachidananda Urs <sac@redhat.com> 0.5
- Address the security concerns regarding plaintext passwords

* Fri Oct 12 2018 Sachidnanda Urs <sac@redhat.com> 0.4
- Enhancements to examples

* Mon Sep 24 2018 Sachidananda Urs <sac@redhat.com> 0.3
- Added playbooks to illustrate end-to-end deployment

* Fri Aug 31 2018 Sachidananda Urs <sac@redhat.com> 0.2
- Added gluster-maintenance. Bug fixes across the roles

* Tue Apr 24 2018 Sachidananda Urs <sac@redhat.com> 0.1
- Initial release.

