# awesome-safety-critical

[![Build Status](https://travis-ci.org/stanislaw/awesome-safety-critical.svg?branch=master)](https://travis-ci.org/stanislaw/awesome-safety-critical)

This is a list of resources about programming practices for writing
safety-critical software.

**Disclaimer:** I don't work on safety-critical software so the resources
presented here are not necessarily authoritative documents on topic.

The starting point for me to create this resource was my interest in a solid
software:

[What kind of special training do engineers working on mission-critical software receive? [closed]](What_kind_of_special_training_do_engineer_working_on_mission-critical_software_receive%3F_-_Stack_Overflow.pdf) and [its followup on Reddit](https://www.reddit.com/r/programming/comments/5iohue/what_kind_of_special_training_do_engineers/).

## Standards

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

- [IEC 61508](https://en.wikipedia.org/wiki/IEC_61508)

> IEC 61508 is an international standard published by the International Electrotechnical Commission of rules applied in industry. It is titled Functional Safety of Electrical/Electronic/Programmable Electronic Safety-related Systems (E/E/PE, or E/E/PES).

- [ARINC standards](https://en.wikipedia.org/wiki/ARINC#Standards)

> The ARINC Standards are prepared by the Airlines Electronic Engineering Committee (AEEC) where Rockwell Collins and other aviation suppliers serve as a contributor in support of their airline customer base. (Wikipedia)

- [ISO 26262](https://en.wikipedia.org/wiki/ISO_26262)

> The ISO 26262 Standard is prepared by the ISO Committee and is a derivative of the IEC 61508 standard listed above.  The committee members include the major vehicle manufacturers and suppliers.  It is expressly a safety standard, but includes details about Hazard Analysis and Risk Assessment and system design to detect faults and their potential failures.


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

- [JOINT STRIKE FIGHTER AIR VEHICLE C++ CODING STANDARDS](http://www.stroustrup.com/JSF-AV-rules.pdf)

## Articles

- [IEEE Spectrum-Why Software Fails](http://spectrum.ieee.org/computing/software/why-software-fails)

- [IEEE Spectrum-Lessons From a Decade of IT Failures](http://spectrum.ieee.org/static/lessons-from-a-decade-of-it-failures)

## Papers

- [Making reliable distributed systems in the presence of software errors](http://erlang.org/download/armstrong_thesis_2003.pdf)

- [Why Do Computers Stop and What Can Be Done About It?](http://www.hpl.hp.com/techreports/tandem/TR-85.7.pdf)

- [Targeting  Safety-Related  Errors  During  Software Requirem.ents Analysis](https://trs.jpl.nasa.gov/bitstream/handle/2014/35179/93-0749.pdf)

## Incidents

- [Mars Climate Orbiter Mishap Investigation](http://sunnyday.mit.edu/accidents/MCO_report.pdf)

- [An Investigation of the Therac-25 Accidents](https://www.cs.nmt.edu/~cse382/reading/therac-25.pdf)

- [ESA ARIANE 5 Flight 501 Failure](http://sunnyday.mit.edu/accidents/Ariane5accidentreport.html)

- [ESA Schiaparelli Lander Crash](http://spacenews.com/esa-mars-lander-crash-caused-by-1-second-inertial-measurement-error/)

## Questions and Answers

- What is the difference between mission-critical and safety-critical software?

This article contains interesting section on what is the difference between
mission-critical and safety-critical software: [Military COTS-based systems: Not necessarily right off the shelf](http://pdf.cloud.opensystemsmedia.com/advancedtca-systems.com/SBS.Jan04.pdf)

- What kind of special training do engineers working on mission-critical software receive?

See [What kind of special training do engineers working on mission-critical software receive? [closed]](What_kind_of_special_training_do_engineer_working_on_mission-critical_software_receive%3F_-_Stack_Overflow.pdf) and [its followup on Reddit](https://www.reddit.com/r/programming/comments/5iohue/what_kind_of_special_training_do_engineers/). **In the Reddit thread there are 2 expanded answers**. The thread is also archived [here](What_kind_of_special_training_do_engineer_working_on_mission-critical_software_receive%3F_-_Reddit.pdf).

## Other

[Safety in Medical Device Software: Questions and Answers](http://electronicdesign.com/embedded/safety-medical-device-software-questions-and-answers)

## Books

- [Safety Critical Systems Handbook: A Straight forward Guide to Functional Safety, IEC 61508 (2010 EDITION) and Related Standards, Including Process IEC 61511 and Machinery IEC 62061 and ISO 13849 1st Edition](https://www.amazon.com/Safety-Critical-Systems-Handbook-Functional/dp/0080967817)

- [Engineering a Safer World. Systems Thinking Applied to Safety](https://mitpress.mit.edu/books/engineering-safer-world)

- [Writing Solid Code](http://writingsolidcode.com/)
