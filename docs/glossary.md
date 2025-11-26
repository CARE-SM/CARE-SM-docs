# CARE-SM CSV Glossary Documentation

CARE-SM implements a CSV template structure to populate patient registry information. This template consists of a defined set of columns used across different data model modules. Depending on the specific module, a subset of these columns may be required, optional, or not applicable.

## CSV template columns

The following table is the complete list of available columns:

| Name               | Datatype | Description |
|--------------------|----------|-------------|
| `model`            | Literal (string)   | Tag name used to identify the specific model to generate. |
| `pid`              | Literal (integer)  | Patient unique identifier. |
| `event_id`         | Literal (integer)  | Event-specific identifier used to contextualize several data elements under the same medical visit or encounter. |
| `value`            | Literal (string, number, or date)  | Lexical value of this data element. |
| `value_datatype`   | Literal (string)   | Additional metadata of the `value` column, using the [XML Schema Definition Language (XSD)](https://www.w3.org/TR/xmlschema11-1/). Expected to be a literal such as `xsd:date` or `xsd:string`. |
| `valueIRI`         | IRI      | Full IRI-based value of the data element. |
| `activity`         | IRI      | Full conceptual IRI describing a specific process associated with this data element, such as a clinical method or route of administration. |
| `unit`             | IRI      | Full conceptual IRI describing the data element’s unit of measurement. |
| `input`            | IRI      | Full conceptual IRI defining any input associated with the clinical procedure, such as a medication used or a related tissue sample. |
| `target`           | IRI      | Full conceptual IRI defining any target associated with the clinical procedure, such as an anatomical structure or a molecule. |
| `specification`    | IRI      | Full conceptual IRI specifying any protocol or document that contextualizes the reported data element. |
| `frequency_type`   | IRI      | Full conceptual IRI defining the frequency type of the associated clinical procedure. |
| `frequency_value`  | Literal (string)  | Numerical frequency value; combined with `frequency_type`, it defines the full frequency (e.g., “2 times per month”). |
| `agent`            | IRI      | Full conceptual IRI defining an additional agent participating in the data element definition. |
| `startdate`        | Literal (ISO 8601 date)    | Start date of the the data registration or time instant when the observation was taken. If identical to `value`, it is not required. |
| `enddate`          | Literal (ISO 8601 date)    | End date of the data registration, if it 's different from `startdate`. |
| `age`              | Literal (integer)  | Age of the patient at the time of observation. |
| `comments`         | Literal (string)   | Human-readable comments or descriptions related to this data element. |
| `organisation`     | IRI      | IRI used to define the organisation identifier. |

## CSV template creation

This guide explains how to structure, populate, and utilize CSV files for patient data in CARE-SM.

1. **Create the CSV File**  
   
   This document would only allow a set of concrete columns names:
   - `model`, `pid`, `event_id`, `value`, `age`, `value_datatype`, `valueIRI`, `activity`, `unit`, `input`, `target`, `specification`, `frequency_type`, `frequency_value`, `agent`, `startdate`, `enddate`, `comments`,`organisation`, `organisation_type`.

   *Example:*
   ```text
   model,pid,event_id,value,age,value_datatype,valueIRI,activity,unit,input,target,specification,frequency_type,frequency_value,agent,startdate,enddate,comments,organisation,organisation_type
   ,,,,,,,,,,,,,,,,,,,
   ```
2. **Populate Data**  
   Each data entry needs specific fields (not all fields are mandatory). See the glossary below for details.

    *Example:*
    ```text
    model,pid,event_id,value,age,value_datatype,valueIRI,activity,unit,input,target,specification,frequency_type,frequency_value,agent,startdate,enddate,comments,organisation,organisation_type
    Diagnosis,30056,,,,,http://www.orpha.net/ORDO/Orphanet_93552,,,,,,,,,,,2006-01-19,,,,
    ```

    For more examples, refer to the [`exemplar_data`](https://github.com/CARE-SM/CARE-SM-Implementation/tree/main/CSV/data) folder.

## Data Element Glossary

**Legend:**
- ![](https://placehold.co/15x15/1589F0/1589F0.png) This column is **REQUIRED** for this case.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) This column is **OPTIONAL**. for this case
- ![](https://placehold.co/15x15/808080/808080.png) This column is **NOT APPLICABLE** for this case.
<hr>

(birthdate_glossary)=
### Birthdate

**This data element can be queried (in an aggregated and anonymized manner) through the Beacon API developed for CARE-SM. For more information, click [here](https://github.com/CARE-SM/beaconAPI4CARESM)**

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Birthdate
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: ISO 8601-formatted birthdate.
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **specification**: IRI reference to any associated protocol.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601-formatted start date of the data resgitration., could be the same of the `value`
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/808080/808080.png) **age**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **organisation**:
<hr>

(birthyear_glossary)=
### Birthyear

**This data element can be queried (in an aggregated and anonymized manner) through the Beacon API developed for CARE-SM. For more information, click [here](https://github.com/CARE-SM/beaconAPI4CARESM)**

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Birthdate
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: The year (YYYY) in which a person was born.
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **specification**: IRI reference to any associated protocol.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/808080/808080.png) **startdate**:
- ![](https://placehold.co/15x15/808080/808080.png) **enddate**:
- ![](https://placehold.co/15x15/808080/808080.png) **age**: 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **organisation**:
<hr>

(country_glossary)=
### Birthplace

**This data element can be queried (in an aggregated and anonymized manner) through the Beacon API developed for CARE-SM. For more information, click [here](https://github.com/CARE-SM/beaconAPI4CARESM)**

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Birthplace
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value**: Human-readable label of the country.
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**: 
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**:  Full IRI used as annonation code for the country at birth.
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **specification**: IRI reference to any associated protocol.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601-formatted start date of the data resgitration.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/808080/808080.png) **age**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **organisation**:
<hr>

(deathdate_glossary)=
### Deathdate

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Deathdate
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: ISO 8601-formatted date of death (not date time)
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **valueIRI**: Full IRI used as annonation code for the cause of the patient's death.
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **specification**: IRI reference to any associated protocol.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601-formatted start date of the data resgitration., could be the same of the `value`
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: The patient’s age at the time the observation was taken.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **organisation**:
<hr>

(sex_glossary)=
### Sex

**This data element can be queried (in an aggregated and anonymized manner) through the Beacon API developed for CARE-SM. For more information, click [here](https://github.com/CARE-SM/beaconAPI4CARESM)**

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Sex
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value**: Human-readable label of the concept IRI used for `valueIRI`.
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**: 
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**: Full concept IRI for the patient sex annonation.**
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **specification**: IRI reference to any associated protocol.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601-formatted start date of the data resgitration.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/808080/808080.png) **age**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **organisation**:

** If you are representing CARE-SM with the **OBO Foundry**, use the one of the following **NCIT terms**:
  - http://purl.obolibrary.org/obo/NCIT_C16576 (Female)
  - http://purl.obolibrary.org/obo/NCIT_C20197 (Male)
  - http://purl.obolibrary.org/obo/NCIT_C124294 (Undetermined)
  - http://purl.obolibrary.org/obo/NCIT_C17998 (Unknown)

<hr>

(first-visit_glossary)=
### First Confirmed Visit

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: First_visit
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value**: ISO 8601-formatted date of first confirmed visit.
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **specification**: IRI reference to any associated protocol.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601-formatted start date of the data resgitration., could be the same of the `value`
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: The patient’s age at the time the observation was taken.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **organisation**:
<hr>

(status_glossary)=
### Participation status

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Status
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value**: Human-readable label of the concept IRI used for `valueIRI`.**
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**: 
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**: Full concept IRI for the patient participation status annotation.
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **specification**: IRI reference to any associated protocol.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601-formatted start date of the data resgitration.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: The patient’s age at the time the observation was taken.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **organisation**:

** If you are representing CARE-SM with the **OBO Foundry**, use the one of the following **NCIT terms**:
  - http://purl.obolibrary.org/obo/NCIT_C37987 (Alive)
  - http://purl.obolibrary.org/obo/NCIT_C90387 (Found Dead)
  - http://purl.obolibrary.org/obo/NCIT_C70740 (Subject Lost to Follow Up)
  - http://purl.obolibrary.org/obo/NCIT_C124784 (Refusal To Participate)
<hr>

(symptoms_onset_glossary)=
### Symptoms onset

**This data element can be queried (in an aggregated and anonymized manner) through the Beacon API developed for CARE-SM. For more information, click [here](https://github.com/CARE-SM/beaconAPI4CARESM)**

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Symptoms_onset
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: One of the following:
  * Age of the symptoms onset.
  * ISO 8601-formatted date of the symptoms occurrence.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value_datatype**: XSD datatype that defines `value` column.
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**: 
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **target**: Full concept IRI for the particular symptom annotation.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **specification**: IRI reference to any associated protocol.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601-formatted start date of registration
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: The patient’s age at the time the observation was taken.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **organisation**:
<hr>

(examination_glossary)=
### Examination

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Examination
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: Resulting value from this examination.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value_datatype**: XSD datatype that defines `value` column.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**: Full concept IRI for the patient attribute/finding examinated annotation.**
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **activity**: Full concept IRI for the specific method activity.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **unit**: Full concept IRI for the unit of measurement.
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **target**: Full concept IRI for the anatomic structure examinated.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **specification**: URL reference to any protocol.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**: 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601-formatted start date of the data resgitration.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: The patient’s age at the time the observation was taken.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **organisation**:

** If you are representing CARE-SM with the **OBO Foundry**, this is some example using **NCIT terms**:
  - http://purl.obolibrary.org/obo/NCIT_C25208 (Weight)
  - http://purl.obolibrary.org/obo/NCIT_C25347 (Height)
  - http://purl.obolibrary.org/obo/NCIT_C99524 (Left Ventricular Ejection Fraction)
  - http://purl.obolibrary.org/obo/NCIT_C16358 (Body Mass Index)
<hr>

(phenotype_glossary)=
### Phenotype

**This data element can be queried (in an aggregated and anonymized manner) through the Beacon API developed for CARE-SM. For more information, click [here](https://github.com/CARE-SM/beaconAPI4CARESM)**

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Phenotype
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value**: Human-readable label of the concept IRI used for `valueIRI`.
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**: 
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**: Full concept IRI for the phenotype, symptom or sign annotation.
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **target**: Full concept IRI for the anatomic region where the observation was diagnosed, including the cardinality if possible.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **specification**: IRI reference to any associated protocol.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601-formatted start date of the data resgitration.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: The patient’s age at the time the observation was taken.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **organisation**:
<hr>

(diagnosis_glossary)=
### Diagnosis

**This data element can be queried (in an aggregated and anonymized manner) through the Beacon API developed for CARE-SM. For more information, click [here](https://github.com/CARE-SM/beaconAPI4CARESM)**

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Diagnosis
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/fb9902/fb9902.png)  **value**: Human-readable label of the concept IRI used for `valueIRI`.
- ![](https://placehold.co/15x15/808080/808080.png)  **value_datatype**: 
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**: Full concept IRI for the disease or disorder diagnosed.
- ![](https://placehold.co/15x15/808080/808080.png)  **activity**:
- ![](https://placehold.co/15x15/808080/808080.png)  **unit**:
- ![](https://placehold.co/15x15/808080/808080.png)  **input**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png)  **target**: Full concept IRI for the anatomic region where the diagnosed was performed.
- ![](https://placehold.co/15x15/808080/808080.png)  **specification**:
- ![](https://placehold.co/15x15/808080/808080.png)  **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png)  **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png)  **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601-formatted start date of the data resgitration.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: The patient’s age at the time the observation was taken.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **organisation**:
<hr>

(consent_glossary)=
## Consent

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Consent
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value**: some label describing consent outcome
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**: Full concept IRI that describes the consent statement.**
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **specification**: IRI reference to any associated protocol.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601-formatted start date of the data resgitration.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: The patient’s age at the time the observation was taken.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **organisation**:

** If you are representing CARE-SM with the **OBO Foundry**, use the one of the following **DUO and OBIB terms**:
  - http://purl.obolibrary.org/obo/DUO_0000001 (Data Use Permission)
  - http://purl.obolibrary.org/obo/OBIB_0000488 (willingness to be contacted)

<hr>

(laboratory_glossary)=
### Laboratory

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Laboratory
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: value of the laboratory measurement.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value_datatype**: XSD datatype that defines `value` column.
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**: 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **activity**: Full concept IRI for the specific method annonation.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **unit**: Full concept IRI for the unit of measurement.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **input**: Full concept IRI for the substance sample analysed.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **target**: Full concept IRI for the compound measured in the sample.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **specification**: URL reference to a protocol.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**: 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601-formatted start date of the data resgitration.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: The patient’s age at the time the observation was taken.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **organisation**:
<hr>

(genotype_glossary)=
### Genetic

**This data element can be queried (in an aggregated and anonymized manner) through the Beacon API developed for CARE-SM. For more information, click [here](https://github.com/CARE-SM/beaconAPI4CARESM)**

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Genetic
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: Lexical annotation code for the genetic variant. E.g. NM-004006.2:c.4375C>T p.(Arg1459*)
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**: Full concept IRI for the genetic variant annotation.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **activity**: Full concept IRI for the specific method.
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **input**: Full concept IRI for the type of substance sample analysed.
- ![](https://placehold.co/15x15/808080/808080.png) **target**: 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **specification**: IRI reference to any associated protocol.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **agent**: Full concept IRI for the associated zygosity annotation.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601-formatted start date of the data resgitration..
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: The patient’s age at the time the observation was taken.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **organisation**:
<hr>

(questionnaire_glossary)=
### Questionnaire

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Questionnaire
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: Score/value of the patient reported response.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value_datatype**: XSD datatype that defines `value` column.
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/808080/808080.png) **activity**: 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **unit**: Full concept IRI for the unit of measurement.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **input**: Full concept IRI for the clinical question performed.
- ![](https://placehold.co/15x15/808080/808080.png) **target**: 
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **specification**: Full concept IRI for the assessment tool or Patient Reported Outcome Measures specification.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/808080/808080.png) **startdate**: ISO 8601-formatted start date of the data resgitration..
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: The patient’s age at the time the observation was taken.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **organisation**:
<hr>

(disability_glossary)=
### Disability

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Disability
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: Score/value of the patient reported response.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value_datatype**: XSD datatype that defines `value` column.
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/808080/808080.png) **activity**: 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **unit**: Full concept IRI for the unit of measurement.
- ![](https://placehold.co/15x15/808080/808080.png) **input**: Full concept IRI for the clinical question performed.
- ![](https://placehold.co/15x15/808080/808080.png) **target**: 
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **specification**: Full concept IRI for the assessment toll or questionnaire specification.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/808080/808080.png) **startdate**: ISO 8601-formatted start date of the data resgitration..
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: The patient’s age at the time the observation was taken.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **organisation**:
<hr>

(medication_glossary)=
### Medication

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Medication
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: Prescribed or Administrated dose value.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value_datatype**: XSD datatype that defines `value` column type.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**: Full concept IRI for the definition of the type of medication. (Drug Prescription or Administration).**
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **activity**: Full concept IRI for the route of administration.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **unit**: Full concept IRI for the unit of measurement.
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**: 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **specification**: URL reference to a protocol.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **frequency_type**: Full concept IRI for the administered/prescribed frequency annotation.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **frequency_value**: frequency value prescribe to the patient
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **agent**: Full concept IRI for the drugs annotation.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601-formatted start date of the data resgitration..
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: The patient’s age at the time the observation was taken.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **organisation**:

** If you are representing CARE-SM with the **OBO Foundry**, use the one of the following **NCIT terms**:
  - http://purl.obolibrary.org/obo/NCIT_C167190 (Dose Administered)
  - http://purl.obolibrary.org/obo/NCIT_C198143 (Prescribed Dose)
<hr>

(hospitalization_glossary)=
### Hospitalization

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Hospitalization
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **value**: 
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **activity**: Full concept IRI for the specific activity performed during the hospitalization.
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **specification**: URL reference to a protocol.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601-formatted start date of the data resgitration..
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: The patient’s age at the time the observation was taken.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **organisation**:
<hr>

(surgery_glossary)=
### Surgery

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Surgery
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **value**: 
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **activity**: Full concept IRI for the specific activity performed during the surgery.
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **target**: Full concept IRI for the anatomic structure that participates in the surgical intervention. 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **specification**: URL reference to a protocol.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601-formatted start date of the data resgitration..
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: The patient’s age at the time the observation was taken.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **organisation**:
<hr>

(biobank_glossary)=
### Biobank

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Biobank
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: Sample accesion number.
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**: 
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**: 
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **input**: Full concept IRI for the type of tissue/sample collected during the sampling process.
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **specification**: IRI reference to any associated protocol.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601-formatted start date of the data resgitration..
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: The patient’s age at the time the observation was taken.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **organisation**: Associated biobank identifier. 
<hr>

(clinical_trial_glossary)=
### Clinical trial

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Clinical_trial
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0..png) **value**: Study report name/identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**: 
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**: 
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **target**: Full concept IRI for the genetic or disease condition.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **specification**: IRI reference to any associated protocol.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601-formatted start date of the data resgitration..
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: The patient’s age at the time the observation was taken.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **organisation**: Medical/research center identifier associated with the clinical trial.

(cohort_glossary)=
### Cohort

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Cohort
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: Patient Unique Identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0..png) **value**: Study report name/identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**: 
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**: 
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **target**: Full concept IRI for the genetic or disease condition.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **specification**: IRI reference to any associated protocol.
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601-formatted start date of the data resgitration..
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601-formatted end date of the data registration in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: The patient’s age at the time the observation was taken.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: Additional human-readable comments.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: Visit occurrence identifier.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **organisation**: Medical/research center identifier associated with the clinical trial.
