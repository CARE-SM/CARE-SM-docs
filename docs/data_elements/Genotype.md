# Genetic assessment

This module describes the data element in the Common Data Elemments group. These elements, defined by the JRC, can be found on the EU RD Platform at [this link](https://eu-rd-platform.jrc.ec.europa.eu/sites/default/files/CDS/EU_RD_Platform_CDS_Final.pdf).

## Data visualization:

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