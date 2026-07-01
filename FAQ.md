# FAQ - Frequently Asked Questions

## What is the goal of .cjson?
The goal is to provide a "Clear" and human-centric way to write configuration files. We want to eliminate the visual clutter caused by mandatory double quotes and brackets while keeping the data structure identical to standard JSON.

## Why are there no comments (like # or //) in .cjson?
We believe that configuration files should be pure data. Adding comments turns a data format into a pseudo-scripting language, which increases complexity for parsers and leads to inconsistent file structures. Clear JSON is strictly for data representation.

## How does the compiler handle Boolean and Number types?
Our compiler uses "Tag-free detection." If a value is literally `true`, `false`, `null`, or a standard numeric sequence (integers or decimals) without surrounding characters, it is automatically parsed into its corresponding Boolean, Null, or Number type. All other non-bracketed data is treated as a string.

## Can I use .cjson for public APIs?
No. .cjson is designed for local configuration, project settings, and internal system parameters. For data exchange between different systems or public APIs, we strongly recommend converting it to standard JSON to ensure maximum compatibility.

## How do I handle multi-word strings?
To maintain readability and avoid parsing conflicts, we use hyphens (`-`) as separators for multi-word strings (e.g., `deployment_type: high-availability`).

## Is .cjson a replacement for JSON?
Not at all. It is a refinement of the configuration experience. Think of it as a "pre-processor" for your application settings that is easier for you to edit by hand, while remaining 100% compatible with the JSON ecosystem once compiled.

