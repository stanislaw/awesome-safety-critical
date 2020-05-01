.. awesome-safety-critical documentation master file, created by
   sphinx-quickstart on Fri May  1 14:32:48 2020.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

:tocdepth: 2

awesome-safety-critical
=======================

.. image:: https://travis-ci.org/stanislaw/awesome-safety-critical.svg?branch=master

This is a list of resources about programming practices for writing
safety-critical software.

The starting point for me to create this resource was my interest in a solid
software:

`What kind of special training do engineers working on mission-critical software receive? [closed] <What*kind*of*special*training*do*engineer*working*on*mission-critical*software*receive%3F*-*Stack*Overflow.pdf) and [its followup on Reddit](https://www.reddit.com/r/programming/comments/5iohue/what*kind*of_special_training_do_engineers>`__

**Disclaimer:** Resources presented here are not necessarily authoritative or
latest documents on the topic.

.. About this repository
   toctree::
   maxdepth: 1
   ContentOrganization
   QA

Tags
----

.. asc-meta-summary::

Friendly lists
--------------

.. asc-meta::
    :types: List
    :keywords: Safety, Resilience

    `resilience-engineering <https://github.com/lorin/resilience-engineering>`_

    Resilience engineering papers http://resiliencepapers.club

.. asc-meta::
    :types: List
    :keywords: Quality

    `awesome-software-quality <https://github.com/ligurio/awesome-software-quality>`_

    List of free software testing and verification resources

.. asc-meta::
    :types: List
    :keywords: Verification

    `awesome-provable <https://github.com/awesomo4000/awesome-provable>`_

    A curated set of links to formal methods involving provable code.

.. asc-meta::
    :types: List
    :keywords: Verification, Formal Verification
    :companies: All

    `practical-fm <https://github.com/ligurio/practical-fm>`_

    A List of companies that use Formal methods in Software engineering

.. asc-meta::
    :types: List
    :keywords: Verification

    `awesome-static-analysis <https://github.com/mre/awesome-static-analysis>`_

    A curated list of static analysis tools, linters and code quality checkers
    for various programming languages

.. asc-meta::
    :types: List
    :keywords: Safety
    :people: Phil Koopman

    `Computer-Based System Safety Essential Reading List <https://safeautonomy.blogspot.com/p/safe-autonomy.html>`_

Resources
---------

.. asc-meta::
    :types: Resource
    :industries: Space
    :keywords: Hardware, Standards

    `European Cooperation for Space Standardization <http://ecss.nl/>`_

    The European Cooperation for Space Standardization is an initiative
    established to develop a coherent, single set of user-friendly standards for
    use in all European space activities.

    **This list has a number of links from this resource.**

.. asc-meta::
    :types: Resource
    :industries: All
    :keywords: Safety

    `The International System Safety Society <http://www.system-safety.org/>`_

    The International System Safety Society is a non-profit organization
    dedicated to supporting the Safety Professional in the application of Systems
    Engineering and Systems Management to the process of hazard, safety and risk
    analysis. The Society is international in scope and draws members throughout
    the world. It is affiliated with major corporations, educational institutions
    and other agencies in the United States and abroad.

    **This list has a number of links from this resource.**

.. asc-meta::
    :types: Resource
    :industries: Space, All
    :keywords: Formal Verification

    `NASA Langley Formal Methods Research Program <https://shemesh.larc.nasa.gov/fm/index.html>`_

    The NASA Langley's Formal Methods Research Program of the NASA Langley
    Safety-Critical Avionics Systems Branch develops formal methods technology
    for the development of mission-critical and safety-critical digital systems
    of interest to NASA.

Software safety standards
-------------------------

.. asc-meta::
    :types: Standard
    :industries: All
    :keywords: Safety, Functional Safety

    `IEC 61508 <https://en.wikipedia.org/wiki/IEC_61508>`_

    IEC 61508 is an international standard published by the International
    Electrotechnical Commission of rules applied in industry. It is titled
    Functional Safety of Electrical/Electronic/Programmable Electronic
    Safety-related Systems (E/E/PE, or E/E/PES).

.. asc-meta::
    :types: Standard
    :industries: Automotive
    :keywords: Safety, Functional Safety

    `ISO 26262 <https://en.wikipedia.org/wiki/ISO_26262>`_

    The ISO 26262 Standard is prepared by the ISO Committee and is a derivative
    of the IEC 61508 standard... The committee members include the major vehicle
    manufacturers and suppliers. It is expressly a safety standard, but includes
    details about Hazard Analysis and Risk Assessment and system design to
    detect faults and their potential failures.

.. asc-meta::
    :types: Standard
    :industries: Automotive
    :keywords: Safety, Functional Safety

    IEC 62279

    IEC 62279 provides a specific interpretation of IEC 61508 for railway
    applications. It is intended to cover the development of software for
    railway control and protection including communications, signaling and
    processing systems.

.. asc-meta::
    :types: Standard
    :industries: Nuclear
    :keywords: Safety, Functional Safety

    IEC 61513

    IEC 61513 provides requirements and recommendations for the instrumentation
    and control for systems important to safety of nuclear power plants. It
    indicates the general requirements for systems that contain conventional
    hardwired equipment, computer-based equipment or a combination of both types of
    equipment.

.. asc-meta::
    :types: Standard
    :industries: Aviation
    :keywords: Safety

    `DO-178C <https://en.wikipedia.org/wiki/DO-178C>`_

    DO-178C, Software Considerations in Airborne Systems and Equipment
    Certification is the primary document by which the certification authorities
    such as FAA, EASA and Transport Canada approve all commercial software-based
    aerospace systems. The document is published by RTCA, Incorporated, in a
    joint effort with EUROCAE, and replaces DO-178B.

    The FAA approved AC 20-115C on 19 Jul 2013, making DO-178C a recognized
    acceptable means, but not the only means, for showing compliance with the
    applicable airworthiness regulations for the software aspects of
    airborne systems and equipment certification." (Wikipedia)

.. asc-meta::
    :types: Standard
    :industries: All
    :keywords: Safety

    `ARINC standards <https://en.wikipedia.org/wiki/ARINC#Standards>`_

    The ARINC Standards are prepared by the Airlines Electronic Engineering
    Committee (AEEC) where Rockwell Collins and other aviation suppliers serve
    as a contributor in support of their airline customer base. (Wikipedia)

.. asc-meta::
    :types: Standard
    :industries: All
    :keywords: Safety, RTOS

    `ARINC 653 <https://en.wikipedia.org/wiki/ARINC_653>`_

    ARINC 653 is a standard Real Time Operating System (RTOS) interface for
    partitioning of computer resources in the time and space domains. The
    standard also specifies Application Program Interfaces (APIs) for
    abstraction of the application from the underlying hardware and software.

.. asc-meta::
    :types: Standard
    :industries: All
    :keywords: Safety

    `MIL-STD-882E, System Safety <http://www.system-safety.org/Documents/MIL-STD-882E.pdf>`_

.. asc-meta::
    :types: Standard
    :industries: All
    :keywords: Safety

    `MIL-STD-1472G, Human Engineering <http://everyspec.com/MIL-STD/MIL-STD-1400-1499/download.php?spec=MIL-STD-1472G.039997.pdf>`_

.. asc-meta::
    :types: Standard
    :keywords: Safety
    :industries: Space, All
    :companies: NASA

    `NASA-STD-8719.13B, NASA Software Safety Standard <http://www.system-safety.org/Documents/NASA-STD-8719.13B.pdf>`_

.. asc-meta::
    :types: Standard
    :industries: Space
    :companies: ESA

    `ECSS-E-ST-40C, Software <http://ecss.nl/standard/ecss-e-st-40c-software-general-requirements/>`_

.. asc-meta::
    :types: Standard
    :industries: Space
    :companies: ESA

    `ECSS-Q-ST-80C Rev.1 – Software product assurance <http://ecss.nl/standard/ecss-q-st-80c-rev-1-software-product-assurance-15-february-2017/>`_


Handbooks
---------

.. asc-meta::
    :types: Handbook
    :industries: Space
    :companies: ESA

    `ECSS-E-HB-40A – Software engineering handbook <http://ecss.nl/hbstms/ecss-e-hb-40a-software-engineering-handbook-11-december-2013/>`_

.. asc-meta::
    :types: Handbook
    :industries: Space
    :companies: NASA
    :keywords: Safety

    `NASA Software Safety Guidebook <http://www.system-safety.org/Documents/NASA-GB-8719.13.pdf>`_

    NASA's Software Safety Guidebook (pdf file). The handbook complement to the
    Software Safety Standard.

.. asc-meta::
    :types: Handbook
    :industries: Space
    :companies: NASA
    :keywords: Systems Engineering, Safety

    `NASA Systems Engineering Handbook <https://www.nasa.gov/connect/ebooks/nasa-systems-engineering-handbook>`_

.. asc-meta::
    :types: Handbook
    :industries: Space
    :companies: NASA
    :keywords: Fault Management, Safety

    `NASA Fault Management Handbook <https://www.nasa.gov/pdf/636372main_NASA-HDBK-1002_Draft.pdf>`_

    `The Development of NASA’s Fault Management Handbook (Slides) <https://indico.esa.int/event/62/contributions/2777/attachments/2297/2653/1125_-_the-development-of-nasas-fault-management-handbook_Presentation.pdf>`_

.. asc-meta::
    :types: Handbook
    :industries: All
    :companies: NASA
    :keywords: Safety, Safety Culture

    `NASA Safety Culture Handbook <https://standards.nasa.gov/standard/nasa/nasa-hdbk-870924>`_

.. asc-meta::
    :types: Handbook
    :industries: All
    :keywords: Safety

    `Software System Safety Handbook <http://www.system-safety.org/Documents/Software_System_Safety_Handbook.pdf>`_

    From the Joint Services Computer Resources Management Group, US Navy,
    US Army, And US Air Force (pdf file)

.. asc-meta::
    :types: Handbook
    :industries: All
    :keywords: Safety

    `Joint Software Systems Safety Engineering Handbook <http://www.system-safety.org/Documents/SOFTWARE_SYSTEM_SAFETY_HDBK_2010.pdf>`_

.. asc-meta::
    :types: Handbook
    :industries: All
    :keywords: Safety, System Safety

    `Air Force System Safety Handbook <http://www.system-safety.org/Documents/AF_System-Safety-HNDBK.pdf>`_

    First chapter has an excellent introduction to system safety with a
    discussion of the evolution of the DoD Standard 882 (DOD Standard Practice
    for System Safety).

.. asc-meta::
    :types: Handbook
    :industries: Space
    :companies: ESA
    :keywords: Technology Readiness Level

    `European Space Agency - Technology Readiness Levels Handbook for Space Applications <https://artes.esa.int/sites/default/files/TRL_Handbook.pdf>`_

Coding guidelines
-----------------

.. asc-meta::
    :types: Coding guidelines
    :keywords: MISRA
    :languages: C, C++
    :industries: All


    `MISRA guidelines <https://www.misra.org.uk/Publications/tabid/57/Default.aspx>`_

    (MISRA C:2012) Guidelines for the Use of the C Language in Critical Systems,

    ISBN 978-1-906400-10-1 (paperback), ISBN 978-1-906400-11-8 (PDF), March 2013.

    (MISRA C++:2008) Guidelines for the Use of the C++ Language in Critical Systems, ISBN 978-906400-03-3 (paperback), ISBN 978-906400-04-0 (PDF), June 2008.

    See more papers there.

.. asc-meta::
    :types: Coding guidelines
    :keywords: AUTOSAR
    :languages: C++
    :industries: All, Automotive

    `AUTOSAR C++14: Guidelines for the use of the C++14 language in critical and safety-related systems <https://www.autosar.org/fileadmin/user_upload/standards/adaptive/17-03/AUTOSAR_RS_CPP14Guidelines.pdf>`_

.. asc-meta::
    :types: Coding guidelines
    :languages: C, C++
    :industries: All, Space
    :companies: NASA, JPL

    `The Power of Ten – Rules for Developing Safety Critical Code <Backup/P10.pdf>`_

.. asc-meta::
    :types: Coding guidelines
    :languages: C
    :industries: All, Space
    :companies: NASA, JPL

    `JPL Institutional Coding Standard for the C Programming Language <https://lars-lab.jpl.nasa.gov/JPL_Coding_Standard_C.pdf>`_

.. asc-meta::
    :types: Coding guidelines
    :languages: C
    :industries: All, Space
    :companies: NASA

    `NASA C STYLE GUIDE <Backup/nasa-c-style.pdf>`_

.. asc-meta::
    :types: Coding guidelines
    :languages: C++
    :industries: All, Space
    :companies: NASA

    `C++ Coding Standards and Style Guide <https://ntrs.nasa.gov/search.jsp?R=20080039927>`_

    This document is based on the "C Style Guide" (SEL-94-003). It contains recommendations for C++ implementations that build on, or in some cases replace, the style described in the C style guide.

.. asc-meta::
    :types: Coding guidelines
    :languages: C
    :industries: All

    `SEI CERT C Coding Standard <https://www.securecoding.cert.org/confluence/display/c/SEI+CERT+C+Coding+Standard>`_

    SEI CERT C and C++ Coding Standards are now freely available in pdf format:
    `C Coding Standard <http://www.sei.cmu.edu/downloads/sei-cert-c-coding-standard-2016-v01.pdf>`_

.. asc-meta::
    :types: Coding guidelines
    :languages: C++
    :industries: All

    `SEI CERT C++ Coding Standard <https://www.securecoding.cert.org/confluence/display/cplusplus>`_

    SEI CERT C and C++ Coding Standards are now freely available in pdf format:
    `C++ Coding Standard <http://www.cert.org/downloads/secure-coding/assets/sei-cert-cpp-coding-standard-2016-v01.pdf>`_

.. asc-meta::
    :types: Coding guidelines
    :languages: C++
    :industries: All

    `JOINT STRIKE FIGHTER AIR VEHICLE C++ CODING STANDARDS <http://www.stroustrup.com/JSF-AV-rules.pdf>`_

    also video: `CppCon2014: Bill Emshoff "Using C++ on Mission and Safety Critical Platforms <https://www.youtube.com/watch?v=sRe77Mdna0Y&list=WL&index=2&t=1245s>`_

Topics
------

Certification
~~~~~~~~~~~~~

.. asc-meta::
    :types: Presentation
    :keywords: Certification
    :industries: All
    :companies: AdaCore

    `Introduction to Certification by Quentin Ochem, AdaCore <http://idl.univ-brest.fr/etr11/EXPOSES%20ETR%202011/mercredi%20AM/etr11-ochem.pptx>`_

.. asc-meta::
    :types: Article
    :industries: All
    :keywords: Certification

    `Certification Requirements for Safety-Critical Software <Backup/Certification-Requirements-for-Safety-Critical-Software-RTC-Magazine.pdf>`_

.. asc-meta::
    :types: Article
    :industries: All
    :companies: ESA, NASA
    :keywords: Certification, Technology Readiness Level

    `Technology Readiness Level, ESA <http://sci.esa.int/sci-ft/50124-technology-readiness-level>`_,
    `Technology Readiness Level, NASA <https://www.nasa.gov/directorates/heo/scan/engineering/technology/txt_accordion1.html>`_

    Technology Readiness Levels (TRL) are a type of measurement system used to
    assess the maturity level of a particular technology. Each technology
    project is evaluated against the parameters for each technology level and is
    then assigned a TRL rating based on the projects progress. There are nine
    technology readiness levels. TRL 1 is the lowest and TRL 9 is the highest.

Formal verification
~~~~~~~~~~~~~~~~~~~

.. asc-meta::
    :types: Article
    :industries: All
    :companies: INRIA
    :keywords: Formal Verification

    `Verified Squared: Does Critical Software Deserve Verified Tools? <http://gallium.inria.fr/~xleroy/publi/popl11-invited-talk.pdf>`_

MC/DC
~~~~~

.. asc-meta::
    :types: Paper
    :industries: All
    :companies: NASA
    :keywords: MC/DC

    `A practical approach to Modified Condition/Decision Coverage <https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/20040086014.pdf>`_

    This paper provides a practical 5-step approach for assessing MC/DC for
    aviation software products, and an analysis of some types of errors expected
    to be caught when MC/DC is achieved.

.. asc-meta::
    :types: Paper
    :industries: All
    :companies: NASA
    :keywords: MC/DC

    `A Practical Tutorial on Modified Condition/Decision Coverage <https://shemesh.larc.nasa.gov/fm/papers/Hayhurst-2001-tm210876-MCDC.pdf>`_

    This tutorial provides a practical approach to assessing modified
    condition/decision coverage (MC/DC) for aviation software products that must
    comply with regulatory guidance for DO-178B level A software.

.. asc-meta::
    :types: Paper
    :industries: All
    :companies: NASA
    :keywords: MC/DC

    `An Empirical Evaluation of the MC/DC Coverage Criterion on the HETE-2 Satellite Software <http://sunnyday.mit.edu/papers/dupuy.pdf>`_

    ...In this paper, we present the results of an empirical study that compared
    functional testing and functional testing augmented with test cases to
    satisfy MC/DC coverage. The evaluation was performed during the testing of
    the attitude control software for the HETE-2 (High Energy Transient
    Explorer) scientific satellite...

Articles
--------

.. asc-meta::
    :types: Article
    :industries: All

    `About Safety Critical Software <http://web.archive.org/web/20110209112635/http://www.aonix.com/safety_critical_overview.html>`_

.. asc-meta::
    :types: Article
    :industries: All

    `IEEE Spectrum-Why Software Fails <http://spectrum.ieee.org/computing/software/why-software-fails>`_

.. asc-meta::
    :types: Article
    :industries: All

    `IEEE Spectrum-Lessons From a Decade of IT Failures <http://spectrum.ieee.org/static/lessons-from-a-decade-of-it-failures>`_

Papers
------

.. asc-meta::
    :types: Paper
    :industries: All
    :people: Nancy Leveson

    `White Paper on Approaches to Safety Engineering <http://sunnyday.mit.edu/caib/concepts.pdf>`_

    This white paper lays out some foundational information about different
    approaches to safety: how various industries differ in their approaches to
    safety engineering, and a comparison of three general approaches to safety
    (system safety, industrial safety engineering, and reliability engineering).
    An attempt is made to lay out the properties of industries and systems that
    make one approach more appropriate than another.

.. asc-meta::
    :types: Paper
    :industries: All
    :keywords: Safety Standards, Software Safety Standards

    `Software Safety Standards: Evolution and Lessons Learned <http://paris.utdallas.edu/reu/document/01-Publications/04-Software-Safety-Standards-TSA.pdf>`_

.. asc-meta::
    :types: Paper
    :industries: All
    :keywords: Safety Standards, Software Safety Standards

    `An Overview of Software Safety Standards <https://www.osti.gov/scitech/servlets/purl/184397>`_

.. asc-meta::
    :types: Paper
    :industries: All
    :people: Joe Armstrong

    `Making reliable distributed systems in the presence of software errors <http://erlang.org/download/armstrong_thesis_2003.pdf>`_

.. asc-meta::
    :types: Paper
    :industries: All

    `Why Do Computers Stop and What Can Be Done About It? <http://www.hpl.hp.com/techreports/tandem/TR-85.7.pdf>`_

.. asc-meta::
    :types: Paper
    :industries: All
    :keywords: Requirements

    `Targeting Safety-Related  Errors  During  Software Requirements Analysis <https://trs.jpl.nasa.gov/bitstream/handle/2014/35179/93-0749.pdf>`_

.. asc-meta::
    :types: Paper
    :industries: All, Medical
    :people: Richard Cook

    `How Complex Systems Fail <http://web.mit.edu/2.75/resources/random/How%20Complex%20Systems%20Fail.pdf>`_

.. asc-meta::
    :types: Paper
    :industries: All
    :keywords: Certification

    `The Qualification of Software Development Tools From the DO-178B Certification Perspective <http://static1.1.sqspcdn.com/static/f/702523/9272430/1288904989327/200604-Kornecki.pdf?token=uZElb5dHWyIfQeLIZnOpSN5BG%2FE%3D>`_

.. asc-meta::
    :types: Paper
    :keywords: Accidents
    :industries: All, Space
    :people: Nancy Leveson

    `The Role of Software in Spacecraft Accidents <http://sunnyday.mit.edu/papers/jsr.pdf>`_

Reports
-------

.. asc-meta::
    :types: Report
    :industries: Space
    :people: Nancy Leveson

    `An Assessment of Space Shuttle Flight Software Development Processes <https://ntrs.nasa.gov/archive/nasa/casi.ntrs.nasa.gov/19930019745.pdf>`_

.. asc-meta::
    :types: Report
    :industries: Nuclear

    `Licensing of safety critical software for nuclear reactors (2018) <https://www.base.bund.de/SharedDocs/Downloads/BASE/EN/reports/kt/Report-Software.pdf?__blob=publicationFile&v=2>`_

    Common position of international nuclear regulators and authorised technical support organisations

.. asc-meta::
    :types: Report
    :industries: Automotive
    :keywords: Safety Standards

    `Assessment of Safety Standards for Automotive Electronic Control Systems <https://www.nhtsa.gov/sites/nhtsa.dot.gov/files/812285_electronicsreliabilityreport.pdf>`_

    Van Eikema Hommes, Q. D. (2016, June). Assessment of safety standards for
    automotive electronic control systems. (Report No. DOT HS 812 285).
    Washington, DC: National Highway Traffic Safety Administration.

Accidents
---------

.. asc-meta::
    :types: Resource
    :industries: All
    :keywords: Accidents

    `Failure Knowledge Database <http://www.shippai.org/fkd/en/index.html>`_

.. asc-meta::
    :types: Accident Report
    :industries: Space
    :keywords: Accidents
    :people: Nancy Leveson

    `Mars Climate Orbiter Mishap Investigation <http://sunnyday.mit.edu/accidents/MCO_report.pdf>`_

.. asc-meta::
    :types: Accident Report
    :industries: Space
    :keywords: Accidents

    `Report on the Loss of the Mars Polar Lander and Deep Space 2 Missions <https://spaceflight.nasa.gov/spacenews/releases/2000/mpl/mpl_report_1.pdf>`_

.. asc-meta::
    :types: Accident Report
    :industries: Medical
    :keywords: Accidents
    :people: Nancy Leveson

    `An Investigation of the Therac-25 Accidents <https://www.cs.nmt.edu/~cse382/reading/therac-25.pdf>`_ (original paper),
    `Medical Devices: The Therac-25 (updated version of the paper) <http://sunnyday.mit.edu/papers/therac.pdf>`_,
    `Killed by a Machine: The Therac-25 <https://hackaday.com/2015/10/26/killed-by-a-machine-the-therac-25>`_ (article)

.. asc-meta::
    :types: Accident Report
    :industries: Space
    :companies: ESA
    :keywords: Accidents
    :people: Nancy Leveson

    `ESA ARIANE 5 Flight 501 Failure <http://sunnyday.mit.edu/accidents/Ariane5accidentreport.html>`_

.. asc-meta::
    :types: Accident Report
    :industries: Space
    :companies: ESA
    :keywords: Accidents

    `ExoMars 2016 - Schiaparelli Anomaly Inquiry (PDF at the bottom) <http://exploration.esa.int/mars/59176-exomars-2016-schiaparelli-anomaly-inquiry>`_,
    `ESA Schiaparelli Lander Crash <http://spacenews.com/esa-mars-lander-crash-caused-by-1-second-inertial-measurement-error>`_

.. asc-meta::
    :types: Accident Report
    :keywords: Accidents
    :industries: Automotive
    :companies: NASA
    :people: Phil Koopman

    `A Case Study of Toyota Unintended Acceleration and Software Safety <https://betterembsw.blogspot.de/2014/09/a-case-study-of-toyota-unintended.html>`_
    and
    `NASA report on the Toyota Unintended Acceleration Issue <https://www.nhtsa.gov/staticfiles/nvs/pdf/NASA-UA_report.pdf>`_

Books
-----

.. asc-meta::
    :types: Book
    :industries: All
    :keywords: Safety, Functional Safety

    `Safety Critical Systems Handbook: A Straight forward Guide to Functional Safety, IEC 61508 (2010 EDITION) and Related Standards, Including Process IEC 61511 and Machinery IEC 62061 and ISO 13849 1st Edition <https://www.amazon.com/Safety-Critical-Systems-Handbook-Functional/dp/0080967817>`_

.. asc-meta::
    :types: Book
    :industries: All
    :keywords: Safety, System Safety

    `Engineering a Safer World. Systems Thinking Applied to Safety <https://mitpress.mit.edu/books/engineering-safer-world>`_

.. asc-meta::
    :types: Book
    :industries: All
    :keywords: Safety

    `Computer-Related Risks <http://www.csl.sri.com/users/neumann/neumann-book.html>`_

.. asc-meta::
    :types: Book
    :industries: All

    `Building High Integrity Applications with SPARK <https://www.amazon.com/Building-High-Integrity-Applications-SPARK/dp/1107656842/ref=sr_1_1?s=books&ie=UTF8&qid=1489271661&sr=1-1&keywords=high+integrity+spark>`_

.. asc-meta::
    :types: Book
    :industries: All

    `Building Parallel, Embedded, and Real-Time Applications with Ada <https://www.amazon.com/Building-Parallel-Embedded-Real-Time-Applications/dp/0521197163/ref=sr_1_1?s=books&ie=UTF8&qid=1489271672&sr=1-1&keywords=embedded+ada>`_

.. asc-meta::
    :types: Book
    :languages: C
    :industries: All

    `Writing Solid Code <http://writingsolidcode.com/>`_

.. asc-meta::
    :types: Book
    :industries: All
    :keywords: Agile Development, Safety

    `SafeScrum® – Agile Development of Safety-Critical Software <https://www.springer.com/gp/book/9783319993331>`_

Videos
------

.. asc-meta::
    :types: Video, Lecture
    :industries: All
    :keywords: Embedded, Safety
    :people: Phil Koopman

    `Embedded System Safety Lecture Video Series <https://betterembsw.blogspot.de/2017/12/embedded-system-safety-lecture-video.html>`_

.. asc-meta::
    :types: Video
    :industries: All
    :keywords: Safety, Security
    :people: Nancy Leveson

    `The Need for a Paradigm Shift in Safety and Cyber Security <https://www.youtube.com/watch?v=WBktiCyPLo4>`_

    CREDC Seminar Series. Presented on November 7, 2016 by Nancy Leveson,
    Professor of Aeronautics and Astronautics and Engineering Systems, MIT.
    Cyber Resilient Energy Delivery Consortium (CREDC), http://cred-c.org

.. asc-meta::
    :types: Video
    :industries: All, Medical
    :keywords: Safety
    :people: Richard Cook

    `Velocity 2012: Richard Cook, "How Complex Systems Fail" <https://www.youtube.com/watch?v=2S0k12uZR14>`_

    Dr. Richard Cook is the Professor of Healthcare Systems Safety and Chairman
    of the Department of Patient Safety at the Kungliga Techniska Hogskolan
    (the Royal Institute of Technology) in Stockholm, Sweden. He is a practicing
    physician, researcher and educator.

    See also paper "How Complex Systems Fail".

.. asc-meta::
    :types: Video
    :industries: All, Automotive
    :keywords: Safety, Certification

    `2017 EuroLLVM Developers’ Meeting: M. Beemster "Using LLVM for Safety-Critical Applications <https://www.youtube.com/watch?v=pmy1Ttieh3I>`_
    and
    `Using LLVM for Safety-Critical Applications. Interview with Marcel Beemster (Euro LLVM 2017) <https://www.youtube.com/watch?v=zSnfGp9HO7g>`_

    Marcel Beemster, Solid Sands B.V. http://solidsands.nl

.. asc-meta::
    :types: Video
    :industries: All, Aviation
    :companies: Airbus
    :keywords: Formal Verification

    Formal Method for Avionics Software Verification

    - `Formal Method for Avionics Software Verification pt1 (Hervé Delseny) <https://www.youtube.com/watch?v=tRtK4xOK-8o>`_

    - `Formal Method for Avionics Software Verification pt2 (Hervé Delseny) <https://www.youtube.com/watch?v=BVI5J1GAQ30>`_

    - `Formal Method for Avionics Software Verification pt3 (Hervé Delseny) <https://www.youtube.com/watch?v=U3G1ZOoqg78>`_

    - `Formal Method for Avionics Software Verification pt4 (Hervé Delseny) <https://www.youtube.com/watch?v=WtlqS-JOHrA>`_

    This talk will give examples of Airbus use of Formal Methods to verify
    avionics software, and summarises the integration of Formal Methods in the
    upcoming ED-12/DO-178 issue C. Firstly, examples of verification based on
    theorem proving or abstract interpretation will show how Airbus has already
    taken advantage of the use of Formal Methods to verify avionics software.
    Secondly, we will show how Formal Method for verification has been introduced
    in the upcoming issue C of ED-12/DO-178.

.. asc-meta::
    :types: Video
    :industries: All

    `Programming Languages for High-Assurance Vehicles <https://www.youtube.com/watch?v=3iFFYKM3CTM&feature=youtu.be>`_

.. asc-meta::
    :types: Video
    :languages: C
    :industries: All, Space
    :companies: NASA, JPL
    :people: Gerard Holzmann

    `Mars Code - Gerard Holzmann, JPL Laboratory for Reliable Software (2012) <https://www.usenix.org/conference/hotdep12/workshop-program/presentation/holzmann>`_

Interviews
----------

.. asc-meta::
    :types: Interview
    :industries: Medical

    `Safety in Medical Device Software: Questions and Answers <http://electronicdesign.com/embedded/safety-medical-device-software-questions-and-answers>`_

Press
-----

.. asc-meta::
    :types: Press
    :industries: Space

    `They Write the Right Stuff <https://www.fastcompany.com/28121/they-write-right-stuff>`_

    This software is the work of 260 women and men based in an anonymous office
    building across the street from the Johnson Space Center in Clear Lake,
    Texas, southeast of Houston. They work for the “on-board shuttle group,” a
    branch of Lockheed Martin Corps space mission systems division, and their
    prowess is world renowned: the shuttle software group is one of just four
    outfits in the world to win the coveted Level 5 ranking of the federal
    governments Software Engineering Institute (SEI) a measure of the
    sophistication and reliability of the way they do their work. In fact, the
    SEI based it standards in part from watching the on-board shuttle group do
    its work.

License
-------

.. raw:: html

    <p xmlns:dct="http://purl.org/dc/terms/">

    <a rel="license" href="http://creativecommons.org/publicdomain/zero/1.0/">
      <img src="http://i.creativecommons.org/p/zero/1.0/88x31.png" style="border-style: none;" alt="CC0" />
    </a>

    <br />

    To the extent possible under law,
    <a rel="dct:publisher" href="https://github.com/stanislaw">
      <span property="dct:title">Stanislav Pankevich</span>
    </a>
    has waived all copyright and related or neighboring rights to

    <span property="dct:title">awesome-safety-critical</span>.
    </p>

    This list's repository contains a backup of all content presented in the list.
    This is done to ensure availability of these resources in case if their original
    sources become unavailable. Every link always points to its original source
    unless it becomes unavailable in which case a resource from a backup is used
    or a link to web.archive.org if possible.

    <a href="https://github.com/dkhamsing/awesome_bot">awesome_bot</a> tool is
    used to check the dead links.
