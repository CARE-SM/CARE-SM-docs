# Corporal measurement

### Data visualization

The module shows how the individual, defined as a patient, possesses a personal attribute which is a body measurement (e.g. weight, height). This patient participates in a data capture process that has as output, the value of this examination and its units.

<p align="center">
    <a href="https://raw.githubusercontent.com/CARE-SM/CARE-Semantic-Model/main/images/CARE-SM-Body_measurement.png" target="_blank">
        <img src="https://raw.githubusercontent.com/CARE-SM/CARE-Semantic-Model/main/images/CARE-SM-Body_measurement.png">
    </a>
</p>


**OBO Foundry terms used:**

OBI:patient role: http://purl.obolibrary.org/obo/OBI_0000093

NCIT:Data capture: http://purl.obolibrary.org/obo/NCIT_C142470

NCIT:Observation Result: http://purl.obolibrary.org/obo/NCIT_C70856

NCIT:Personal Atribute: http://purl.obolibrary.org/obo/NCIT_C19332

NCIT:Weight: http://purl.obolibrary.org/obo/NCIT_C25208

NCIT:Height: http://purl.obolibrary.org/obo/NCIT_C25347

NCIT:Body Mass Index: http://purl.obolibrary.org/obo/NCIT_C16358

UO:Kilogram: http://purl.obolibrary.org/obo/UO_0000009


# Laboratory measurement

### Data visualization

The module shows how the individual, defined as a patient, participates in a laboratory testing process. At this process, the target of this medical intervention is defined, being a chemical component structure from an individual's body, the input is defined as the anatomic structure where this substance is extracted. Also this procedure has as output the observational result from this test and its value, measured among its unit of measurement.

<p align="center">
    <a href="https://raw.githubusercontent.com/CARE-SM/CARE-Semantic-Model/main/images/CARE-SM-Laboratory.png" target="_blank">
        <img src="https://raw.githubusercontent.com/CARE-SM/CARE-Semantic-Model/main/images/CARE-SM-Laboratory.png">
    </a>
</p>


**OBO Foundry terms used:**

OBI:patient role: http://purl.obolibrary.org/obo/OBI_0000093

NCIT:Laboratory procedure: http://purl.obolibrary.org/obo/NCIT_C25294

NCIT:Creatinine Clearance Adjusted for BSA: http://purl.obolibrary.org/obo/NCIT_C147324

NCIT:Observation Result: http://purl.obolibrary.org/obo/NCIT_C70856

NCIT:Anatomic Structure, System, or Substance: http://purl.obolibrary.org/obo/NCIT_C12219

NCIT:Blood: http://purl.obolibrary.org/obo/NCIT_C12434

NCIT:Drug, Food, Chemical or Biomedical Material: http://purl.obolibrary.org/obo/NCIT_C1908

NCIT:Creatinine: http://purl.obolibrary.org/obo/NCIT_C399

UO:Milligram: http://purl.obolibrary.org/obo/UO_0000022


# Medical imaging

### Data visualization

The module shows how the individual, defined as a patient, participates in a medical imaging procedure that has as output, the resulting medical image (measured the source image ID) referencing its imaging finding. At this process, the target of this medical image is defined, being an anatomic structure or substance from an individual's body.

<p align="center">
    <a href="https://raw.githubusercontent.com/CARE-SM/CARE-Semantic-Model/main/images/CARE-SM-Imaging.png" target="_blank">
        <img src="https://raw.githubusercontent.com/CARE-SM/CARE-Semantic-Model/main/images/CARE-SM-Imaging.png">
    </a>
</p>


**OBO Foundry terms used:**

OBI:patient role: http://purl.obolibrary.org/obo/OBI_0000093

NCIT:Imaging Technique: http://purl.obolibrary.org/obo/NCIT_C17369

NCIT:X-Ray Imaging: http://purl.obolibrary.org/obo/NCIT_C38101

NCIT:Anatomic Structure, System, or Substance: http://purl.obolibrary.org/obo/NCIT_C12219

NCIT:Head: http://purl.obolibrary.org/obo/NCIT_C12419

NCIT:Image Identifier: http://purl.obolibrary.org/obo/NCIT_C81289


# Genetic assessment

This module describes the data element in the Common Data Elemments group. These elements, defined by the JRC, can be found on the EU RD Platform at [this link](https://eu-rd-platform.jrc.ec.europa.eu/sites/default/files/CDS/EU_RD_Platform_CDS_Final.pdf).

### Data visualization

The module shows how the individual, defined as a patient, participates in a genetic testing process related to identifying a patient genetic variants mutation using the gene and genetic variant identifiers (coded using HGVS/HGNC/OMIM nomenclature). Zygosity is also included as a genetic attribute referring to the output genetic variant. Specific molecular process and anatomical input samples are also included, associated with the genetic testing process.

<p align="center">
    <a href="https://raw.githubusercontent.com/CARE-SM/CARE-Semantic-Model/main/images/CARE-SM-Genotype.png" target="_blank">
        <img src="https://raw.githubusercontent.com/CARE-SM/CARE-Semantic-Model/main/images/CARE-SM-Genotype.png">
    </a>
</p>

**OBO Foundry terms used:**

OBI:patient role: http://purl.obolibrary.org/obo/OBI_0000093

NCIT:Genetic Testing: http://purl.obolibrary.org/obo/NCIT_C15709

NCIT:Microarray Analysis: http://purl.obolibrary.org/obo/NCIT_C18477

NCIT:Blood Sample: http://purl.obolibrary.org/obo/NCIT_C17610 

NCIT:Gene: http://purl.obolibrary.org/obo/NCIT_C16612

NCIT:Gene Variant: http://purl.obolibrary.org/obo/NCIT_C97927

NCIT:Protein: http://purl.obolibrary.org/obo/NCIT_C17021

NCIT:Messenger RNA: http://purl.obolibrary.org/obo/NCIT_C813

NCIT:Transfer RNA: http://purl.obolibrary.org/obo/NCIT_C816

NCIT:Mitochondrial RNA: http://purl.obolibrary.org/obo/NCIT_C25975

GENO:hemizygosity: http://purl.obolibrary.org/obo/GENO_0000134

GENO:heterozygosity: http://purl.obolibrary.org/obo/GENO_0000135

GENO:homozygosity: http://purl.obolibrary.org/obo/GENO_0000136

GENO:nullizygosity: http://purl.obolibrary.org/obo/GENO_0000978

GENO:compound heterozygosity: http://purl.obolibrary.org/obo/GENO_0000402