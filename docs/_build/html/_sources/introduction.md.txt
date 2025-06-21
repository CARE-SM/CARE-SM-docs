# Introduction

<p align="center"> 
    <img src="https://github.com/CARE-SM/CARE-SM-docs/blob/main/docs/assets/care-sm.png?raw=true"width="400" height="400"> 
<p align="center" > </p> 
<p align="center"><b>Take CARE of your data! FAIRly!</b></p>
<hr>

CARE-SM is a more robust and matured representation of its precursor, the Common Data Element (CDE) semantic data model. The primary objective of its creation was to develop a semantic data model capable of representing [a set of common data elements for rare diseases registration](https://eu-rd-platform.jrc.ec.europa.eu/sites/default/files/CDS/EU_RD_Platform_CDS_Final.pdf) recommended by the European Commission Joint Research Centre. CARE-SM stands as the matured iteration of this CDE semantic model, extending its capabilities to encompass the representation of all data elements pertinent to patient registries and clinical encounters.

CARE-SM is built upon the [Semanticscience Integrated Ontology (SIO)](https://doi.org/10.1186/2041-1480-5-14) as its core structural schema. SIO is used to define every concept within the data model, utilizing upper-class classes and properties. This knowledge graph serves as a "scaffold" that holds every data element within its structure. By a combination of these instances defined by SIO, it becomes possible to represent every clinical entry comprehensively.

Moreover, each instance within CARE-SM is associated with a domain-specific ontological class from the [OBO Foundry](http://obofoundry.org/). For instance, the representation of patient birthdate is described at an upper-class level using the ontological term [SIO:attribute](http://semanticscience.org/resource/SIO_000614) and, at a domain-specific level, as [ncit:Birthdate](http://purl.obolibrary.org/obo/NCIT_C68615). This dual ontological characterization enhances data interoperability and precise semantic descriptions.

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
  - [Birthdate](https://care-sm.readthedocs.io/en/latest/data_elements.html#birthdate)
  - [Birthyear](https://care-sm.readthedocs.io/en/latest/data_elements.html#birthyear)
  - [Deathdate](https://care-sm.readthedocs.io/en/latest/data_elements.html#deathdate)
  - [Sex](https://care-sm.readthedocs.io/en/latest/data_elements.html#sex)
  - [Education level](https://care-sm.readthedocs.io/en/latest/data_elements.html#education-level)

- **Participation and timeline:**
  - [First confirmed visit](https://care-sm.readthedocs.io/en/latest/data_elements.html#birthdate)
  - [Participation status](https://care-sm.readthedocs.io/en/latest/data_elements.html#participation-status)
  - [Symptoms onset](https://care-sm.readthedocs.io/en/latest/data_elements.html#symptoms-onset)

- **Conditions and findings:**
  - [Diagnosis](https://care-sm.readthedocs.io/en/latest/data_elements.html#diagnosis)
  - [Phenotype](https://care-sm.readthedocs.io/en/latest/data_elements.html#phenotype)

- **Clinical measurements:**
  - [Corporal measurement](https://care-sm.readthedocs.io/en/latest/data_elements.html#corporal-measurements)
  - [Laboratory measurement](https://care-sm.readthedocs.io/en/latest/data_elements.html#laboratory-measurement)
  - [Medical imaging](https://care-sm.readthedocs.io/en/latest/data_elements.html#medical-imaging)
  - [Genetic testing](https://care-sm.readthedocs.io/en/latest/data_elements.html#genetic-testing)

- **Treatments and interventions:**
  - [Medication](https://care-sm.readthedocs.io/en/latest/data_elements.html#medication)
  - [Surgery](https://care-sm.readthedocs.io/en/latest/data_elements.html#surgical-intervention)

- **Patient-reported outcomes:**
  - [Questionnaire](https://care-sm.readthedocs.io/en/latest/data_elements.html#questionnaire)
  - [Disability](https://care-sm.readthedocs.io/en/latest/data_elements.html#disability)

- **Research samples:**
  - [Biobank](https://care-sm.readthedocs.io/en/latest/data_elements.html#biobank)
  - [Consent](https://care-sm.readthedocs.io/en/latest/data_elements.html#consent)
  - [Clinical trial](https://care-sm.readthedocs.io/en/latest/data_elements.html#clinical-trial)