The approach to testing this application was multifaceted. 

Initially all of the folder and file structure the application description set as essential was manually removed and subsequently the application run to test if error messaging occured as expected.
After each error message the referenced missing folder was added and the next test attemped.
The report for this is in the .pdf 'Folder Structure'

Subsequentely a challenge_test_setup.py was created. When run, this script clears everything in target directory, recreates the essential directories, asks the user to choose a seed for the test data, asks for number of records to create in originals, and wether the user would like to use an allowlist or droplist. It also prompts the user to select records in the original records to copy into the updates folder (one at a time), to facilitate setting up test cases.

Afterwards, excalidraw was used to create a diagram that lays out the application states/transitions and relates them to different test cases as well as their expected outcome.
This diagram is in the .png 'diagram'



|Test|Originals|Faker data seed|Droplist|Allowlist|Updates|Outcome|
|---|---|---|---|---|---|---|
|1.|5 records|1|Does not exist|Exists but empty|Empty|Application error - list index out of range|
|2.|5 records|1|Does not exist|References all records in Originals and Updates|Contains updated versions of 2 of the records in Originals|Only the records referenced in Updates ended up in Finals (in their Updates version)|
|3.|5 records|1|References only records in Updates that do not exist in Originals|Does not exist|Contains 2 new records that are not referenced in Originals|Application error - [Errno 17] File exists: 'blends'. Finals was empty and a new directory called blends was created. This directory contained one of the records in updates|
|4.|Over 1000 records|1|Does not exist|Exists for all original records|Empty|Only 65 out of the expected 1000 end up in Finals|
|5.|100 records|1|Does not exist|Exists for all original records|Empty|Records with hyphen or accents in name end up in Finals without hyphen/accent|