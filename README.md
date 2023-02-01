### Description of challenge approach

The approach to testing this application was multifaceted. 

Initially all of the folder and file structure the application description set as essential was manually removed and subsequently the application run to test if error messaging occured as expected.
After each error message the referenced missing folder was added and the next test attemped.
The report for this is in the .pdf 'Folder Structure'

Subsequentely a challenge_test_setup.py was created. When run, this script clears everything in target directory, recreates the essential directories, asks the user to choose a seed for the test data, asks for number of records to create in originals, and wether the user would like to use an allowlist or droplist. It also prompts the user to select records in the original records to copy into the updates folder (one at a time), to facilitate setting up test cases.

Afterwards, excalidraw was used to create a diagram that lays out the application states/transitions and relates them to different test cases as well as their expected outcome.
This diagram is in the .png 'diagram'

Finally some of the prepared test scenarios were run with the most relevant ones described in the table below.

|Test|Originals|Faker data seed|Droplist|Allowlist|Updates|Outcome|
|---|---|---|---|---|---|---|
|1.|5 records|1|Does not exist|Exists but empty|Empty|Application error - list index out of range|
|2.|5 records|1|Does not exist|References all records in Originals and Updates|Contains updated versions of 2 of the records in Originals|Only the records referenced in Updates ended up in Finals (in their Updates version)|
|3.|5 records|1|References only records in Updates that do not exist in Originals|Does not exist|Contains 2 new records that are not referenced in Originals|Application error - [Errno 17] File exists: 'blends'. Finals was empty and a new directory called blends was created. This directory contained one of the records in updates|
|4.|Over 1000 records|1|Does not exist|Exists for all original records|Empty|Only 65 out of the expected 1000 end up in Finals|
|5.|100 records|1|Does not exist|Exists for all original records|Empty|Records with hyphen or accents in name end up in Finals without hyphen/accent|

Test 1

![Screenshot 2023-02-01 at 12 15 00](https://user-images.githubusercontent.com/115627873/216039935-4a1c1285-122b-4861-b66a-50e03d76d1da.png)
![Screenshot 2023-02-01 at 12 15 49](https://user-images.githubusercontent.com/115627873/216040047-c5a90633-99c8-4b9b-9be4-303eaa1a36d6.png)


Test 2

![Screenshot 2023-02-01 at 10 03 52](https://user-images.githubusercontent.com/115627873/216038913-84f75c2a-315e-4c7d-9b9c-f2f8f8f0e244.png)

Test 3

![Screenshot 2023-02-01 at 10 14 47](https://user-images.githubusercontent.com/115627873/216039065-a3921be5-e952-4234-8e7b-52eb74421789.png)
![Screenshot 2023-02-01 at 10 15 02](https://user-images.githubusercontent.com/115627873/216039134-9f0f779f-f59e-47e7-8222-b13e25d20b50.png)

Test 4

![Screenshot 2023-02-01 at 10 26 19](https://user-images.githubusercontent.com/115627873/216039313-46b4d48e-614c-4e73-b45c-157039882c44.png)

Test 5

![Screenshot 2023-02-01 at 10 30 23](https://user-images.githubusercontent.com/115627873/216039404-b66ad0b3-1e47-42d1-beac-1ce09fc4171f.png)



