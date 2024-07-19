# Code analysis
## IoT 
#### Version not provided 

**By: Administrator**

*Date: 2024-07-19*

## Introduction
This document contains results of the code analysis of IoT



## Configuration

- Quality Profiles
    - Names: Sonar way [Python]; 
    - Files: AZDJexoopNZcRql2xSg6.json; 


 - Quality Gate
    - Name: Sonar way
    - File: Sonar way.xml

## Synthesis

### Analysis Status

Reliability | Security | Security Review | Maintainability |
:---:|:---:|:---:|:---:
A | A | E | A |

### Quality gate status

| Quality Gate Status | OK |
|-|-|



### Metrics

Coverage | Duplications | Comment density | Median number of lines of code per file | Adherence to coding standard |
:---:|:---:|:---:|:---:|:---:
0.0 % | 0.0 % | 20.8 % | 9.0 | 99.8 %

### Tests

Total | Success Rate | Skipped | Errors | Failures |
:---:|:---:|:---:|:---:|:---:
0 | 0 % | 0 | 0 | 0

### Detailed technical debt

Reliability|Security|Maintainability|Total
---|---|---|---
-|-|0d 0h 15min|0d 0h 15min


### Metrics Range

\ | Cyclomatic Complexity | Cognitive Complexity | Lines of code per file | Coverage | Comment density (%) | Duplication (%)
:---|:---:|:---:|:---:|:---:|:---:|:---:
Min | 0.0 | 0.0 | 0.0 | 0.0 | 0.0 | 0.0
Max | 19.0 | 12.0 | 229.0 | 0.0 | 66.7 | 0.0

### Volume

Language|Number
---|---
Python|377
Total|377


## Issues

### Issues count by severity and types

Type / Severity|INFO|MINOR|MAJOR|CRITICAL|BLOCKER
---|---|---|---|---|---
BUG|0|0|0|0|0
VULNERABILITY|0|0|0|0|0
CODE_SMELL|0|0|3|0|0


### Issues List

Name|Description|Type|Severity|Number
---|---|---|---|---
Collapsible "if" statements should be merged|Merging collapsible if statements increases the code’s readability. <br /> Noncompliant Code Example <br />  <br /> if condition1: <br />     if condition2: <br />         # ... <br />  <br /> Compliant Solution <br />  <br /> if condition1 and condition2: <br />     # ... <br /> |CODE_SMELL|MAJOR|1
Sections of code should not be commented out|Programmers should not comment out code as it bloats programs and reduces readability. <br /> Unused code should be deleted and can be retrieved from source control history if required.|CODE_SMELL|MAJOR|2


## Security Hotspots

### Security hotspots count by category and priority

Category / Priority|LOW|MEDIUM|HIGH
---|---|---|---
LDAP Injection|0|0|0
Object Injection|0|0|0
Server-Side Request Forgery (SSRF)|0|0|0
XML External Entity (XXE)|0|0|0
Insecure Configuration|1|0|0
XPath Injection|0|0|0
Authentication|0|0|1
Weak Cryptography|0|0|0
Denial of Service (DoS)|0|0|0
Log Injection|0|0|0
Cross-Site Request Forgery (CSRF)|0|0|2
Open Redirect|0|0|0
Permission|0|0|0
SQL Injection|0|0|0
Encryption of Sensitive Data|0|0|0
Traceability|0|0|0
Buffer Overflow|0|0|0
File Manipulation|0|0|0
Code Injection (RCE)|0|0|0
Cross-Site Scripting (XSS)|0|0|0
Command Injection|0|0|0
Path Traversal Injection|0|0|0
HTTP Response Splitting|0|0|0
Others|0|0|0


### Security hotspots

Category|Name|Priority|Severity|Count
---|---|---|---|---
Cross-Site Request Forgery (CSRF)|Allowing both safe and unsafe HTTP methods is security-sensitive|HIGH|MINOR|2
Authentication|Hard-coded credentials are security-sensitive|HIGH|BLOCKER|1
Insecure Configuration|Delivering code in production with debug features activated is security-sensitive|LOW|MINOR|1
