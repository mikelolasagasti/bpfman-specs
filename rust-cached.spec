# Generated by rust2rpm 25
%bcond_without check
%global debug_package %{nil}

%global crate cached

Name:           rust-cached
Version:        0.48.1
Release:        %autorelease
Summary:        Generic cache implementations and simplified function memoization

License:        MIT
URL:            https://crates.io/crates/cached
Source:         %{crates_source}
# Manually created patch for downstream crate metadata changes
Patch:          cached-fix-metadata.diff

BuildRequires:  cargo-rpm-macros >= 24

%global _description %{expand:
Generic cache implementations and simplified function memoization.}

%description %{_description}

%package        devel
Summary:        %{summary}
BuildArch:      noarch

%description    devel %{_description}

This package contains library source intended for building other packages which
use the "%{crate}" crate.

%files          devel
%license %{crate_instdir}/COPYRIGHT
%license %{crate_instdir}/LICENSE
%doc %{crate_instdir}/CHANGELOG.md
%doc %{crate_instdir}/CONTRIBUTING.md
%doc %{crate_instdir}/README.md
%{crate_instdir}/

%package     -n %{name}+default-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+default-devel %{_description}

This package contains library source intended for building other packages which
use the "default" feature of the "%{crate}" crate.

%files       -n %{name}+default-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+ahash-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+ahash-devel %{_description}

This package contains library source intended for building other packages which
use the "ahash" feature of the "%{crate}" crate.

%files       -n %{name}+ahash-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-devel %{_description}

This package contains library source intended for building other packages which
use the "async" feature of the "%{crate}" crate.

%files       -n %{name}+async-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async-trait-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async-trait-devel %{_description}

This package contains library source intended for building other packages which
use the "async-trait" feature of the "%{crate}" crate.

%files       -n %{name}+async-trait-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+async_tokio_rt_multi_thread-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+async_tokio_rt_multi_thread-devel %{_description}

This package contains library source intended for building other packages which
use the "async_tokio_rt_multi_thread" feature of the "%{crate}" crate.

%files       -n %{name}+async_tokio_rt_multi_thread-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+cached_proc_macro-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cached_proc_macro-devel %{_description}

This package contains library source intended for building other packages which
use the "cached_proc_macro" feature of the "%{crate}" crate.

%files       -n %{name}+cached_proc_macro-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+cached_proc_macro_types-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+cached_proc_macro_types-devel %{_description}

This package contains library source intended for building other packages which
use the "cached_proc_macro_types" feature of the "%{crate}" crate.

%files       -n %{name}+cached_proc_macro_types-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+futures-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+futures-devel %{_description}

This package contains library source intended for building other packages which
use the "futures" feature of the "%{crate}" crate.

%files       -n %{name}+futures-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+proc_macro-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+proc_macro-devel %{_description}

This package contains library source intended for building other packages which
use the "proc_macro" feature of the "%{crate}" crate.

%files       -n %{name}+proc_macro-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+r2d2-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+r2d2-devel %{_description}

This package contains library source intended for building other packages which
use the "r2d2" feature of the "%{crate}" crate.

%files       -n %{name}+r2d2-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde-devel %{_description}

This package contains library source intended for building other packages which
use the "serde" feature of the "%{crate}" crate.

%files       -n %{name}+serde-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+serde_json-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+serde_json-devel %{_description}

This package contains library source intended for building other packages which
use the "serde_json" feature of the "%{crate}" crate.

%files       -n %{name}+serde_json-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+tokio-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+tokio-devel %{_description}

This package contains library source intended for building other packages which
use the "tokio" feature of the "%{crate}" crate.

%files       -n %{name}+tokio-devel
%ghost %{crate_instdir}/Cargo.toml

%package     -n %{name}+wasm-devel
Summary:        %{summary}
BuildArch:      noarch

%description -n %{name}+wasm-devel %{_description}

This package contains library source intended for building other packages which
use the "wasm" feature of the "%{crate}" crate.

%files       -n %{name}+wasm-devel
%ghost %{crate_instdir}/Cargo.toml

%prep
%autosetup -n %{crate}-%{version} -p1
%cargo_prep

%generate_buildrequires
%cargo_generate_buildrequires

%build
%cargo_build

%install
%cargo_install

%if %{with check}
%check
%cargo_test
%endif

%changelog
%autochangelog
