# Bug reports

## Application only adds 65 records to Finals folder, even though Originals folder contained over 1000 records (all of which were in the allowlist)

#### Test purpose: 
Check behaviour of application for high number of records.

#### Expected output:
All created records in originals folder to be added to finals folder.

#### Actual output:
Only 65 records were in finals folder after running application.

#### Instructions for test recreation:
1. Install faker in your python environment by running
    pip install Faker
2. Run challenge_test_setup.py with the following input
    Data seed: 1
    Number of records: 1500
    Allowlist or droplist: A
    Updates: DONE (nothing copied to updates)
3. Run document_updater.py
4. Check number of items in originals and finals folders (you can use finder for this)

___

## When using allowlist, application only adds Originals records to Finals that are also in referenced in Updates folder

#### Test purpose: 
Determine if program adds all records to Finals folder, with the ones in Updates in their updated format.

#### Expected output:
Originals records copied to Finals with relevant updates.

#### Actual output:
Only original records also in Updates folder were copied to Finals folder.

#### Instructions for test recreation:
1. Install faker in your python environment by running
    pip install Faker
2. Run challenge_test_setup.py with the following input
    Data seed: 1
    Number of records: 5
    Allowlist or droplist: A
    Updates: Hardy
             Riley
             DONE
3. Open Hardy file in Updates folder and change address to Flat 3456
4. Open Riley file in Updates folder and change name to Mr Damian Riley
5. Run document_updater.py
4. Check finals folder only contains records for Hardy and Riley
