# tldextract Changelog

After upgrading, update your cache file by deleting it or via `tldextract
--update`.

## 1.7.3 (2015-12-12)

* Bugfixes
    * Support IDNA2008 - [#82](https://github.com/john-kurkowski/tldextract/pull/82)
* Misc.
    * Ease running scripts during local development

## 1.7.2 (2015-11-28)

* Bugfixes
    * Domain parsing fails with trailing spaces - [#75](https://github.com/john-kurkowski/tldextract/pull/75)
    * Update to latest, direct PSL links - [#77](https://github.com/john-kurkowski/tldextract/pull/77)
* Misc.
    * Update bundled PSL snapshot
    * Require requirements.txt for local development
    * Enforce linting via the test suite - [#79](https://github.com/john-kurkowski/tldextract/pull/79)
    * Switch to py.test runner - [#80](https://github.com/john-kurkowski/tldextract/pull/80)
    * No longer distribute tests. No mention of `test_suite` in setup.py. CI is
      handled centrally now, on this project's GitHub.

## 1.7.1 (2015-08-22)

Fix publishing mistake with 1.7.0.

## 1.7.0 (2015-08-22)

* Features
    * Can include PSL's private domains on CLI with `--private_domains` boolean flag
* Bugfixes
    * Improved support for multiple Punycode (or Punycode-looking) parts of a URL
        * Mixed in/valid
        * Mixed encodings
    * Fix `ExtractResult._asdict` on Python 3.4. This should also save space,
      as `__dict__` is not created for each `ExtractResult` instance.

## 1.6 (2015-03-22)

* Features
    * Pass `extra_suffixes` directly to constructor
* Bugfixes
    * Punycode URLs were returned decoded, rather than left alone
    * Things that look like Punycode to tldextract, but aren't, shouldn't raise
    * Print unified diff to debug log, rather than inconsistent stderr

## 1.5.1 (2014-10-13)

* Bugfixes
    * Missing setuptools dependency
    * Avoid u'' literal for Python 3.0 - 3.2 compatibility. Tests will still fail though.

## 1.5 (2014-09-08)

* Bugfixes
    * Exclude PSL's private domains by default - [#19](https://github.com/john-kurkowski/tldextract/pull/19)
        * This is a **BREAKING** bugfix if you relied on the PSL's private
          domains
        * Revert to old behavior by setting `include_psl_private_domains=True`
    * `UnicodeError` for inputs that looked like an IP

## 1.4 (2014-06-01)

* Features
    * Support punycode inputs
* Bugfixes
    * Fix minor Python 3 unicode errors

## 1.3.1 (2013-12-16)

* Bugfixes
    * Match PSL's GitHub mirror rename, from mozilla-central to gecko-dev
    * Try Mozilla's PSL SPOT first, then the mirror

## 1.3 (2013-12-08)

* Features
    * Specify your own PSL url/file with `suffix_list_url` kwarg
    * `fallback_to_snapshot` kwarg - defaults to True
* Deprecations
    * `fetch` kwarg

## 1.2 (2013-07-07)

* Features
    * Better CLI
    * Cache env var support
    * Python 3.3 support
    * New aliases `suffix` and `registered_domain`
* Bugfixes
    * Fix dns root label

## 1.1 (2012-03-22)

* Bugfixes
    * Reliable logger name
    * Forgotten `import sys`
