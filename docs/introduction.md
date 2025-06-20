# Introduction

CARE-SM is a more robust and matured representation of its precursor, the Common Data Element (CDE) semantic data model. The primary objective of its creation was to develop a semantic data model capable of representing [a set of common data elements for rare diseases registration](https://eu-rd-platform.jrc.ec.europa.eu/sites/default/files/CDS/EU_RD_Platform_CDS_Final.pdf) recommended by the European Commission Joint Research Centre. CARE-SM stands as the matured iteration of this CDE semantic model, extending its capabilities to encompass the representation of all data elements pertinent to patient registries and clinical encounters.

CARE-SM is built upon the [Semanticscience Integrated Ontology (SIO)](https://doi.org/10.1186/2041-1480-5-14) as its core structural schema. SIO is used to define every concept within the data model, utilizing upper-class classes and properties. This knowledge graph serves as a "scaffold" that holds every data element within its structure. By a combination of these instances defined by SIO, it becomes possible to represent every clinical entry comprehensively.

Moreover, each instance within CARE-SM is associated with a domain-specific ontological class from the [OBO Foundry](http://obofoundry.org/). For instance, the representation of patient birthdate is described at an upper-class level using the ontological term [SIO:attribute](http://semanticscience.org/resource/SIO_000614) and, at a domain-specific level, as [ncit:Birthdate](http://purl.obolibrary.org/obo/NCIT_C68615). This dual ontological characterization enhances data interoperability and precise semantic descriptions.


## Motivation and Goals

CARE-SM provides a common structure to map healthcare-related concepts to machine-readable knowledge graphs.

- Enable semantic interoperability 


## Genesis of CARE-SM

CARE-SM is a more robust and matured representation of its precursor, the Common Data Element (CDE) semantic data model. The primary objective of its creation was to develop a semantic data model capable of representing [a set of common data elements for rare diseases registration](https://eu-rd-platform.jrc.ec.europa.eu/sites/default/files/CDS/EU_RD_Platform_CDS_Final.pdf) recommended by the European Commission Joint Research Centre. CARE-SM stands as the matured iteration of this CDE semantic model, extending its capabilities to encompass the representation of all data elements pertinent to patient registries and clinical encounters.

# Foundational design of CARE-SM

## Core Structure

CARE-SM is built upon the [Semanticscience Integrated Ontology (SIO)](https://doi.org/10.1186/2041-1480-5-14) as its core structural schema. SIO is used to define every concept within the data model, utilizing upper-class classes and properties. This knowledge graph serves as a "scaffold" that holds every data element within its structure (see Figure 1). By a combination of these instances defined by SIO, it becomes possible to represent every clinical entry comprehensively.

Moreover, each instance within CARE-SM is associated with a domain-specific ontological class from the [OBO Foundry](http://obofoundry.org/). For instance, the representation of patient birthdate is described at an upper-class level using the ontological term [SIO:attribute](http://semanticscience.org/resource/SIO_000614) and, at a domain-specific level, as [ncit:Birthdate](http://purl.obolibrary.org/obo/NCIT_C68615). This dual ontological characterization enhances data interoperability and precise semantic descriptions.

![Figure 1: Core structure](https://raw.githubusercontent.com/CARE-SM/CARE-Semantic-Model/main/images/CARE-SM-Core.png)


## Contextual Layer

To maintain a common core structure using CARE-SM, only one data element is modeled at a time. For that reason, if you do not have that element, you do not use that particular data representation. This could lead to situations where data is not aggregated enough. To address this, a layer of metadata has been created around every data element representation (see Figure 2).

This metadata describes the context of the data represented in the core structure model, giving some temporal information to each data element. This structure is preserved even when date/time are the core observation of the model (e.g., date of symptom onset). The context layer creates a timeline of events around every data element, allowing the model to represent not only individual patient registry entries but also patient clinical encounters in a precise way.

In addition to the patient's timeline and temporal information, common context can be grouped into other arbitrary data elements by connecting them through event nodes. This event has a common context between data elements for cases where multiple data elements share a unique relationship (like conditions/treatment scenarios, visit-based aggregated information). It's not mandatory to implement this in your model, but it is made possible by the design.

This metadata requires the combination of RDF-Quads and RDF-Triples, rather than only RDF Triples used for regular knowledge graphs. The core structure of the model is represented using RDF-Quad, containing as a fourth element (Quad) the same context ID URL. This URL is used as the subject for other RDF Triples that define the metadata layer (see Figure 2).

![Figure 2: Context representation](https://raw.githubusercontent.com/CARE-SM/CARE-Semantic-Model/main/images/CARE-SM-Context.png)

Figure 2: Context representation

List of Data Elements

- **Demographics:**
  - [Birthdate](https://care-sm.readthedocs.io/en/latest/Birthdate.html)
  - [Birthyear](https://care-sm.readthedocs.io/en/latest/Birthyear.html)
  - [Deathdate](https://care-sm.readthedocs.io/en/latest/Deathdate.html)
  - [Sex](https://care-sm.readthedocs.io/en/latest/Sex.html)
  - [Education level](https://care-sm.readthedocs.io/en/latest/Education.html)

- **Participation & Timeline:**
  - [First confirmed visit](https://care-sm.readthedocs.io/en/latest/First_visit.html)
  - [Participation status](https://care-sm.readthedocs.io/en/latest/Status.html)
  - [Symptoms onset](https://care-sm.readthedocs.io/en/latest/Symptoms_onset.html)

- **Conditions and findings:**
  - [Diagnosis](https://care-sm.readthedocs.io/en/latest/Diagnosis.html)
  - [Phenotype](https://care-sm.readthedocs.io/en/latest/Phenotype.html)

- **Clinical measurements:**
  - [Corporal measurement](https://care-sm.readthedocs.io/en/latest/Body-measurement.html)
  - [Laboratory measurement](https://care-sm.readthedocs.io/en/latest/Laboratory.html)
  - [Medical imaging](https://care-sm.readthedocs.io/en/latest/Imaging.html)
  - [Genotype](https://care-sm.readthedocs.io/en/latest/Genotype.html)

- **Treatments and interventions:**
  - [Medication](https://care-sm.readthedocs.io/en/latest/Medication.html)
  - [Surgery](https://care-sm.readthedocs.io/en/latest/Surgery.html)

- **Patient-reported Outcomes:**
  - [Questionnaire](https://care-sm.readthedocs.io/en/latest/Questionnaire.html)
  - [Disability](https://care-sm.readthedocs.io/en/latest/Disability.html)

- **Research samples:**
  - [Biobank](https://care-sm.readthedocs.io/en/latest/Biobank.html)
  - [Consent](https://care-sm.readthedocs.io/en/latest/Consent.html)
  - [Clinical trial](https://care-sm.readthedocs.io/en/latest/Cclinical_trial.html)