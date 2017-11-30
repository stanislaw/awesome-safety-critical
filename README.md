# awesome-safety-critical

[![Build Status](https://travis-ci.org/stanislaw/awesome-safety-critical.svg?branch=master)](https://travis-ci.org/stanislaw/awesome-safety-critical)

This is a list of resources about programming practices for writing
safety-critical software.

The starting point for me to create this resource was my interest in a solid
software:

[What kind of special training do engineers working on mission-critical software receive? [closed]](What_kind_of_special_training_do_engineer_working_on_mission-critical_software_receive%3F_-_Stack_Overflow.pdf) and [its followup on Reddit](https://www.reddit.com/r/programming/comments/5iohue/what_kind_of_special_training_do_engineers/).

**Disclaimer:** I don't work on safety-critical software. Resources presented
here are not necessarily authoritative or latest documents on topic.

## Contents

<!-- START doctoc generated TOC please keep comment here to allow auto update -->
<!-- DON'T EDIT THIS SECTION, INSTEAD RE-RUN doctoc TO UPDATE -->
**Table of Contents**  *generated with [DocToc](https://github.com/thlorenz/doctoc)*

- [Friendly lists](#friendly-lists)
- [Resources](#resources)
- [Software safety standards](#software-safety-standards)
- [Safety guidebooks](#safety-guidebooks)
- [Coding guidelines](#coding-guidelines)
- [Topics](#topics)
  - [Certification](#certification)
  - [Formal verification](#formal-verification)
  - [MC/DC](#mcdc)
- [Articles](#articles)
- [Papers](#papers)
- [Accidents](#accidents)
- [Questions and Answers](#questions-and-answers)
- [Books](#books)
- [Videos](#videos)
- [Interviews](#interviews)
- [Press](#press)
- [License](#license)

<!-- END doctoc generated TOC please keep comment here to allow auto update -->

## Friendly lists

- [awesome-static-analysis](https://github.com/mre/awesome-static-analysis)

> A curated list of static analysis tools, linters and code quality checkers
for various programming languages

- [free-software-testing-books](https://github.com/ligurio/free-software-testing-books)

> List of free software testing resources

## Resources

- [European Cooperation for Space Standardization](http://ecss.nl/)

> The European Cooperation for Space Standardization is an initiative established to develop a coherent, single set of user-friendly standards for use in all European space activities.

**This list has a number of links from this resource.**

- [The International System Safety Society](http://www.system-safety.org/)

> The International System Safety Society is a non-profit organization dedicated to supporting the Safety Professional in the application of Systems Engineering and Systems Management to the process of hazard, safety and risk analysis.  The Society is international in scope and draws members throughout the world.  It is affiliated with major corporations, educational institutions and other agencies in the United States and abroad.

**This list has a number of links from this resource.**

- [NASA Langley Formal Methods Research Program](https://shemesh.larc.nasa.gov/fm/index.html)

> The NASA Langley's Formal Methods Research Program of the NASA Langley Safety-Critical Avionics Systems Branch develops formal methods technology for the development of mission-critical and safety-critical digital systems of interest to NASA.

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

- [NASA Systems Engineering Handbook](https://www.nasa.gov/connect/ebooks/nasa-systems-engineering-handbook)

- [Software System Safety Handbook](http://www.system-safety.org/Documents/Software_System_Safety_Handbook.pdf)

> From the Joint Services Computer Resources Management Group, US Navy, US Army,
And US Air Force (pdf file)

- [Joint Software Systems Safety Engineering Handbook](http://www.system-safety.org/Documents/SOFTWARE_SYSTEM_SAFETY_HDBK_2010.pdf)

- [Air Force System Safety Handbook](http://www.system-safety.org/Documents/AF_System-Safety-HNDBK.pdf)

> First chapter has an excellent introduction to system safety with a discussion
of the evolution of the DoD Standard 882 (DOD Standard Practice for
System Safety).

- [European Space Agency - Technology Readiness Levels Handbook for Space Applications](https://artes.esa.int/sites/default/files/TRL_Handbook.pdf)

## Coding guidelines

- [MISRA guidelines](https://www.misra.org.uk/Publications/tabid/57/Default.aspx)
  - (MISRA C:2012) Guidelines for the Use of the C Language in Critical Systems,
  ISBN 978-1-906400-10-1 (paperback), ISBN 978-1-906400-11-8 (PDF), March 2013.
  - (MISRA C++:2008) Guidelines for the Use of the C++ Language in Critical Systems, ISBN 978-906400-03-3 (paperback), ISBN 978-906400-04-0 (PDF), June 2008.
  - See more papers there.

- [The Power of Ten – Rules for Developing Safety Critical Code](Backup/P10.pdf)

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

## Topics

### Certification

- [Introduction to Certification by Quentin Ochem, AdaCore](http://idl.univ-brest.fr/etr11/EXPOSES%20ETR%202011/mercredi%20AM/etr11-ochem.pptx)

- [Certification Requirements for Safety-Critical Software](http://www.rtcmagazine.com/articles/view/100010)

- [Technology Readiness Level, ESA](http://sci.esa.int/sci-ft/50124-technology-readiness-level/), [Technology Readiness Level, NASA](https://www.nasa.gov/directorates/heo/scan/engineering/technology/txt_accordion1.html)

> Technology Readiness Levels (TRL) are a type of measurement system used to
assess the maturity level of a particular technology. Each technology project is
evaluated against the parameters for each technology level and is then assigned
a TRL rating based on the projects progress. There are nine technology readiness
levels. TRL 1 is the lowest and TRL 9 is the highest.

### Formal verification

- [Verified Squared: Does Critical Software Deserve Verified Tools?](http://gallium.inria.fr/~xleroy/publi/popl11-invited-talk.pdf)

### MC/DC

- [A practical approach to Modified Condition/Decision Coverage](https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20040086014.pdf)

> This paper provides a practical 5-step approach for assessing MC/DC for
aviation software products, and an analysis of some types of errors expected
to be caught when MC/DC is achieved.

- [A Practical Tutorial on Modified Condition/Decision Coverage](https://shemesh.larc.nasa.gov/fm/papers/Hayhurst-2001-tm210876-MCDC.pdf)

> This tutorial provides a practical approach to assessing modified
condition/decision coverage (MC/DC) for aviation software products that must
comply with regulatory guidance for DO-178B level A software.

- [An Empirical Evaluation of the MC/DC Coverage Criterion on the HETE-2 Satellite Software](http://sunnyday.mit.edu/papers/dupuy.pdf)

> ...In this paper, we present the results of an empirical study that compared
functional testing and functional testing augmented with test cases to satisfy
MC/DC coverage. The evaluation was performed during the testing of the
attitude control software for the HETE-2 (High Energy Transient Explorer)
scientific satellite...

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

- [How Complex Systems Fail](http://web.mit.edu/2.75/resources/random/How%20Complex%20Systems%20Fail.pdf)

- [The Qualification of Software Development Tools From the DO-178B Certification Perspective](http://static1.1.sqspcdn.com/static/f/702523/9272430/1288904989327/200604-Kornecki.pdf?token=uZElb5dHWyIfQeLIZnOpSN5BG%2FE%3D)

## Accidents

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

- [Release It!: Design and Deploy Production-Ready Software (Pragmatic Programmers)](https://www.amazon.com/Release-Production-Ready-Software-Pragmatic-Programmers/dp/0978739213)

> While not necessarily focused on safety-critical software, the book touches extensively on the design of high availability complex systems where failures of any size are very expensive for the owner.

## Videos

[The Need for a Paradigm Shift in Safety and Cyber Security](https://www.youtube.com/watch?v=WBktiCyPLo4)

> CREDC Seminar Series. Presented on November 7, 2016 by Nancy Leveson,
Professor of Aeronautics and Astronautics and Engineering Systems, MIT.
Cyber Resilient Energy Delivery Consortium (CREDC), http://cred-c.org

[Velocity 2012: Richard Cook, "How Complex Systems Fail"](https://www.youtube.com/watch?v=2S0k12uZR14)

> Dr. Richard Cook is the Professor of Healthcare Systems Safety and Chairman of the Department of Patient Safety at the Kungliga Techniska Hogskolan (the Royal Institute of Technology) in Stockholm, Sweden. He is a practicing physician, researcher and educator.

See also paper "How Complex Systems Fail".

[2017 EuroLLVM Developers’ Meeting: M. Beemster "Using LLVM for Safety-Critical Applications"](https://www.youtube.com/watch?v=pmy1Ttieh3I) and [Using LLVM for Safety-Critical Applications. Interview with Marcel Beemster (Euro LLVM 2017)](https://www.youtube.com/watch?v=zSnfGp9HO7g).

> Marcel Beemster, Solid Sands B.V. http://solidsands.nl/, http://www.LLVM.org/devmtg/2017-03/

## Interviews

[Safety in Medical Device Software: Questions and Answers](http://electronicdesign.com/embedded/safety-medical-device-software-questions-and-answers)

## Press

[They Write the Right Stuff](https://www.fastcompany.com/28121/they-write-right-stuff)

> This software is the work of 260 women and men based in an anonymous office
building across the street from the Johnson Space Center in Clear Lake, Texas,
southeast of Houston. They work for the “on-board shuttle group,” a branch of
Lockheed Martin Corps space mission systems division, and their prowess is
world renowned: the shuttle software group is one of just four outfits in
the world to win the coveted Level 5 ranking of the federal governments
Software Engineering Institute (SEI) a measure of the sophistication and
reliability of the way they do their work. In fact, the SEI based it standards
in part from watching the on-board shuttle group do its work.

## License

<p xmlns:dct="http://purl.org/dc/terms/">

<a rel="license"
   href="http://creativecommons.org/publicdomain/zero/1.0/">
  <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
</a>
<br />
To the extent possible under law,
<a rel="dct:publisher"
   href="https://github.com/stanislaw">
  <span property="dct:title">Stanislav Pankevich</span></a>
has waived all copyright and related or neighboring rights to
<span property="dct:title">awesome-safety-critical</span>.

</p>

This list's repository contains a backup of all content presented in the list.
This is done to ensure availability of these resources in case if their original
sources become unavailable. Every link always points to its original source
unless it becomes unavailable in which case a resource from a backup is used
or a link to web.archive.org if possible.
[awesome_bot](https://github.com/dkhamsing/awesome_bot) tool is used to check the dead links.
