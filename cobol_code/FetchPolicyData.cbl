IDENTIFICATION DIVISION.
PROGRAM-ID. FetchPolicyData.
AUTHOR. Udit Sharma.
DATE-WRITTEN. 2023-07-21.
DATE-COMPILED.
DATA DIVISION.
WORKING-STORAGE SECTION.
01 PolicyDB2File.
   05 PolicyDB2Record OCCURS 10 TIMES.
      10 Policy-Number      PIC X(10).
      10 Policy-Holder-Name PIC X(50).
      10 Premium-Amount     PIC 9(9)V99.
      10 Policy-Type        PIC X(15).  // Increased the size to accommodate the longest policy_type
      10 Coverage-Limits    PIC 9(9)V99.
      10 Policy-Premium     PIC 9(9)V99.
      10 Age                PIC 9(3).
      10 Car-Value          PIC 9(9)V99.
      10 Property-Type      PIC X(20).
      10 Property-Value     PIC 9(9)V99.
      10 Coverage-Amount    PIC 9(9)V99.

PROCEDURE DIVISION USING PolicyDB2File, WS-Sort-Buffer.
    DISPLAY "Fetching policy data from DB2..."
    PERFORM VARYING Record-Count FROM 1 BY 1
      UNTIL Record-Count > 10
      MOVE SPACES TO PolicyDB2Record(Record-Count)

      // Simulate fetching random data for each policy record
      MOVE "POLICY00" & Record-Count TO Policy-Number(Record-Count)
      MOVE "Policy Holder " & Record-Count TO Policy-Holder-Name(Record-Count)
      COMPUTE Premium-Amount(Record-Count) = Record-Count * 100.50
      MOVE RANDOM-POLICY-TYPE TO Policy-Type(Record-Count)
      COMPUTE Coverage-Limits(Record-Count) = Record-Count * 1000
      COMPUTE Policy-Premium(Record-Count) = Record-Count * 200.75
      MOVE Record-Count TO Age(Record-Count)
      COMPUTE Car-Value(Record-Count) = Record-Count * 5000.50
      MOVE RANDOM-PROPERTY-TYPE TO Property-Type(Record-Count)
      COMPUTE Property-Value(Record-Count) = Record-Count * 10000.25
      COMPUTE Coverage-Amount(Record-Count) = Record-Count * 5000
    END-PERFORM.
    DISPLAY "Policy data fetched."
    EXIT PROGRAM.

RANDOM-POLICY-TYPE SECTION.
01 Random-Policy-Type PIC X.
PROCEDURE DIVISION.
    MOVE FUNCTION RANDOM(3) TO Random-Policy-Type
    IF Random-Policy-Type = 1
        MOVE "CAR_INSURANCE" TO Random-Policy-Type
    ELSE IF Random-Policy-Type = 2
        MOVE "HOME_INSURANCE" TO Random-Policy-Type
    ELSE
        MOVE "LIFE_INSURANCE" TO Random-Policy-Type
    END-IF.
    EXIT PROGRAM.

RANDOM-PROPERTY-TYPE SECTION.
01 Random-Property-Type PIC X.
PROCEDURE DIVISION.
    MOVE FUNCTION RANDOM(3) TO Random-Property-Type
    IF Random-Property-Type = 1
        MOVE "Condo" TO Random-Property-Type
    ELSE IF Random-Property-Type = 2
        MOVE "Townhouse" TO Random-Property-Type
    ELSE
        MOVE "Single-family home" TO Random-Property-Type
    END-IF.
    EXIT PROGRAM.
