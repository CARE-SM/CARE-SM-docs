# Biobank

This module describes the data element in the Common Data Elemments group. These elements, defined by the JRC, can be found on the EU RD Platform at [this link](https://eu-rd-platform.jrc.ec.europa.eu/sites/default/files/CDS/EU_RD_Platform_CDS_Final.pdf).

### Data visualization

The module shows how the individual, defined as a patient, possesses a biological sample in a biobank, and its availability. This patient participates in a sampling procedure that has as output, the biological sample. In the module, a biobank participates as a target, measured as a global unique identifier.

<p align="center">
    <a href="https://raw.githubusercontent.com/CARE-SM/CARE-Semantic-Model/main/images/CARE-SM-Biobank.png" target="_blank">
        <img src="https://raw.githubusercontent.com/CARE-SM/CARE-Semantic-Model/main/images/CARE-SM-Biobank.png">
    </a>
</p>

**OBO Foundry terms used:**

OBI:patient role: http://purl.obolibrary.org/obo/OBI_0000093

OBIB:sampling specimens for biobank: http://purl.obolibrary.org/obo/OBIB_0000668

NCIT:Record of Retained Body Fluids or Tissue Sample: http://purl.obolibrary.org/obo/NCIT_C115570

OBIB:biobank: http://purl.obolibrary.org/obo/OBIB_0000616

NCIT:Anatomic Structure, System, or Substance: http://purl.obolibrary.org/obo/NCIT_C12219

NCIT:Cerebrospinal Fluid: http://purl.obolibrary.org/obo/NCIT_C12692


# Consent

This module describes the data element in the Common Data Elemments group. These elements, defined by the JRC, can be found on the EU RD Platform at [this link](https://eu-rd-platform.jrc.ec.europa.eu/sites/default/files/CDS/EU_RD_Platform_CDS_Final.pdf).

### Data visualization

The module shows how the individual, defined as a patient, participates in an informed consent process that has as output the permission to be contacted or reusing his/her data. This output refers to the consent given by the individual.


<p align="center">
    <a href="https://raw.githubusercontent.com/CARE-SM/CARE-Semantic-Model/main/images/CARE-SM-Consent.png" target="_blank">
        <img src="https://raw.githubusercontent.com/CARE-SM/CARE-Semantic-Model/main/images/CARE-SM-Consent.png">
    </a>
</p>

**OBO Foundry terms used:**

OBI:patient role: http://purl.obolibrary.org/obo/OBI_0000093

OBI:informed consent process: http://purl.obolibrary.org/obo/OBI_0000810

DUI:data use permission: http://purl.obolibrary.org/obo/DUO_0000001

OBIB:willingness to be contacted for a research study: http://purl.obolibrary.org/obo/OBIB_0000488

# Clinical trials

### Data visualization

The module shows how the individual, defined as a patient, possesses a medical condition which is a certain disease (measured in this case using ORDO codes). This patient participates in a clinical trial that has as output, a clinical trial report referencing its condition. At this procedure, the patient participates in a clinical institute, measured in this case as a Hospital using a global unique identifier.

<p align="center">
    <a href="https://raw.githubusercontent.com/CARE-SM/CARE-Semantic-Model/main/images/CARE-SM-Clinical_trials.png" target="_blank">
        <img src="https://raw.githubusercontent.com/CARE-SM/CARE-Semantic-Model/main/images/CARE-SM-Clinical_trials.png">
    </a>
</p>

**OBO Foundry terms used:**

OBI:patient role: http://purl.obolibrary.org/obo/OBI_0000093

NCIT:Clinical trial: http://purl.obolibrary.org/obo/NCIT_C71104

NCIT:Clinical Trial Final Report: http://purl.obolibrary.org/obo/NCIT_C115575

NCIT:Hospital: http://purl.obolibrary.org/obo/NCIT_C16696