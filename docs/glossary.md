# CARE-SM CSV Glossasy Documentation

This guide explains how to structure, populate, and utilize CSV files for patient data in CARE-SM.

## CSV template creation

1. **Create the CSV File**  
   
   This document would only allow a set of concrete columns names:
   - `model`, `pid`, `event_id`, `value`, `age`, `value_datatype`, `valueIRI`, `activity`, `unit`, `input`, `target`, `protocol_id`, `frequency_type`, `frequency_value`, `agent`, `startdate`, `enddate`, `comments`

   *Example:*
   ```text
   model,pid,event_id,value,age,value_datatype,valueIRI,activity,unit,input,target,protocol_id,frequency_type,frequency_value,agent,startdate,enddate,comments
   ,,,,,,,,,,,,,,,,,
   ```
2. **Populate Data**  
   Each data entry needs specific fields (not all fields are mandatory). See the glossary below for details.

    *Example:*
    ```text
    model,pid,event_id,value,age,value_datatype,valueIRI,activity,unit,input,target,protocol_id,frequency_type,frequency_value,agent,startdate,enddate,comments
    Diagnosis,30056,,,,,http://www.orpha.net/ORDO/Orphanet_93552,,,,,,,,,,,2006-01-19,,
    ```

    For more examples, refer to the [`exemplar_data`](https://github.com/CARE-SM/CARE-SM-Implementation/tree/main/CSV/data) folder.

## Data Element Glossary
<!-- 
* Demographics:
    * {ref}`birthdate`
    * {ref}`birthyear`
    * {ref}`deathdate`
    * {ref}`sex`
    * {ref}`education`

* Participation and Timeline:
    * {ref}`first_visit`
    * {ref}`status`
    * {ref}`symptoms_onset`

* Conditions and findings:
    * {ref}`diagnosis`
    * {ref}`phenotype`

* Clinical and molecular measurements:
    * {ref}`laboratory`
    * {ref}`corporal`
    * {ref}`imaging`
    * {ref}`genotype`

* Patient-reported outcomes:
    * {ref}`disability`
    * {ref}`questionnaire`

* Treatment and interventions:
    * {ref}`medication`
    * {ref}`surgery`

* Research:
    * {ref}`biobank`
    * {ref}`clinical_trial`
-->


**Legend:**

- ![](https://placehold.co/15x15/808080/808080.png) This column is **UNUSED** for this case.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) This column is filled in **IN CASE OF ANY**.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) This column colored is **REQUIRED** for this case.

Here you can find the list of data elements and the columns required to be defined. Those that are optional, feel free to add them. If not, leave them empty.
<hr>

(birthdate_glossary)=
### Birthdate

**This data element can be queried (for counting anonymized patient information) by Beacon API created for CARE-SM, for more information, click [here](https://github.com/CARE-SM/beaconAPI4CARESM)**

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Birthdate
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: patient unique identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: ISO 8601 formatted date (not date time)
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation, could be the same of the `value`
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/808080/808080.png) **age**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of this data elements under the same visit occurrence event.
<hr>

(birthyear_glossary)=
### Birthyear

**This data element can be queried (for counting anonymized patient information) by Beacon API created for CARE-SM, for more information, click [here](https://github.com/CARE-SM/beaconAPI4CARESM)**

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Birthdate
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: patient unique identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: The year in which a person was born. E.g. 1984
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/808080/808080.png) **startdate**:
- ![](https://placehold.co/15x15/808080/808080.png) **enddate**:
- ![](https://placehold.co/15x15/808080/808080.png) **age**: 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of this data elements under the same visit occurrence event.
<hr>

(country_glossary)=
### Country at birth

**This data element can be queried (for counting anonymized patient information) by Beacon API created for CARE-SM, for more information, click [here](https://github.com/CARE-SM/beaconAPI4CARESM)**

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Country
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in form of a patient identifier.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value**: human readable label, e.g. Spain
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**: 
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**:  Full IRI used as annonation code for the country at birth.
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/808080/808080.png) **age**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.
<hr>

(deathdate_glossary)=
### Deathdate

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Deathdate
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: ISO 8601 formatted date of death (not date time)
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **valueIRI**: Full IRI used as annonation code for the cause of the patient death.
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation, could be the same of the `value`
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: Besides its named as "Deathdate", accepts "Age of Death" using this `age` column. Patient age when this observation was taken, this age information can be both an addition or an alternative for `value`/`startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.
<hr>

(sex_glossary)=
### Sex

**This data element can be queried (for counting anonymized patient information) by Beacon API created for CARE-SM, for more information, click [here](https://github.com/CARE-SM/beaconAPI4CARESM)**

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Sex
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in form of a patient identifier.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value**: human readable label, e.g. Female
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**: 
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**: one of the following: 
    * http://purl.obolibrary.org/obo/NCIT_C16576 (Female) ; 
    * http://purl.obolibrary.org/obo/NCIT_C20197 (Male); 
    * http://purl.obolibrary.org/obo/NCIT_C124294 (Undetermined) ; 
    * http://purl.obolibrary.org/obo/NCIT_C17998 (Unknown, use this for foetal undetermined) 
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/808080/808080.png) **age**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.
<hr>

<!-- (education_glossary)=
### Education

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Education
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: International Standard Classification of Education score. E.g. 7
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**: 
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**: 
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: patient age when this observation was taken, this age information can be both an addition or an alternative for `startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.
<hr> -->

(first-visit_glossary)=
### First Confirmed Visit

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: First_visit
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value**: ISO 8601 formatted date of first confirmed visit (not date time). Its required to add at least one the following: `value` and/or `age` column (preferably `value`)
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation, could be the same of the `value`
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: Patient age when this observation was taken, this age information can be both an addition or an alternative for `value`/`startdate`/`enddate` information. It's required to add at least one the following: `value` and/or `age` column (preferably `value`). Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.
<hr>

(status_glossary)=
### Participation status

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Status
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value**: any human readable response, e.g. Lost of follow-up
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**: 
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**: one of the following: 
    * http://semanticscience.org/resource/SIO_010059 (dead)
    * http://semanticscience.org/resource/SIO_010058 (alive)
    * http://purl.obolibrary.org/obo/NCIT_C70740 (lost to follow-up)
    * http://purl.obolibrary.org/obo/NCIT_C124784 (refused to participate)
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: Patient age when this observation was taken, this age information can be both an addition or an alternative for `startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of this data elements under the same visit occurrence event.
<hr>

(symptoms_onset_glossary)=
### Symptoms onset

**This data element can be queried (for counting anonymized patient information) by Beacon API created for CARE-SM, for more information, click [here](https://github.com/CARE-SM/beaconAPI4CARESM)**

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Symptoms_onset
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: age or date of symptoms occurrence (Do not confuse with `startdate`/`enddate`/`age` for defining when this observation was registered).
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value_datatype**: XSD datatype that defines `value` column.`xsd:date` for date or `xsd:integer` for age. (xsd:float is not included as an option because fractional ages are not accepted by CARE-SM Toolkit).
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**: 
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **target**: URI based ontological term that defines symptom/phenotype measured, in case of any. E.g. HP ontological term for the symptom.
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: Patient age when this observation was taken, this age information can be both an addition or an alternative for `startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.
<hr>

(examination_glossary)=
### Examination

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Examination
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: Resulting value from this examination
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value_datatype**: XSD datatype that defines `value` column type, e.g. `xsd:float` or `xsd:integer` for numerical values. In case of none, `xsd:float` will be added by default.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**: Full IRI used for defining the patient attribute/finding examinated, e.g.:
    * [NCIT:Weight](http://purl.obolibrary.org/obo/NCIT_C25208)
    * [NCIT:Height](http://purl.obolibrary.org/obo/NCIT_C25347)
    * [Left Ventricular Ejection Fraction](http://purl.obolibrary.org/obo/NCIT_C99524)
    * [NCIT:Body Mass Index](http://purl.obolibrary.org/obo/NCIT_C16358)
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **activity**: Full IRI used for pecific method activity.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **unit**: child of UO:unit http://purl.obolibrary.org/obo/UO_0000000
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **target**: Full IRI used for annonatating the anatomic structure examinated.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **protocol_id**: URL reference to a protocol, e.g. https://protocols.io deposit or any identifier that describes the specific properties of this clinical procedure. E.g. https://www.protocols.io/view/hplc-sample-prep-4r3l25ew4l1y/v1
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**: 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: Patient age when this observation was taken, this age information can be both an addition or an alternative for `startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.
<hr>


(phenotype_glossary)=
### Phenotype

**This data element can be queried (for counting anonymized patient information) by Beacon API created for CARE-SM, for more information, click [here](https://github.com/CARE-SM/beaconAPI4CARESM)**

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Phenotype
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **value**:
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**: 
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**: IRI that defines clinical phenotypic symptom or sign: For example Human Phenotype ontology (HPO) term represented with a full URL such as http://purl.obolibrary.org/obo/HP_0001251
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **target**: Full IRI used to describe the anatomic region where the observation was discovered or to which it is associated. E.g., http://purl.obolibrary.org/obo/NCIT_C105633 (Left Arm)
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: Patient age when this observation was taken, this age information can be both an addition or an alternative for `startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.
<hr>

(diagnosis_glossary)=
### Diagnosis

**This data element can be queried (for counting anonymized patient information) by Beacon API created for CARE-SM, for more information, click [here](https://github.com/CARE-SM/beaconAPI4CARESM)**

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Diagnosis
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/fb9902/fb9902.png)  **value**: Human readable label of the diagnosed condition.
- ![](https://placehold.co/15x15/808080/808080.png)  **value_datatype**: 
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**: Full IRI that defines clinical condition as disease or disorder: Orphanet disease ontology (ORDO), such as http://www.orpha.net/ORDO/Orphanet_199630. **NOTE:** For confirmed undiagnosed cases, please use: ORDO:Orphanet_616874 (full IRI)
- ![](https://placehold.co/15x15/808080/808080.png)  **activity**:
- ![](https://placehold.co/15x15/808080/808080.png)  **unit**:
- ![](https://placehold.co/15x15/808080/808080.png)  **input**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png)  **target**: Full IRI used to describe the anatomic region where the diagnosis was discovered or to which it is associated. E.g., http://purl.obolibrary.org/obo/NCIT_C105633 (Left Arm)
- ![](https://placehold.co/15x15/808080/808080.png)  **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png)  **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png)  **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png)  **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: Patient age when this observation was taken, this age information can be both an addition or an alternative for `startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.
<hr>


<!-- 

## Consent for being contacted for research:

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Consent_contacted
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value**: some label describing consent outcome
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: patient age when this observation was taken, this age information can be both an addition or an alternative for `startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.

## Consent for data (re)use permission:

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Consent_used
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value**: some label describing consent outcome
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: patient age when this observation was taken, this age information can be both an addition or an alternative for `startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.
<hr>

-->

(laboratory_glossary)=
### Laboratory

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Laboratory
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: resulting value from this analysis.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value_datatype**: XSD datatype that defines `value` column type, e.g. `xsd:float` or `xsd:integer` for numerical values. In case of none, `xsd:float` will be added by default.
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**: 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **activity**: Specific method in form of an ontological class that describe the process, e.g. NCIT:Creatinine Clearance Adjusted for BSA: http://purl.obolibrary.org/obo/NCIT_C147324
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **unit**: child of UO:unit http://purl.obolibrary.org/obo/UO_0000000
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **input**: material input represented as Child of Anatomic, Structure, System, or Substance http://purl.obolibrary.org/obo/NCIT_C12219 (e.g: obo:Urine)
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **target**: compound being measured in the sample. Child of Drug, Food, Chemical or Biomedical Material http://purl.obolibrary.org/obo/NCIT_C1908 (e.g. obo:Creatinine http://purl.obolibrary.org/obo/NCIT_C399)
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **protocol_id**: URL reference to a protocol, e.g. https://protocols.io deposit or any identifier that describes the specific properties of this clinical procedure. E.g. https://www.protocols.io/view/hplc-sample-prep-4r3l25ew4l1y/v1
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**: 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: patient age when this observation was taken, this age information can be both an addition or an alternative for `startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.
<hr>

<!-- (imaging_glossary)=
### Medical imaging

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Imaging
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **value**: 
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**: 
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**: medical imagine GUID of the file (must be a GUID system compatible with RDF Resource identifiers)
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **activity**: child of Imaging technique http://purl.obolibrary.org/obo/NCIT_C17369  (e.g. obo:Digital X-Ray http://purl.obolibrary.org/obo/NCIT_C18001)
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **target**: child of Anatomic Structure, System, or Substance http://purl.obolibrary.org/obo/NCIT_C12219 (e.g. obo:Palmar Region http://purl.obolibrary.org/obo/NCIT_C33252)
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **protocol_id**: URL reference to a protocol, e.g. https://protocols.io deposit or any identifier that describes the specific properties of this clinical procedure. E.g. https://www.protocols.io/view/anatomical-variations-and-dimensions-of-the-poplit-3byl4qqk8vo5
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: patient age when this observation was taken, this age information can be both an addition or an alternative for `startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.
<hr> -->

(genotype_glossary)=
### Genetic

**This data element can be queried (for counting anonymized patient information) by Beacon API created for CARE-SM, for more information, click [here](https://github.com/CARE-SM/beaconAPI4CARESM)**

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Genetic
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: Lexical Annonatation code for the genetic variant. E.g. NM-004006.2:c.4375C>T p.(Arg1459*)
- ![](https://placehold.co/15x15/808080/808080.png)  **value_datatype**:
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**: Genetic variant code constructed by appending the HGNC/OMIM/HGVS annotation, e.g. https://www.ncbi.nlm.nih.gov/clinvar/RCV000008537
- ![](https://placehold.co/15x15/fb9902/fb9902.png)  **activity**: Specific method in form of an ontological class that describe the process, e.g. NCIT:Microarray Analysis: http://purl.obolibrary.org/obo/NCIT_C18477
- ![](https://placehold.co/15x15/808080/808080.png)  **unit**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png)  **input**: Anatomical structure where the sample was extracted. Recommended a child of NCIT:Biospecimen or NCIT:Anatomic Structure, System, or Substance, e.g. NCIT:Blood Sample: http://purl.obolibrary.org/obo/NCIT_C17610
- ![](https://placehold.co/15x15/fb9902/fb9902.png)  **target**: Zygosity associated with this particular genetic variant. Defined by GENO OBO Foundry ontology: One of the following:
    * [GENO:hemizygosity](http://purl.obolibrary.org/obo/GENO_0000134)
    * [GENO:heterozygosity](http://purl.obolibrary.org/obo/GENO_0000135)
    * [GENO:homozygosity](http://purl.obolibrary.org/obo/GENO_0000136)
    * [GENO:nullizygosity](http://purl.obolibrary.org/obo/GENO_0000978)
    * [GENO:compound heterozygosity](http://purl.obolibrary.org/obo/GENO_0000402)
- ![](https://placehold.co/15x15/808080/808080.png)  **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png)  **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png)  **frequency_value**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png)  **agent**: IRI describing the level of pathogenecity of the sequence variant.
<!--  Molecular target type, refering to the level of molecular dogma central studied by the genetic variant. Some of the examples terminology from NCIT:
    * [NCIT:Gene](http://purl.obolibrary.org/obo/NCIT_C16612)
    * [NCIT:Gene Variant](http://purl.obolibrary.org/obo/NCIT_C97927)
    * [NCIT:Protein](http://purl.obolibrary.org/obo/NCIT_C17021)
    * [NCIT:Messenger RNA](http://purl.obolibrary.org/obo/NCIT_C813)
    * [NCIT:Transfer RNA](http://purl.obolibrary.org/obo/NCIT_C816)
    * [NCIT:Mitochondrial RNA](http://purl.obolibrary.org/obo/NCIT_C25975) -->

- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: Patient age when this observation was taken, this age information can be both an addition or an alternative for `startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.
<hr>

(questionnaire_glossary)=
### Questionnaire

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Questionnaire
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: Score/value of the reported outcome.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value_datatype**: XSD datatype that defines `value` column type, e.g. `xsd:float` por a decimal score.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**: Full URI/IRI that defines the specific clinical question defined in the questionnaire or Patient Reported Outcome (PRO).
- ![](https://placehold.co/15x15/808080/808080.png) **activity**: 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **unit**: unit of measurement coming from the reported outcome.
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**: 
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/808080/808080.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: Patient age when this observation was taken, this age information can be both an addition or an alternative for `startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of this data elements under the same visit occurrence event.
<hr>

(disability_glossary)=
### Disability

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Disability
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: Score/value of the assessment.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value_datatype**: XSD datatype that defines `value` column type, e.g. `xsd:float` in case of a decimal score.
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **activity**: Full IRI that defines the specific clinical assessment. Some examples are presented. E.g. http://purl.obolibrary.org/obo/NCIT_C107391  for Edmonton symptom disability assessment .
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **unit**: unit of measurement coming from the resulting assessment score/value.
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: Patient age when this observation was taken, this age information can be both an addition or an alternative for `startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.
<hr>

(prescription_glossary)=
### Prescription

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Prescription
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: dose value prescribed to the patient
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value_datatype**: XSD datatype that defines `value` column type, e.g. `xsd:float` or `xsd:integer` for numerical values.
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**: 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **activity**: child of Route of Administration http://purl.obolibrary.org/obo/NCIT_C38114 (e.g. obo:Sublingual Route of Administration http://purl.obolibrary.org/obo/NCIT_C38300 )
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **unit**: child of UO:unit http://purl.obolibrary.org/obo/UO_0000000
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**: 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **protocol_id**: URL reference to a protocol, e.g. https://protocols.io deposit or any identifier that describes the specific properties of this clinical procedure. E.g. https://www.protocols.io/view/hplc-sample-prep-4r3l25ew4l1y/v1
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **frequency_type**: child of obo:Temporal Qualifier http://purl.obolibrary.org/obo/NCIT_C21514 (e.g. obo:Per Day)
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **frequency_value**: frequency value prescribe to the patient
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **agent**: Full IRI used as annotation code for drugs components. (e.g. https://www.whocc.no/atc_ddd_index/?code=A07EA01)
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: patient age when this observation was taken, this age information can be both an addition or an alternative for `startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.
<hr>

(medication_glossary)=
### Medication

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Medication
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: dose value administered to the patient
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **value_datatype**: XSD datatype that defines `value` column type, e.g. `xsd:float` or `xsd:integer` for numerical values.
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**: 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **activity**: Full IRI for the route of administration, e.g.,[Sublingual Route of Administration](http://purl.obolibrary.org/obo/NCIT_C38300)
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **unit**: child of UO:unit http://purl.obolibrary.org/obo/UO_0000000
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**: 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **protocol_id**: URL reference to a protocol, e.g. https://protocols.io deposit or any identifier that describes the specific properties of this clinical procedure. E.g. https://www.protocols.io/view/hplc-sample-prep-4r3l25ew4l1y/v1
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **frequency_type**: child of obo:Temporal Qualifier http://purl.obolibrary.org/obo/NCIT_C21514 (e.g. obo:Per Day)
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **frequency_value**: frequency value prescribe to the patient
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **agent**: Full IRI used as annotation code for drugs components. (e.g. https://www.whocc.no/atc_ddd_index/?code=A07EA01)
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: patient age when this observation was taken, this age information can be both an addition or an alternative for `startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.
<hr>

(hospitalization_glossary)=
### Hospitalization

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Hospitalization
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **value**: 
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **activity**: Full IRI used for annotating the specific activity performed during the hospitalization, e.g.: [obo:Tumor Resection](http://purl.obolibrary.org/obo/NCIT_C164212)
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **protocol_id**: URL reference to a protocol, e.g. https://protocols.io deposit or any identifier that describes the specific properties of this clinical procedure. E.g. https://www.protocols.io/view/hplc-sample-prep-4r3l25ew4l1y/v1
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: patient age when this observation was taken, this age information can be both an addition or an alternative for `value`/`startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.
<hr>

(surgery_glossary)=
### Surgery

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Surgery
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **value**: 
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**:
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**:
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **activity**: Full IRI used for annotating the specific activity performed during the hospitalization, e.g.: [obo:Tumor Resection](http://purl.obolibrary.org/obo/NCIT_C164212)
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **target**: Full IRI for anatomic structure that participates in the surgical intervention. 
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **protocol_id**: URL reference to a protocol, e.g. https://protocols.io deposit or any identifier that describes the specific properties of this clinical procedure. E.g. https://www.protocols.io/view/hplc-sample-prep-4r3l25ew4l1y/v1
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/808080/808080.png) **agent**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: patient age when this observation was taken, this age information can be both an addition or an alternative for `value`/`startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.
<hr>

(biobank_glossary)=
### Biobank

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Biobank
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **value**: sample identifier
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**: 
- ![](https://placehold.co/15x15/808080/808080.png) **valueIRI**: 
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **input**: tissue/sample collected during the sampling process. E.g. Cerebrospinal Fluid http://purl.obolibrary.org/obo/NCIT_C12692
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **agent**: biobank Identifier, e.g. https://directory.bbmri-eric.eu/biobankid
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: patient age when this observation was taken, this age information can be both an addition or an alternative for `startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.
<hr>

(clinical_trial_glossary)=
### Clinical trial

- ![](https://placehold.co/15x15/1589F0/1589F0.png) **model**: Clinical_trial
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **pid**: individual identifier, in the form of a patient identifier.
- ![](https://placehold.co/15x15/808080/808080.png) **value**:
- ![](https://placehold.co/15x15/808080/808080.png) **value_datatype**: 
- ![](https://placehold.co/15x15/1589F0/1589F0.png) **valueIRI**: IRI that defines clinical condition as disease or disorder: Orphanet disease ontology (ORDO) represented with a full URL such as http://www.orpha.net/ORDO/Orphanet_199630
- ![](https://placehold.co/15x15/808080/808080.png) **activity**:
- ![](https://placehold.co/15x15/808080/808080.png) **unit**:
- ![](https://placehold.co/15x15/808080/808080.png) **input**:
- ![](https://placehold.co/15x15/808080/808080.png) **target**:
- ![](https://placehold.co/15x15/808080/808080.png) **protocol_id**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_type**:
- ![](https://placehold.co/15x15/808080/808080.png) **frequency_value**:
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **agent**: GUID for this medical center where this clinical trial is taking place.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **startdate**: ISO 8601 formatted start date of observation
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **enddate**: ISO 8601 formatted enddate of observation in case it is different from `startdate`.  
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **age**: patient age when this observation was taken, this age information can be both an addition or an alternative for `startdate`/`enddate` information. Its units are fractional years, so it accepts any decimal figure for age. E.g. 33.75 years.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **comments**: human readable comments of any kind related to this procedure.
- ![](https://placehold.co/15x15/fb9902/fb9902.png) **event_id**: contextual identifier (formatted as `integer`) used for relating several of these data elements under the same visit occurrence event.