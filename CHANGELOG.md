# Changelog

## Version 0.1.2 Release

Fix pipeline not sending pypi properties

## Version 0.1.1 Release

New pipeline setup; updated dependencies

## Version 0.0.22 Release

Fixes bugs MeasurementProxy "module as a context manager" (or batching) use cases introduced in v0.0.21.

##  Version 0.0.21 Release

edit: DO NOT USE - use v0.0.22 instead.

Adds context manager capabilities to MeasurementWrapper to allow for more
efficient connection handling in high volume measuring situations. Ported from
https://github.com/unite-io/data-collection-tw/commit/1c60768ba5320917b79792def64ad18fc7f44eeb.

## Version 0.0.20 Release

Add `bugsnag_handler` flag to logging module which allows not logging "log errors" to Bugsnag.

## Version 0.0.19 Release

Port over instrumentation code, which extracts measurement tags from method arguments

## Version 0.0.18 Release

Add new logging module which configures logging in a standardized way

## Version 0.0.15 Release

Change default Consul scheme to be HTTP instead of HTTPS

## Version 0.0.14 Release

Fixes dynamicconfig bug where no data was loaded at start time.

## Version 0.0.13 Release

Fixes using `_provider` and `_runner` when not inited

## Version 0.0.12 Release

Contains dynamic config submodule.

## Version 0.0.11 Release

Fixing breaking change that removed `@property` from `Timer.elapsed`
