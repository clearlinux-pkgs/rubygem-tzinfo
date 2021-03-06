#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-tzinfo
Version  : 1.2.2
Release  : 11
URL      : https://rubygems.org/downloads/tzinfo-1.2.2.gem
Source0  : https://rubygems.org/downloads/tzinfo-1.2.2.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-minitest
BuildRequires : rubygem-rake
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-thread_safe

%description
TZInfo - Ruby Timezone Library
==============================
[![Gem Version](https://badge.fury.io/rb/tzinfo.svg)](http://badge.fury.io/rb/tzinfo) [![Build Status](https://travis-ci.org/tzinfo/tzinfo.svg?branch=master)](https://travis-ci.org/tzinfo/tzinfo)

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n tzinfo-1.2.2
gem spec %{SOURCE0} -l --ruby > rubygem-tzinfo.gemspec

%build
gem build rubygem-tzinfo.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
tzinfo-1.2.2.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
pushd %{buildroot}%{gem_dir}/gems/tzinfo-1.2.2 &&  rake --trace test TESTOPTS="-v" && popd


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/tzinfo-1.2.2.gem
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/.yardopts
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/CHANGES.md
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/README.md
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/country.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/country_index_definition.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/country_info.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/country_timezone.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/data_source.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/data_timezone.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/data_timezone_info.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/info_timezone.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/linked_timezone.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/linked_timezone_info.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/offset_rationals.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/ruby_core_support.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/ruby_country_info.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/ruby_data_source.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/time_or_datetime.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/timezone.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/timezone_definition.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/timezone_index_definition.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/timezone_info.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/timezone_offset.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/timezone_period.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/timezone_proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/timezone_transition.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/timezone_transition_definition.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/transition_data_timezone_info.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/zoneinfo_country_info.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/zoneinfo_data_source.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/lib/tzinfo/zoneinfo_timezone_info.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_country.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_country_index_definition.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_country_info.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_country_timezone.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_data_source.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_data_timezone.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_data_timezone_info.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_info_timezone.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_linked_timezone.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_linked_timezone_info.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_offset_rationals.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_ruby_core_support.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_ruby_country_info.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_ruby_data_source.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_time_or_datetime.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_timezone.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_timezone_definition.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_timezone_index_definition.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_timezone_info.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_timezone_london.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_timezone_melbourne.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_timezone_new_york.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_timezone_offset.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_timezone_period.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_timezone_proxy.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_timezone_transition.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_timezone_transition_definition.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_timezone_utc.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_transition_data_timezone_info.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_zoneinfo_country_info.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_zoneinfo_data_source.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tc_zoneinfo_timezone_info.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/test_utils.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/ts_all.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/ts_all_ruby.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/ts_all_zoneinfo.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tzinfo-data/tzinfo/data.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tzinfo-data/tzinfo/data/definitions/America/Argentina/Buenos_Aires.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tzinfo-data/tzinfo/data/definitions/America/New_York.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tzinfo-data/tzinfo/data/definitions/Australia/Melbourne.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tzinfo-data/tzinfo/data/definitions/EST.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tzinfo-data/tzinfo/data/definitions/Etc/GMT__m__1.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tzinfo-data/tzinfo/data/definitions/Etc/GMT__p__1.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tzinfo-data/tzinfo/data/definitions/Etc/UTC.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tzinfo-data/tzinfo/data/definitions/Europe/Amsterdam.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tzinfo-data/tzinfo/data/definitions/Europe/Andorra.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tzinfo-data/tzinfo/data/definitions/Europe/London.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tzinfo-data/tzinfo/data/definitions/Europe/Paris.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tzinfo-data/tzinfo/data/definitions/Europe/Prague.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tzinfo-data/tzinfo/data/definitions/UTC.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tzinfo-data/tzinfo/data/indexes/countries.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tzinfo-data/tzinfo/data/indexes/timezones.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/tzinfo-data/tzinfo/data/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/zoneinfo/America/Argentina/Buenos_Aires
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/zoneinfo/America/New_York
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/zoneinfo/Australia/Melbourne
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/zoneinfo/EST
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/zoneinfo/Etc/UTC
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/zoneinfo/Europe/Amsterdam
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/zoneinfo/Europe/Andorra
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/zoneinfo/Europe/London
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/zoneinfo/Europe/Paris
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/zoneinfo/Europe/Prague
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/zoneinfo/Factory
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/zoneinfo/UTC
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/zoneinfo/iso3166.tab
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/zoneinfo/localtime
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/zoneinfo/posix/Europe/London
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/zoneinfo/posixrules
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/zoneinfo/right/Europe/London
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/zoneinfo/zone.tab
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/test/zoneinfo/zone1970.tab
/usr/lib64/ruby/gems/2.3.0/gems/tzinfo-1.2.2/tzinfo.gemspec
/usr/lib64/ruby/gems/2.3.0/specifications/tzinfo-1.2.2.gemspec
