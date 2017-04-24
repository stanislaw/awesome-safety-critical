# awesome-safety-critical

[![Build Status](https://travis-ci.org/stanislaw/awesome-safety-critical.svg?branch=master)](https://travis-ci.org/stanislaw/awesome-safety-critical)

This is a list of resources about programming practices for writing
safety-critical software.

The starting point for me to create this resource was my interest in a solid
software:

[What kind of special training do engineers working on mission-critical software receive? [closed]](What_kind_of_special_training_do_engineer_working_on_mission-critical_software_receive%3F_-_Stack_Overflow.pdf) and [its followup on Reddit](https://www.reddit.com/r/programming/comments/5iohue/what_kind_of_special_training_do_engineers/).

**Disclaimer:** I don't work on safety-critical software so the resources
presented here are not necessarily authoritative or latest documents on topic.

## Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Resources](#resources)
- [Software safety standards](#software-safety-standards)
- [Safety guidebooks](#safety-guidebooks)
- [Coding guidelines](#coding-guidelines)
- [Articles](#articles)
- [Papers](#papers)
- [Incidents](#incidents)
- [Questions and Answers](#questions-and-answers)
- [Books](#books)
- [Interviews](#interviews)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Resources

- [European Cooperation for Space Standardization](http://ecss.nl/)

> The European Cooperation for Space Standardization is an initiative established to develop a coherent, single set of user-friendly standards for use in all European space activities.

**This list has a number of links from this resource.**

- [The International System Safety Society](http://www.system-safety.org/)

> The International System Safety Society is a non-profit organization dedicated to supporting the Safety Professional in the application of Systems Engineering and Systems Management to the process of hazard, safety and risk analysis.  The Society is international in scope and draws members throughout the world.  It is affiliated with major corporations, educational institutions and other agencies in the United States and abroad.

**This list has a number of links from this resource.**

## Software safety standards

- [IEC 61508](https://en.wikipedia.org/wiki/IEC_61508)

> IEC 61508 is an international standard published by the International Electrotechnical Commission of rules applied in industry. It is titled Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems (E/E/PE, or E/E/PES).

- [DO-178C](https://en.wikipedia.org/wiki/DO-178C)

> DO-178C, Software Considerations in Airborne Systems and
Equipment Certification is the primary document by which the certification
authorities such as FAA, EASA and Transport Canada approve all commercial
software-based aerospace systems. The document is published by
RTCA, Incorporated, in a joint effort with EUROCAE, and replaces DO-178B.
The new document is called DO-178C/ED-12C and was completed in November 2011 and
approved by the RTCA in December 2011. It became available for sale and use
in January 2012.

> The FAA approved AC 20-115C on 19 Jul 2013, making DO-178C a recognized
"acceptable means, but not the only means, for showing compliance with the
applicable airworthiness regulations for the software aspects of
airborne systems and equipment certification." (Wikipedia)

- [ARINC standards](https://en.wikipedia.org/wiki/ARINC#Standards)

> The ARINC Standards are prepared by the Airlines Electronic Engineering Committee (AEEC) where Rockwell Collins and other aviation suppliers serve as a contributor in support of their airline customer base. (Wikipedia)

- [ISO 26262](https://en.wikipedia.org/wiki/ISO_26262)

> The ISO 26262 Standard is prepared by the ISO Committee and is a derivative of the IEC 61508 standard listed above.  The committee members include the major vehicle manufacturers and suppliers.  It is expressly a safety standard, but includes details about Hazard Analysis and Risk Assessment and system design to detect faults and their potential failures.

- [MIL-STD-882E, System Safety](http://www.system-safety.org/Documents/MIL-STD-882E.pdf)

- [MIL-STD-1472F, Human Engineering](http://www.system-safety.org/Operations%20Manual/1472f.doc)

- [NASA-STD-8719.13B, NASA Software Safety Standard](http://www.system-safety.org/Documents/NASA-STD-8719.13B.pdf)

- [ECSS-E-ST-40C, Software](http://ecss.nl/standard/ecss-e-st-40c-software-general-requirements/)

- [ECSS-Q-ST-80C Rev.1 – Software product assurance](http://ecss.nl/standard/ecss-q-st-80c-rev-1-software-product-assurance-15-february-2017/)

## Safety guidebooks

- [ECSS-E-HB-40A – Software engineering handbook](http://ecss.nl/hbstms/ecss-e-hb-40a-software-engineering-handbook-11-december-2013/)

- [NASA Software Safety Guidebook](http://www.system-safety.org/Documents/NASA-GB-8719.13.pdf)

> NASA's Software Safety Guidebook (pdf file). The handbook complement to the
Software Safety Standard.

- [Software System Safety Handbook](http://www.system-safety.org/Documents/Software_System_Safety_Handbook.pdf)

> From the Joint Services Computer Resources Management Group, US Navy, US Army,
And US Air Force (pdf file)

- [Joint Software Systems Safety Engineering Handbook](http://www.system-safety.org/Documents/SOFTWARE_SYSTEM_SAFETY_HDBK_2010.pdf)

- [Air Force System Safety Handbook](http://www.system-safety.org/Documents/AF_System-Safety-HNDBK.pdf)

> First chapter has an excellent introduction to system safety with a discussion
of the evolution of the DoD Standard 882 (DOD Standard Practice for
System Safety).

## Coding guidelines

- [MISRA guidelines](https://www.misra.org.uk/Publications/tabid/57/Default.aspx)
  - (MISRA C:2012) Guidelines for the Use of the C Language in Critical Systems,
  ISBN 978-1-906400-10-1 (paperback), ISBN 978-1-906400-11-8 (PDF), March 2013.
  - (MISRA C++:2008) Guidelines for the Use of the C++ Language in Critical Systems, ISBN 978-906400-03-3 (paperback), ISBN 978-906400-04-0 (PDF), June 2008.
  - See more papers there.

- [The Power of Ten – Rules for Developing Safety Critical Code](http://spinroot.com/gerard/pdf/P10.pdf)

> Jet Propulsion Laboratory – scientific institution making a lot of research and development for NASA. JPL have been developing software for most of unmanned missions in the field of deep space and other planets exploration. Their portfolio includes such famous missions as Curiosity Mars rover and Voyager probe which left solar system after 25 years of flight and still providing scientific information. High level of automatization and long duration of missions led to superior demands to software quality. As a result of JPL amazing experience a set of code guidelines was developed and published recently.

- [JPL Institutional Coding Standard for the C Programming Language](http://lars-lab.jpl.nasa.gov/JPL_Coding_Standard_C.pdf)

- [NASA C STYLE GUIDE](http://homepages.inf.ed.ac.uk/dts/pm/Papers/nasa-c-style.pdf)

- [C++ Coding Standards and Style Guide](https://ntrs.nasa.gov/search.jsp?R=20080039927)

> This document is based on the "C Style Guide" (SEL-94-003). It contains recommendations for C++ implementations that build on, or in some cases replace, the style described in the C style guide.

- [SEI CERT C Coding Standard](https://www.securecoding.cert.org/confluence/display/c/SEI+CERT+C+Coding+Standard)

- [SEI CERT C++ Coding Standard](https://www.securecoding.cert.org/confluence/display/cplusplus)

- SEI CERT C and C++ Coding Standards are now freely available in pdf
format:
[C++ Coding Standard](http://www.cert.org/downloads/secure-coding/assets/sei-cert-cpp-coding-standard-2016-v01.pdf),
[C Coding Standard](http://www.sei.cmu.edu/downloads/sei-cert-c-coding-standard-2016-v01.pdf)

- [JOINT STRIKE FIGHTER AIR VEHICLE C++ CODING STANDARDS](http://www.stroustrup.com/JSF-AV-rules.pdf)

## Articles

- [About Safety Critical Software](http://web.archive.org/web/20110209112635/http://www.aonix.com/safety_critical_overview.html)

- [IEEE Spectrum-Why Software Fails](http://spectrum.ieee.org/computing/software/why-software-fails)

- [IEEE Spectrum-Lessons From a Decade of IT Failures](http://spectrum.ieee.org/static/lessons-from-a-decade-of-it-failures)

## Papers

- [White Paper on Approaches to Safety Engineering](http://sunnyday.mit.edu/caib/concepts.pdf)

> This white paper lays out some foundational information about different
approaches to safety: how various industries differ in their approaches to
safety engineering, and a comparison of three general approaches to safety
(system safety, industrial safety engineering, and reliability engineering).
An attempt is made to lay out the properties of industries and systems that
make one approach more appropriate than another.

- [Software Safety Standards: Evolution and Lessons Learned](http://paris.utdallas.edu/reu/document/01-Publications/04-Software-Safety-Standards-TSA.pdf)

- [An Overview of Software Safety Standards](https://www.osti.gov/scitech/servlets/purl/184397)

- [Making reliable distributed systems in the presence of software errors](http://erlang.org/download/armstrong_thesis_2003.pdf)

- [Why Do Computers Stop and What Can Be Done About It?](http://www.hpl.hp.com/techreports/tandem/TR-85.7.pdf)

- [Targeting  Safety-Related  Errors  During  Software Requirem.ents Analysis](https://trs.jpl.nasa.gov/bitstream/handle/2014/35179/93-0749.pdf)

## Incidents

- [Mars Climate Orbiter Mishap Investigation](http://sunnyday.mit.edu/accidents/MCO_report.pdf)

- [An Investigation of the Therac-25 Accidents](https://www.cs.nmt.edu/~cse382/reading/therac-25.pdf)

- [ESA ARIANE 5 Flight 501 Failure](http://sunnyday.mit.edu/accidents/Ariane5accidentreport.html)

- [ESA Schiaparelli Lander Crash](http://spacenews.com/esa-mars-lander-crash-caused-by-1-second-inertial-measurement-error/)

- [A Case Study of Toyota Unintended Acceleration and Software Safety](https://betterembsw.blogspot.de/2014/09/a-case-study-of-toyota-unintended.html) and [NASA report on the Toyota Unintended Acceleration Issue](https://www.nhtsa.gov/staticfiles/nvs/pdf/NASA-UA_report.pdf)

## Questions and Answers

#### - Which languages are used for safety-critical software?

See [Which languages are used for safety-critical software? [closed]](http://stackoverflow.com/questions/243387/which-languages-are-used-for-safety-critical-software).

#### - What is the difference between mission-critical and safety-critical software?

This article contains interesting section on what is the difference between
mission-critical and safety-critical software: [Military COTS-based systems: Not necessarily right off the shelf](http://pdf.cloud.opensystemsmedia.com/advancedtca-systems.com/SBS.Jan04.pdf)

#### - What kind of special training do engineers working on mission-critical software receive?

See [What kind of special training do engineers working on mission-critical software receive? [closed]](What_kind_of_special_training_do_engineer_working_on_mission-critical_software_receive%3F_-_Stack_Overflow.pdf) and [its followup on Reddit](https://www.reddit.com/r/programming/comments/5iohue/what_kind_of_special_training_do_engineers/). **In the Reddit thread there are 2 expanded answers**. The thread is also archived [here](What_kind_of_special_training_do_engineer_working_on_mission-critical_software_receive%3F_-_Reddit.pdf).

#### - What are the software safety standards?

See the [Software Safety Standards](#software-safety-standards) here in this list.

Also see on StackOverflow: [Coding for high reliability/availability/security - what standards do I read?](http://stackoverflow.com/questions/142722/coding-for-high-reliability-availability-security-what-standards-do-i-read)
and [Software Safety Standards](http://stackoverflow.com/questions/565965/software-safety-standards?noredirect=1&lq=1)

#### - Safety-critical software and optimising compilers?

[Safety-critical software and optimising compilers](http://softwareengineering.stackexchange.com/questions/267277/safety-critical-software-and-optimising-compilers)

#### - Does Rust have a chance in mission-critical software?

[Does Rust have a chance in mission-critical software? (currently Ada and proven C niches)](https://www.reddit.com/r/rust/comments/5iv5j7/does_rust_have_a_chance_in_missioncritical/?st=j0hrkiso&sh=3f225aa8)

## Books

- [Safety Critical Systems Handbook: A Straight forward Guide to Functional Safety, IEC 61508 (2010 EDITION) and Related Standards, Including Process IEC 61511 and Machinery IEC 62061 and ISO 13849 1st Edition](https://www.amazon.com/Safety-Critical-Systems-Handbook-Functional/dp/0080967817)

- [Engineering a Safer World. Systems Thinking Applied to Safety](https://mitpress.mit.edu/books/engineering-safer-world)

- [Computer-Related Risks](http://www.csl.sri.com/users/neumann/neumann-book.html)

- [Building High Integrity Applications with SPARK](https://www.amazon.com/Building-High-Integrity-Applications-SPARK/dp/1107656842/ref=sr_1_1?s=books&ie=UTF8&qid=1489271661&sr=1-1&keywords=high+integrity+spark)

- [Building Parallel, Embedded, and Real-Time Applications with Ada](https://www.amazon.com/Building-Parallel-Embedded-Real-Time-Applications/dp/0521197163/ref=sr_1_1?s=books&ie=UTF8&qid=1489271672&sr=1-1&keywords=embedded+ada)

- [Writing Solid Code](http://writingsolidcode.com/)

## Interviews

[Safety in Medical Device Software: Questions and Answers](http://electronicdesign.com/embedded/safety-medical-device-software-questions-and-answers)
